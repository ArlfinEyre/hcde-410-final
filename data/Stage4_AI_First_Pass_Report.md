# Stage 4 — AI-assisted qualitative coding: provisional results

**Project:** *Beyond Thumbs Down: Negative Steam Reviews, Game Systems, and Change Over Time*  
**Status:** First-pass interpretation complete; **not** human-verified qualitative results.  
**Source:** Steam `IUserReviewsService/GetAppReviews`, App ID 289070. Five date windows, 40 selected negative reviews per period.

## 1. Data and quality control

- The full sampling frame consisted of **3,191** English-labeled Steam negative reviews retrieved from five fully paginated windows. A seeded selection produced 200 primary candidates and 50 reserves.
- At Stage 3, four unusable primary candidates were replaced in predefined reserve order. At Stage 4, another incoherent hostile fragment (`CIV6_2026_035`) was excluded and replaced by the next eligible 2026 reserve (`CIV6_2026_044`). **Five replacements total** are documented in the Stage 3 and Stage 4 logs.
- The analyzed **200** unique originals remain equally allocated: 40 from each period. **46** comments were edited after creation; their current wording must not be treated as necessarily written during their creation year.
- Raw text and review identifiers are stored in private/encrypted source files. Public review-level output contains only pseudonymous sample ID, period, model code, a brief paraphrased rationale and derived metadata.

## 2. First-pass feedback specificity

The following are **AI-assisted provisional labels**, not manually validated researcher ground truth. All percentages use the fixed sample denominator of 200 and are *not* Steam-wide population estimates.

| Highest level | Count | Percentage | Meaning |
| --- | ---: | ---: | --- |
| F0 | 36 | 18.0% | General dissatisfaction without identifiable issue |
| F1 | 130 | 65.0% | Identifiable problem without explicit requested change |
| F2 | 29 | 14.5% | Explicitly requested improvement or change |
| F3 | 5 | 2.5% | Proposed specific remedy or implementation |
| **Total** | **200** | **100.0%** | |

Taken together, **34/200 (17.0%)** were provisionally identified as containing an explicit improvement request or remedy (F2/F3), and **164/200 (82.0%)** as F1–F3. These are *properties of these draft AI codes*, not conclusions about the broader population.

## 3. Issue types

Topics were **multi-label**: one review can mention more than one issue. Counts and percentages across categories therefore **must not be added together**.

| Provisional topic | Reviews | Share of this 200-case sample |
| --- | ---: | ---: |
| `technical_performance` | 45 | 22.5% |
| `dlc_pricing` | 43 | 21.5% |
| `game_other` | 42 | 21.0% |
| `game_ai_opponents` | 35 | 17.5% |
| `game_pacing_progression` | 27 | 13.5% |
| `ui_onboarding` | 24 | 12.0% |
| `game_balance` | 23 | 11.5% |
| `game_city_management` | 22 | 11.0% |
| `privacy_terms` | 22 | 11.0% |
| `no_identifiable_issue` | 20 | 10.0% |
| `game_diplomacy` | 18 | 9.0% |
| `visual_style` | 17 | 8.5% |
| `general_comparison` | 16 | 8.0% |
| `game_combat_units` | 14 | 7.0% |
| `update_mods` | 9 | 4.5% |
| `multiplayer_online` | 7 | 3.5% |
| `game_map_generation` | 6 | 3.0% |
| `other` | 6 | 3.0% |
| `game_religion` | 3 | 1.5% |
| `launcher` | 2 | 1.0% |
| `content_representation` | 1 | 0.5% |

Among the **named game systems**, AI opponent behavior appears often (**35** coded reviews), ahead of pacing/progression (**27**), balance (**23**) and cities/districts (**22**). The broad `game_other` label (**42**) is heterogeneous and should **not** be interpreted as a single identifiable game system. Across all themes, non-gameplay technical/performance issues (**45**) and DLC/pricing (**43**) were also prominent. These comparisons require checking the corresponding original reviews before reporting as findings.

## 4. Difference across selected review periods

| Period | F0 | F1 | F2 | F3 | n |
| --- | ---: | ---: | ---: | ---: | ---: |
| `base_2017` | 5 | 22 | 10 | 3 | 40 |
| `rise_fall_2018` | 5 | 26 | 9 | 0 | 40 |
| `gathering_2019` | 6 | 28 | 4 | 2 | 40 |
| `frontier_2020` | 8 | 26 | 6 | 0 | 40 |
| `recent_2026` | 12 | 28 | 0 | 0 | 40 |

These equal-size strata are intended to enable **comparisons within the selected windows**, not represent the distribution of *all* Civ VI reviews. Reviewers differ across periods, Steam's API can exclude off-topic activity, and game expansions/updates do not prove that a reviewer owned the relevant DLC. The original text may have been edited after publication; 46 of the sampled texts have such an edit flag. No causal relationship between an update and a complaint is claimed.

**Exploratory pattern that must be checked:** provisional AI coding identified more privacy-focused comments in 2018 and technical problems in 2020/2026. Do not interpret this as Steam-wide prevalence or change across time until the label audit and edited-review sensitivity check are complete.

## 5. Human validation / code–recode

The private blind-review workbook (shared separately and **not uploaded to public GitHub**) contains **40 actual review texts, eight independently selected from each period**, with **no AI codes shown**. This corresponds to **20%** of the 200-case sample. The selection seed is 419410, stored in the [coding manifest](AI_first_pass_manifest.json).

The researcher should independently read and enter F0/F1/F2/F3 plus issue tags **without** consulting the model's answers, document ambiguous cases, and return the workbook for a code-agreement comparison and reconciliation. This is a *human audit of model predictions*, not an intra-coder test on independent human coding unless the original and repeat codings were both by the researcher.

Additional review priority was given to long, edited, and F2/F3 cases; **98** AI-labeled records are flagged for follow-up review, so the blind sample alone may not cover all questionable classifications. A subsequent targeted audit and documented decisions are needed before releasing final percentages.

## 6. Disclosures and limitations

- The coding was prepared with ChatGPT from original, privately stored Steam review text and targeted excerpts. Some long reviews require full human review; model judgment should not be presented as independently executed manual content analysis.
- `model_confidence` is a *subjective review-priority indicator*, not a calibrated statistical probability.
- Original review text is intentionally not committed publicly. Private research copies should remain outside GitHub.
- No statistical significance testing or model-independent reliability coefficient is claimed at this stage.

## Public supporting files

- [AI first-pass 200 codes](ai_first_pass_200_codes.csv)
- [Feedback-level counts by period](feedback_by_period_AI_first_pass.csv)
- [Topic counts by period](topic_by_period_AI_first_pass.csv)
- [Selection IDs after the fifth exclusion](final_selection_200_ids.csv)
- [Stage 4 exclusion and replacement log](additional_exclusion_log.csv)
- [Source/coding manifest](AI_first_pass_manifest.json)

**Next step:** Independent, blinded human review and reconciliation of 40 cases; then update results and visuals. Do not call this first-pass output the final submitted analysis yet.