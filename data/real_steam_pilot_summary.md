# Genuine Steam review API pilot

**Collection date (UTC):** 2026-11-25T21:25:32.611811+00:00
**Records derived from ORIGINAL Steam reviews:** 50

The collector fetched actual review text. Original text stays in the
gitignored data_private/ directory on the runner and is **not** pushed
to this public repository. To see original text, run the A5 notebook
collector in Google Colab or on your own computer.

## Reviews by period (exploratory)

| Period | Review count |
|---|---:|
| base_2017 | 10 |
| rise_fall_2018 | 10 |
| gathering_2019 | 10 |
| frontier_2020 | 10 |
| recent_2026 | 10 |

## Literal keyword indicators (NOT manually validated topics)

| Keyword flag | Review count |
|---|---:|
| kw_ai | 4 |
| kw_balance | 0 |
| kw_diplomacy | 1 |
| kw_combat | 3 |
| kw_city | 8 |
| kw_pacing | 5 |
| kw_ui | 2 |
| kw_performance | 5 |
| kw_terms | 0 |
| kw_pricing | 9 |
| kw_launcher | 0 |

**Limits:** The sample is nonrandom. Keyword counts can have false
positives/negatives; multiple flags can occur per review. These are
NOT findings about the prevalence of actual complaints among all reviews,
and they are NOT the formal 200-review stratified dataset.

See [the collection script](../scripts/collect_real_pilot.py) for provenance.
