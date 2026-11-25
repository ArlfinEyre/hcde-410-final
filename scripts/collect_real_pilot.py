#!/usr/bin/env python3
"""Fetch ORIGINAL Steam review text through the existing A5 notebook collector.

Raw texts remain ONLY in data_private/ (gitignored). Public CSV contains
nonidentifying metadata and literal keyword flags calculated from originals.
Keyword flags are NOT manual F0-F3 codes, and the pilot is NOT random.
"""
import csv
import json
import re
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone

NB = Path("HCDE410_A4_Proposal.ipynb")
notebook = json.loads(NB.read_text(encoding="utf-8"))
cell = next(
    c for c in notebook["cells"]
    if c["cell_type"] == "code"
    and "def fetch_period(" in "".join(c["source"])
)
src = "".join(cell["source"])
if "RUN_LIVE_PILOT = False" not in src:
    raise RuntimeError("Expected the A5 collector with live pilot disabled.")
src = src.replace("RUN_LIVE_PILOT = False", "RUN_LIVE_PILOT = True")
scope = {}
exec(compile(src, str(NB) + ":collector", "exec"), scope)
pilot = scope.get("pilot")
if pilot is None or len(pilot) == 0:
    raise RuntimeError("No genuine Steam reviews were retrieved. Nothing will be published.")

patterns = {
    "kw_ai": r"\b(?:ai|artificial intelligence|computer opponent|computer player)\b",
    "kw_balance": r"\b(?:balance|balanced|balancing|unfair|overpowered|difficulty)\b",
    "kw_diplomacy": r"\b(?:diplomacy|diplomatic|world congress|alliance|grievance)\b",
    "kw_combat": r"\b(?:combat|battle|military|pathfinding|unit|units)\b",
    "kw_city": r"\b(?:city|cities|district|governor|production)\b",
    "kw_pacing": r"\b(?:turn|turns|late.game|slow|grind|pacing)\b",
    "kw_ui": r"\b(?:ui|interface|tutorial|tooltip|accessibility)\b",
    "kw_performance": r"\b(?:bug|bugs|crash|performance|fps|freeze|lag)\b",
    "kw_terms": r"\b(?:eula|privacy|data collection|terms of service)\b",
    "kw_pricing": r"\b(?:dlc|expansion|pricing|expensive|cash.grab)\b",
    "kw_launcher": r"\b(?:launcher|sign.in)\b",
}
regex = {k: re.compile(v, re.I) for k, v in patterns.items()}
out = Path("data")
out.mkdir(exist_ok=True)
rows = []
for i, r in enumerate(pilot.to_dict(orient="records"), 1):
    txt = str(r.get("review") or "")
    row = {
        "sample_id": f"steam_pilot_{i:03d}",
        "period": r.get("period", ""),
        "created_utc": r.get("created_utc", ""),
        "edited_since_creation": str(r.get("updated_utc", "")) != str(r.get("created_utc", "")),
        "playtime_at_review_hours": r.get("playtime_at_review_hours", ""),
        "review_length_chars": len(txt),
        "review_word_count": len(txt.split()),
    }
    row.update({k: int(bool(rx.search(txt))) for k, rx in regex.items()})
    rows.append(row)

filename = out / "real_steam_pilot_features.csv"
with filename.open("w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0]))
    writer.writeheader()
    writer.writerows(rows)

counts = Counter(str(r["period"]) for r in rows)
topic_counts = {k: sum(int(row[k]) for row in rows) for k in patterns}
now = datetime.now(timezone.utc).isoformat()
status = {
    "source": "Steam official IUserReviewsService/GetAppReviews/v1/",
    "appid": 289070,
    "collected_at_utc": now,
    "original_text_local_only": "data_private/pilot_reviews_private.csv",
    "public_csv": str(filename),
    "review_rows": len(rows),
    "period_counts": dict(counts),
    "keyword_counts": topic_counts,
    "sampling": "First page of 10 recent negative English reviews in each period; non-random exploratory pilot",
    "coding": "Keyword flags are exploratory text features, NOT human F0-F3 coding",
}
(out / "real_steam_pilot_status.json").write_text(
    json.dumps(status, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
)
lines = [
    "# Genuine Steam review API pilot", "",
    f"**Collection date (UTC):** {now}",
    f"**Records derived from ORIGINAL Steam reviews:** {len(rows)}", "",
    "The collector fetched actual review text. Original text stays in the",
    "gitignored data_private/ directory on the runner and is **not** pushed",
    "to this public repository. To see original text, run the A5 notebook",
    "collector in Google Colab or on your own computer.", "",
    "## Reviews by period (exploratory)", "",
    "| Period | Review count |", "|---|---:|"
]
for period, count in counts.items():
    lines.append(f"| {period} | {count} |")
lines += [
    "", "## Literal keyword indicators (NOT manually validated topics)", "",
    "| Keyword flag | Review count |", "|---|---:|"
]
for label, count in topic_counts.items():
    lines.append(f"| {label} | {count} |")
lines += [
    "", "**Limits:** The sample is nonrandom. Keyword counts can have false",
    "positives/negatives; multiple flags can occur per review. These are",
    "NOT findings about the prevalence of actual complaints among all reviews,",
    "and they are NOT the formal 200-review stratified dataset.", "",
    "See [the collection script](../scripts/collect_real_pilot.py) for provenance."
]
(out / "real_steam_pilot_summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("SUCCESS: genuine API review rows:", len(rows))
print("Derived public dataset:", filename)
