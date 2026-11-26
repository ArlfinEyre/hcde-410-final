# Initial quality screening of the 200 stratified sample candidates

**Date:** November 25, 2026 (Pacific). Based on original review text, not AI-paraphrased substitutes. The official Steam API English flag was checked for obvious exceptions. The [complete-frame manifest](stratified_collection_manifest.json) records **3,191 API records**, and the [candidate CSV](stratified_sample_features.csv) records **200 primary + 50 reserves**.

Four primary candidates were excluded in a focused text-quality check and replaced **sequentially by the first available random reserve within the same period**. The [screening log](stratified_screening_log.csv) records the exclusions and reasons; the [final list of selected sample IDs](stratified_screened_200_ids.csv) makes the 200-case selection auditable.

| Period | Final selected | Replacements |
|---|---:|---:|
| 2017 base game | 40 | 0 |
| 2018 Rise and Fall | 40 | 0 |
| 2019 Gathering Storm | 40 | 0 |
| 2020 New Frontier Pass | 40 | 1 |
| 2026 recent | 40 | 3 |
| **Total** | **200** | **4** |

The private 200-row CSV was constructed from the previously encrypted 250 candidate records; no reviewer SteamIDs or bulk verbatim text were placed into the public repository. The final 200 contain **46 records whose update timestamps follow the original review-creation timestamps**. These must be flagged for any historical-period comparisons.

**What this does and does not establish:** This is an initial targeted check for obvious non-substantive or non-English records. It is not a full double-blind validation of all 200 original texts, and it is **not completed qualitative F0–F3 coding**. During actual manual coding, any additional non-English or non-substantive records must be documented and replaced from the remaining unused reserves without choosing according to topic or sentiment. The sample is equally allocated across five periods; unweighted pooled rates should not be represented as the rate for all negative Steam reviews.

**Next:** read the full original 200 selected texts, assign F0–F3 and game-system labels following the [codebook](../CODEBOOK_PILOT.md), document disagreements and then conduct a delayed blind 15–20% code–recode check.

**Steam source:** https://partner.steamgames.com/doc/webapi/IUserReviewsService
