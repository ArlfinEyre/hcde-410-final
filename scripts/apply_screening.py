#!/usr/bin/env python3
"""Rebuild the selected 200 private original-text reviews from the preserved 250.

Inputs: a locally decrypted candidates CSV and public GitHub screening files.
This script never pushes review text to GitHub or publishes reviewer IDs.
"""
import csv
from collections import Counter
from pathlib import Path

PRIVATE = Path("data_private")
DATA = Path("data")
source = PRIVATE / "steam_200_plus_reserves_private.csv"
list_file = DATA / "stratified_screened_200_ids.csv"
if not source.exists():
    raise SystemExit("Missing PRIVATE candidates CSV: decrypt steam_stratified_sample_encrypted.json first")
with source.open(newline="", encoding="utf-8") as stream:
    candidates = list(csv.DictReader(stream))
with list_file.open(newline="", encoding="utf-8") as stream:
    selected = list(csv.DictReader(stream))
by_id = {r["sample_id"]: r for r in candidates}
if len(by_id) != len(candidates):
    raise ValueError("Duplicate sample_id in candidates")
rows = []
for item in selected:
    sid = item["sample_id"]
    record = dict(by_id[sid])
    if record["period"] != item["period"]:
        raise ValueError("Period mismatch for " + sid)
    record["final_selection"] = (
        "reserve_replacement" if item["final_role"] == "reserve_replacement"
        else "initial_primary"
    )
    rows.append(record)
counts = Counter(r["period"] for r in rows)
if len(rows) != 200 or len(set(r["review_id"] for r in rows)) != 200:
    raise ValueError("Expected 200 unique reviews")
if len(counts) != 5 or any(n != 40 for n in counts.values()):
    raise ValueError("Expected 40 reviews in each of five periods")
if any(not r["review"].strip() for r in rows):
    raise ValueError("Unusable blank review in selected sample")

output = PRIVATE / "steam_screened_200_private.csv"
output.parent.mkdir(exist_ok=True)
with output.open("w", newline="", encoding="utf-8") as stream:
    writer = csv.DictWriter(stream, fieldnames=list(candidates[0]) + ["final_selection"])
    writer.writeheader()
    writer.writerows(rows)
output.chmod(0o600)
print("Verified 200 records (40 per period) available privately at", output)
print("This program has NOT performed human F0–F3 coding.")
