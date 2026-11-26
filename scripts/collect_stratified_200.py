#!/usr/bin/env python3
"""Collect COMPLETE fixed-period Steam review frames and draw seeded samples.

The source collector is the tested fetch_period function in the A5 notebook.
Plaintext is never committed. Public files contain metadata only.
"""
import base64
import gzip
import hashlib
import json
import os
import time
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

nb = json.loads(Path("HCDE410_A4_Proposal.ipynb").read_text("utf-8"))
code = next("".join(c["source"]) for c in nb["cells"]
            if c["cell_type"] == "code" and "def fetch_period(" in "".join(c["source"]))
if "RUN_LIVE_PILOT = False" not in code:
    raise RuntimeError("Unexpected source notebook; review it before collecting")
ns = {}
exec(compile(code, "A5:fetch_period", "exec"), ns)
fetch_period = ns["fetch_period"]
periods = ns["PERIODS"]
out = Path("data")
private = Path("data_private")
secure = Path("data_encrypted")
for p in (out, private, secure):
    p.mkdir(exist_ok=True)

frame_parts, sample_parts, statuses, samples_per_period = [], [], [], {}
for i, label in enumerate(periods):
    frame, stat = fetch_period(label, max_pages=50, page_size=100, wait_seconds=1.5)
    api_count = stat["matching_reported"]
    if not stat["complete_frame"] or api_count is None or stat["seen_ids"] != api_count:
        raise RuntimeError("Incomplete sampling frame for " + label + ": " + str(stat))
    if len(frame) == 0 or frame["review_id"].duplicated().any():
        raise RuntimeError("Missing or duplicate review IDs in " + label)
    stat["validated_review_rows"] = len(frame)
    stat["nonblank_eligible"] = int(frame["review"].fillna("").str.strip().ne("").sum())
    stat["blank_excluded"] = len(frame) - stat["nonblank_eligible"]
    stat["edited"] = int((frame["updated_utc"] != frame["created_utc"]).sum())
    statuses.append(stat)
    frame_parts.append(frame)
    eligible = frame[frame["review"].fillna("").str.strip().ne("")].copy()
    eligible["_numeric_id"] = eligible["review_id"].map(int)
    eligible = eligible.sort_values("_numeric_id").drop(columns="_numeric_id")
    candidate_count = min(50, len(eligible))
    picked = eligible.sample(n=candidate_count, random_state=410 + i)
    picked = picked.reset_index(drop=True).copy()
    picked.insert(0, "selection", ["primary" if j < 40 else "reserve"
                                    for j in range(candidate_count)])
    picked.insert(0, "sample_id", [
        "CIV6_" + label.split("_")[-1] + "_" + str(j + 1).zfill(3)
        for j in range(candidate_count)
    ])
    sample_parts.append(picked)
    samples_per_period[label] = {
        "primary_count": min(40, candidate_count),
        "reserve_count": max(0, candidate_count - 40),
        "full_frame_nonblank_count": len(eligible),
    }
    print("VERIFIED FRAME", label, "matched:", stat["seen_ids"],
          "validated:", len(frame), "pages_cap:", stat["pages_requested_max"],
          "primary:", samples_per_period[label]["primary_count"])
    time.sleep(1.5)

full = pd.concat(frame_parts, ignore_index=True)
selected = pd.concat(sample_parts, ignore_index=True)
full_path = private / "full_steam_frame_private.csv"
sample_path = private / "steam_200_plus_reserves_private.csv"
full.to_csv(full_path, index=False)
selected.to_csv(sample_path, index=False)
public = selected[["sample_id", "selection", "period",
                   "created_utc", "edited_since_creation",
                   "playtime_at_review_hours"]].copy()
public["created_month_utc"] = public["created_utc"].str.slice(0, 7)
public["review_char_length"] = selected["review"].fillna("").str.len()
public["review_word_count"] = selected["review"].fillna("").str.split().str.len()
public = public.drop(columns="created_utc")
public.to_csv(out / "stratified_sample_features.csv", index=False)

pubkey = serialization.load_pem_public_key(
    Path("scripts/steam_pilot_public_key.pem").read_bytes()
)
def protect(input_path, encrypted_path):
    data = input_path.read_bytes()
    symkey = os.urandom(32)
    nonce = os.urandom(12)
    cipher = AESGCM(symkey).encrypt(
        nonce, gzip.compress(data, compresslevel=9), b"HCDE410_STEAM_PILOT_V1"
    )
    wrapped = pubkey.encrypt(symkey, padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(), label=None))
    enc = lambda x: base64.b64encode(x).decode("ascii")
    envelope = {
        "format": "HCDE410_STEAM_PILOT_V1",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "algorithm": "gzip + AES-256-GCM + RSA-OAEP-SHA256",
        "public_key_file": "scripts/steam_pilot_public_key.pem",
        "encrypted_key_b64": enc(wrapped),
        "nonce_b64": enc(nonce),
        "encrypted_data_b64": enc(cipher),
        "sha256_raw_csv": hashlib.sha256(data).hexdigest(),
    }
    encrypted_path.write_text(json.dumps(envelope, indent=2) + "\n", "utf-8")
    return envelope["sha256_raw_csv"]

full_sha = protect(full_path, secure / "steam_complete_frame_encrypted.json")
sample_sha = protect(sample_path, secure / "steam_stratified_sample_encrypted.json")
manifest = {
    "app_id": 289070,
    "source": "https://api.steampowered.com/IUserReviewsService/GetAppReviews/v1/",
    "collected_at_utc": datetime.now(timezone.utc).isoformat(),
    "sampling_method": "Complete frames followed by random sample (seed 410+period index) after sorting numeric review IDs",
    "seed_base": 410,
    "filters": {"review_type": "negative", "purchase_type": "Steam",
                "language": "english", "filter": "Recent",
                "filter_offtopic_activity": True},
    "periods": periods,
    "frames": statuses,
    "per_period_draws": samples_per_period,
    "all_frames_complete": all(s["complete_frame"] and
                               s["seen_ids"] == s["matching_reported"]
                               for s in statuses),
    "total_api_ids": sum(s["seen_ids"] for s in statuses),
    "total_validated_api_rows": len(full),
    "primary_candidate_n": int((selected["selection"] == "primary").sum()),
    "reserve_candidate_n": int((selected["selection"] == "reserve").sum()),
    "sha256_full_private": full_sha, "sha256_sample_private": sample_sha,
    "cautions": [
        "This is a drawn sample, not yet manually coded F0-F3.",
        "Original review text is encrypted, not publicly readable.",
        "API English labels can be inaccurate; human language validation pending.",
        "Some reviews are edited after creation, affecting period interpretations.",
        "Equal-sized period strata are not proportional to Steam review volume."
    ],
}
(out / "stratified_collection_manifest.json").write_text(
    json.dumps(manifest, indent=2) + "\n", "utf-8"
)
summary = [
    "# Verified full frames and stratified random sample", "",
    "Source: official Steam IUserReviewsService.GetAppReviews API.",
    "All five date windows were paginated until unique IDs equaled API total_matching.",
    "Review text and IDs are stored only in encrypted archives.", "",
    "| Period | API matching IDs | Validated rows | Nonblank rows | Primary | Reserve |",
    "|---|---:|---:|---:|---:|---:|",
]
for stat in statuses:
    label = stat["period"]
    counts = samples_per_period[label]
    summary.append("| {} | {} | {} | {} | {} | {} |".format(
        label, stat["seen_ids"], stat["validated_review_rows"],
        counts["full_frame_nonblank_count"], counts["primary_count"],
        counts["reserve_count"]))
summary += ["",
    "Total API IDs across windows: " + str(manifest["total_api_ids"]),
    "Main sample candidates: " + str(manifest["primary_candidate_n"]),
    "Reserve candidates: " + str(manifest["reserve_candidate_n"]), "",
    "This is a reproducible draw, **not** completed manual coding.",
    "The 200 initial candidates need text and language checks; replacement",
    "from the random reserve list must be recorded. Edited texts are flagged.",
    "Do not present cross-period patterns as causal effects of game updates.",
    "",
    "Public: [metadata](stratified_sample_features.csv), [full manifest](stratified_collection_manifest.json).",
    "Encrypted: [complete frames](../data_encrypted/steam_complete_frame_encrypted.json),",
    "[sample candidates](../data_encrypted/steam_stratified_sample_encrypted.json)."
]
(out / "stratified_collection_summary.md").write_text(
    "\n".join(summary) + "\n", "utf-8"
)
print("FULL COLLECTION SUCCESS: frames=", manifest["total_api_ids"],
      "sampled=", manifest["primary_candidate_n"],
      "reserves=", manifest["reserve_candidate_n"])
if manifest["primary_candidate_n"] < 200:
    print("WARNING: fewer than 200 sample candidates; revise claims accordingly.")
