# HCDE 410 Final Project — A4 + A5

**Project:** *Beyond Thumbs Down: Negative Steam Reviews, Game Systems, and Change Over Time*

This repository contains the A4 preliminary proposal extended into the A5 final study plan. The revised design responds to instructor feedback by sampling negative reviews of *Sid Meier's Civilization VI* **across five game-development periods**, examining **which game systems reviewers criticize**, and comparing how specifically they describe problems or propose changes.

**[Read the A4 + A5 research notebook](HCDE410_A4_Proposal.ipynb)** · **[Read the updated pilot codebook](CODEBOOK_PILOT.md)**

**Study design:** English-language negative reviews; target 40 coded reviews in each of five periods (2017, 2018, 2019, 2020, 2026), for a total target of 200. The codebook covers feedback specificity (F0–F3), specific game systems including AI opponents, balance, diplomacy, combat, cities, and pacing, and separate non-gameplay complaints. The plan includes a 40–50-review API pilot and within-coder repeat coding of 15–20% of the sample.

**Current evidence and limitations:** The exploratory 20-review and 10-review visible-page checks are **nonrandom convenience samples**, using an earlier topic scheme. Their underlying paraphrased records and exploratory notebooks remain in the repository for transparency; they do **not** establish population frequencies or validate the new period strata. The formal period-stratified **sampling is now complete**, but the 200-case content coding and code–recode check **have not yet been completed**. Older comments may have been edited and an author's expansion ownership cannot be inferred from review dates.

**Resources:**
- [Official Steam User Reviews API](https://partner.steamgames.com/doc/webapi/IUserReviewsService) (replaces legacy /appreviews endpoint)
- [Steam API Terms](https://steamcommunity.com/dev/apiterms)
- [Civilization VI](https://store.steampowered.com/app/289070/)
- [Pilot codebook and categories](CODEBOOK_PILOT.md)
- [Exploratory review analysis](real_review_pilot.ipynb)
- [Supplementary visible-page check](additional_recent_pilot.ipynb)

Review IDs and bulk raw review text stay private and are not intended for public GitHub. The repository's MIT license applies to the project's original code and documentation, not Steam data or reviewers' comments.

## Stage 4 — First-pass coding of 200 original reviews (Nov 26, 2026)

**Status:** A **provisional AI-assisted content-coding pass** has been prepared for the 200 verified Steam review texts. This is **NOT human-confirmed analysis or a reliability result**. [Stage 4 methods and findings](data/Stage4_AI_First_Pass_Report.md) · [Anonymous 200-case codes](data/ai_first_pass_200_codes.csv) · [Runnable charts](analysis/Stage4_Descriptive_Charts.ipynb).

Initial labels: **F0=36, F1=130, F2=29, F3=5**. These descriptive counts belong to the *model's* first pass; they should not be presented as final proportions in an academic report without review. The most frequently flagged named gameplay system is AI opponents (35/200); separately, technical/performance issues (45) and DLC/pricing (43) are common. Multiple topic labels may appear per review.

**Selection correction:** A further non-substantive review (`CIV6_2026_035`) was removed and replaced with the next unused random reserve (`CIV6_2026_044`), yielding **five cumulative screened replacements**, documented in [Stage 4 amendment](data/stage4_additional_exclusion.csv) and the [updated anonymous selection list](data/final_selection_200_ids.csv). All five periods still have 40 selected comments.

**Required next step:** The user/researcher must independently review an original-text **40-item blinded worksheet (20% stratified audit)**, shared privately outside GitHub. No raw Steam review text or reviewer IDs are included in this public repository. Comparison and reconciliation are **pending**, as is a separate within-coder reliability claim (not established by comparing a human with an AI).

## Current status — complete five-period frames and screened 200 candidates (Nov 25, 2026)

- **Complete retrieval:** [manifest](data/stratified_collection_manifest.json) confirms **3,191 unique matching Steam API reviews** across five windows (2017: 811; 2018: 763; 2019: 452; 2020: 870; 2026: 295), with every window paginated until the retrieved-ID count matched the API total.
- **Seeded draws:** [candidate metadata](data/stratified_sample_features.csv) contains **200 initial random primary candidates and 50 random reserves**, 40+10 per period. Original text and review IDs are preserved in the [encrypted frame archive](data_encrypted/steam_complete_frame_encrypted.json) and [encrypted sample archive](data_encrypted/steam_stratified_sample_encrypted.json); the private key is **not** in this public repository.
- **Initial content checks:** four obvious unsuitable primary candidates were replaced in random-reserve order. The [screening log](data/stratified_screening_log.csv), [screened set of 200 anonymous sample IDs](data/stratified_screened_200_ids.csv), and [screening methodology](data/stratified_screening_summary.md) document the changes. The selected 200 contain **46 reviews edited after their creation timestamp**.
- **Rebuild privately:** decrypt the sample archive with the separately held key, then run [scripts/apply_screening.py](scripts/apply_screening.py). This recreates the **200 original-text rows** locally without making review text public.
- **Not yet completed:** the **200-case F0–F3 and game-system coding**, comprehensive language/text validation, a delayed blinded code–recode check, results charts, and final report. The earlier 50-review coding is **AI-assisted provisional interpretation**, not independent human-only coding or an inter-coder reliability result.

**[Verified full collection run](https://github.com/ArlfinEyre/hcde-410-final/actions/runs/45743547456)** · [Full-period collection script](scripts/collect_stratified_200.py)

## Current research status (verified Nov 25, 2026)

- **API Pilot complete:** 50 genuine negative reviews across 5 periods, 10 per period. [Verified collection run](https://github.com/ArlfinEyre/hcde-410-final/actions/runs/45704323963).
- **Verbatim review text retained encrypted**, with public key in the repo but the private key kept separately: [encrypted source archive](data_encrypted/steam_pilot_original_encrypted.json).
- **AI-assisted first-pass coding completed (requires independent review):** [50 annotated records](data/pilot_50_manual_codes.csv), with [methodology and provisional findings](data/pilot_50_coding_findings.md). Valid coded reviews: 48; two excluded.
- **Still pending:** independent code–recode check, formal 200-review content coding, and final report. The 50-review Pilot is nonrandom and not representative.

## Verified live Steam API pilot — Nov 25, 2026

**Successful run:** [GitHub Actions #2](https://github.com/ArlfinEyre/hcde-410-final/actions/runs/45701139671) retrieved **50 original Steam negative reviews**, 10 from each of five selected date periods. The first-page pilot was **not random** and must not be used for population estimates.

The following **real-data-derived** files are now committed:
- [Pilot review metadata and literal keyword indicators](data/real_steam_pilot_features.csv) — 50 records; no raw review text
- [Collection provenance and sampling status](data/real_steam_pilot_status.json)
- [Pilot exploratory summary](data/real_steam_pilot_summary.md)

**Raw text availability:** The original `review` text was accessed in GitHub Actions and preserved as an **encrypted archive**. The private decryption key is stored separately outside GitHub. To generate further original review data, execute [the script](scripts/collect_real_pilot.py) in your own computer or Google Colab and save the generated `data_private/pilot_reviews_private.csv` privately. Do not push that file to this public repo.

**Remaining work:** validate the selected 200 original texts, conduct transparent F0–F3/game-system coding, carry out delayed independent code–recode consistency checking and final analysis. The original-text pilot has already received one AI-assisted coding pass.

## Original Steam review data (not AI paraphrases)

The previous `pilot_20_annotated_summaries.csv` and `latest_page_10_paraphrased.csv` are **exploratory paraphrases**, not raw original review text.

A [live original-review collector](scripts/collect_real_pilot.py) and a [GitHub Actions job](.github/workflows/steam-real-pilot.yml) now attempt a 10-review-per-period pilot using Steam's current official `IUserReviewsService/GetAppReviews` endpoint. **The live first-pass coding and encrypted archival are documented above.** Check the [Actions page](../../actions/workflows/steam-real-pilot.yml) for further runs.

When successful, it creates `data/real_steam_pilot_features.csv` (anonymized metadata and literal word indicators), `data/real_steam_pilot_status.json` (provenance), and `data/real_steam_pilot_summary.md`. The raw original `review` text is collected **privately** in `data_private/pilot_reviews_private.csv`, ignored by Git. GitHub Actions runners are temporary; to retain and read originals, run `python scripts/collect_real_pilot.py` in your own local/Colab environment after installing `pandas` and `requests`, then keep `data_private/` private. No one should confuse automated keyword matches with the manual F0–F3 coding or interpret a first-page pilot as a random sample.
