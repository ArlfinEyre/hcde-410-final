# Verified full frames and stratified random sample

Source: official Steam IUserReviewsService.GetAppReviews API.
All five date windows were paginated until unique IDs equaled API total_matching.
Review text and IDs are stored only in encrypted archives.

| Period | API matching IDs | Validated rows | Nonblank rows | Primary | Reserve |
|---|---:|---:|---:|---:|---:|
| base_2017 | 811 | 811 | 811 | 40 | 10 |
| rise_fall_2018 | 763 | 763 | 763 | 40 | 10 |
| gathering_2019 | 452 | 452 | 452 | 40 | 10 |
| frontier_2020 | 870 | 870 | 867 | 40 | 10 |
| recent_2026 | 295 | 295 | 292 | 40 | 10 |

Total API IDs across windows: 3191
Main sample candidates: 200
Reserve candidates: 50

This is a reproducible draw, **not** completed manual coding.
The 200 initial candidates need text and language checks; replacement
from the random reserve list must be recorded. Edited texts are flagged.
Do not present cross-period patterns as causal effects of game updates.

Public: [metadata](stratified_sample_features.csv), [full manifest](stratified_collection_manifest.json).
Encrypted: [complete frames](../data_encrypted/steam_complete_frame_encrypted.json),
[sample candidates](../data_encrypted/steam_stratified_sample_encrypted.json).
