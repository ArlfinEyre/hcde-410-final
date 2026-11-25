# HCDE 410 Final Project — A4 + A5

**Project:** *Beyond Thumbs Down: Negative Steam Reviews, Game Systems, and Change Over Time*

This repository contains the A4 preliminary proposal extended into the A5 final study plan. The revised design responds to instructor feedback by sampling negative reviews of *Sid Meier's Civilization VI* **across five game-development periods**, examining **which game systems reviewers criticize**, and comparing how specifically they describe problems or propose changes.

**[Read the A4 + A5 research notebook](HCDE410_A4_Proposal.ipynb)** · **[Read the updated pilot codebook](CODEBOOK_PILOT.md)**

**Study design:** English-language negative reviews; target 40 coded reviews in each of five periods (2017, 2018, 2019, 2020, 2026), for a total target of 200. The codebook covers feedback specificity (F0–F3), specific game systems including AI opponents, balance, diplomacy, combat, cities, and pacing, and separate non-gameplay complaints. The plan includes a 40–50-review API pilot and within-coder repeat coding of 15–20% of the sample.

**Current evidence and limitations:** The exploratory 20-review and 10-review visible-page checks are **nonrandom convenience samples**, using an earlier topic scheme. Their underlying paraphrased records and exploratory notebooks remain in the repository for transparency; they do **not** establish population frequencies or validate the new period strata. The official API-based stratified sample and code–recode check **have not yet been completed**. Older comments may have been edited and an author's expansion ownership cannot be inferred from review dates.

**Resources:**
- [Official Steam User Reviews API](https://partner.steamgames.com/doc/webapi/IUserReviewsService) (replaces legacy /appreviews endpoint)
- [Steam API Terms](https://steamcommunity.com/dev/apiterms)
- [Civilization VI](https://store.steampowered.com/app/289070/)
- [Pilot codebook and categories](CODEBOOK_PILOT.md)
- [Exploratory review analysis](real_review_pilot.ipynb)
- [Supplementary visible-page check](additional_recent_pilot.ipynb)

Review IDs and bulk raw review text stay private and are not intended for public GitHub. The repository's MIT license applies to the project's original code and documentation, not Steam data or reviewers' comments.

## Current research status (verified Nov 25, 2026)

- **API Pilot complete:** 50 genuine negative reviews across 5 periods, 10 per period. [Verified collection run](https://github.com/ArlfinEyre/hcde-410-final/actions/runs/45704323963).
- **Verbatim review text retained encrypted**, with public key in the repo but the private key kept separately: [encrypted source archive](data_encrypted/steam_pilot_original_encrypted.json).
- **First-pass manual coding completed:** [50 annotated records](data/pilot_50_manual_codes.csv), with [methodology and provisional findings](data/pilot_50_coding_findings.md). Valid coded reviews: 48; two excluded.
- **Still pending:** independent code–recode check, complete stratified sample of 200, and final report. The 50-review Pilot is nonrandom and not representative.

## Verified live Steam API pilot — Nov 25, 2026

**Successful run:** [GitHub Actions #2](https://github.com/ArlfinEyre/hcde-410-final/actions/runs/45701139671) retrieved **50 original Steam negative reviews**, 10 from each of five selected date periods. The first-page pilot was **not random** and must not be used for population estimates.

The following **real-data-derived** files are now committed:
- [Pilot review metadata and literal keyword indicators](data/real_steam_pilot_features.csv) — 50 records; no raw review text
- [Collection provenance and sampling status](data/real_steam_pilot_status.json)
- [Pilot exploratory summary](data/real_steam_pilot_summary.md)

**Raw text availability:** The original `review` text was accessed in GitHub Actions and preserved as an **encrypted archive**. The private decryption key is stored separately outside GitHub. To generate further original review data, execute [the script](scripts/collect_real_pilot.py) in your own computer or Google Colab and save the generated `data_private/pilot_reviews_private.csv` privately. Do not push that file to this public repo.

**Remaining work:** complete five date-window sampling frames and draw about 40 reviews from each; carry out independent code–recode consistency checking and final analysis. The original-text pilot has already been manually coded once.

## Original Steam review data (not AI paraphrases)

The previous `pilot_20_annotated_summaries.csv` and `latest_page_10_paraphrased.csv` are **exploratory paraphrases**, not raw original review text.

A [live original-review collector](scripts/collect_real_pilot.py) and a [GitHub Actions job](.github/workflows/steam-real-pilot.yml) now attempt a 10-review-per-period pilot using Steam's current official `IUserReviewsService/GetAppReviews` endpoint. **The live first-pass coding and encrypted archival are documented above.** Check the [Actions page](../../actions/workflows/steam-real-pilot.yml) for further runs.

When successful, it creates `data/real_steam_pilot_features.csv` (anonymized metadata and literal word indicators), `data/real_steam_pilot_status.json` (provenance), and `data/real_steam_pilot_summary.md`. The raw original `review` text is collected **privately** in `data_private/pilot_reviews_private.csv`, ignored by Git. GitHub Actions runners are temporary; to retain and read originals, run `python scripts/collect_real_pilot.py` in your own local/Colab environment after installing `pandas` and `requests`, then keep `data_private/` private. No one should confuse automated keyword matches with the manual F0–F3 coding or interpret a first-page pilot as a random sample.
