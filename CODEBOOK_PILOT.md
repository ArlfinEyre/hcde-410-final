# Civilization VI Steam review codebook (A5 revision, Nov 16, 2026)

**Purpose:** Code what English-language negative Steam reviews *say*, not whether the reviewer is right, whether the recommendation is helpful, or whether an update caused the problem. This codebook responds to the A4 instructor feedback about concrete examples, specific game systems (especially AI opponents), multiple development periods, and code–recode consistency.

**Status:** Draft for testing on a 40–50-review **API** pilot across five time periods. The older `pilot_20_annotated_summaries.csv` and `latest_page_10_paraphrased.csv` were convenience samples coded using an earlier, broader topic scheme. They are retained for transparency; **do not treat them as if they had been re-coded under the new topic labels**.

## A. Feedback specificity — one highest supported code per review

| Code | Definition | Invented illustrative sentence (NOT an actual review quotation) |
| --- | --- | --- |
| **F0** | General negative judgment; no recognizable issue | "I really regret buying this." |
| **F1** | Identifies a specific issue but does not clearly ask for a change | "The AI sends units into losing battles." |
| **F2** | Explicitly requests a better outcome, feature, or policy, without an implementation plan | "The developers should improve the AI's tactical decisions." |
| **F3** | Suggests a particular remedy or implementation, beyond just the desired outcome | "Add an option for automated unit orders during late-game turns." |
| **UNCLEAR** | Text does not allow a reliable specificity judgment | Sarcasm or unclear references requiring discussion |
| **EXCLUDED** | Blank, unreadable, or no substantive review text | Empty field |

Rules:
- Assign the **highest level actually supported** by the review; do not infer requests from complaints.
- A detailed complaint without a proposed change is **F1**, not F2.
- "Fix the AI" is **F2**, not F3: it asks for improvement but does not describe how.
- A consumer warning ("Don't buy this") is not itself a product improvement request.
- F3 means a concrete suggestion, **not** that the proposed fix is feasible or valuable.
- Retain F0–F3 in the working table. For a simpler high-level chart: F0 = general dissatisfaction; F1 = specific problem; F2+F3 = improvement suggestions.
- Count exclusions separately. Note ambiguity rather than silently resolving it.

## B. Topics — multiple tags per review

For each code, tag a topic only when the review **explicitly mentions** the relevant issue. A review can receive more than one tag. Use the following two-level organization.

### B1. Game systems (these directly answer the professor's question)

| Tag | Include | Do not automatically include |
| --- | --- | --- |
| `game_ai_opponents` | AI decision-making, tactics, strategic behavior, predictable or incompetent computer opponents | Difficulty bonuses or balance alone |
| `game_balance` | Fairness of difficulty, bonuses, strength of civilizations/units, tuning | AI intelligence alone |
| `game_diplomacy` | Diplomatic rules, deals, alliances, grievances, World Congress | Any complaint simply mentioning another civilization |
| `game_combat_units` | Combat, unit pathfinding, movement, battle decisions, unit management | Technical crashes during a battle |
| `game_city_management` | Cities, districts, production, resources, governors, loyalty or city planning | General pacing without a city mechanic |
| `game_pacing_progression` | Turn length, late-game tedium, victory pacing, progression, repetitive turns | Slow frame rate or loading (technical) |
| `game_other` | Clearly specified game rule/system not covered above | Generic dislike without a specified mechanic |

**Overlap examples, invented:** "AI makes senseless diplomatic deals" can be `game_ai_opponents` **and** `game_diplomacy`. "The AI gets unfair bonuses" may be `game_balance` and `game_ai_opponents` if the review actually discusses both its decisions and the bonuses. A game can have difficult AI without the underlying system being well balanced.

### B2. Non-gameplay topics

| Tag | Include |
| --- | --- |
| `ui_onboarding` | Interface legibility, tooltips, tutorials, learning and accessibility |
| `technical_performance` | Crashes, bugs, FPS, loading, hardware compatibility |
| `update_mods` | Patches, update process, mod breakage |
| `privacy_terms` | EULA, privacy policy, consumer rights |
| `launcher` | Launcher account/sign-in/install/startup workflow |
| `dlc_pricing` | DLC costs, pricing, value of bundles, sales |
| `general_comparison` | Broad comparison to previous *Civilization* games without a more specific topic |
| `other` | Other explicit issue; write a short note |
| `no_identifiable_issue` | No identifiable topic (normally F0) |

For the report, keep **game system tags separate from non-gameplay tags**. Otherwise a surge in policy or launcher complaints could obscure which gameplay systems players discuss. Topic counts may exceed the number of reviews because multiple tags are allowed.

## C. Sampling periods and metadata

All periods are based on the *creation date* in UTC; the title describes the development context, not verified DLC ownership:

| Period label | Dates (UTC, inclusive) | Context | Target |
| --- | --- | --- | ---: |
| `base_2017` | 2017-03-01 to 2017-08-31 | Early base game | 40 |
| `rise_fall_2018` | 2018-03-01 to 2018-08-31 | After Rise and Fall release | 40 |
| `gathering_2019` | 2019-03-01 to 2019-08-31 | After Gathering Storm release | 40 |
| `frontier_2020` | 2020-06-01 to 2020-11-30 | During New Frontier Pass updates | 40 |
| `recent_2026` | 2026-05-01 to 2026-10-31 | Recent reviews | 40 |

Metadata to keep **privately**: unique review ID for de-duplication, review text, created/updated timestamps, period label, and playtime at review if provided. For the released analysis: period, anonymized sample ID, feedback code, topic tags, ambiguity note, and limited paraphrase where appropriate. Do not publish full review text or reviewer identifiers.

Use `Recent` with date filters and cursor pagination in the new [Steam IUserReviewsService](https://partner.steamgames.com/doc/webapi/IUserReviewsService); the legacy `/appreviews` endpoint has been deprecated. Apply consistent purchase, language, and off-topic settings. Check that each period's sampling frame was completely retrieved **before** taking a random sample. Equal sampling of periods is for **comparison**, not for estimating the total proportion of all reviews in each period.

## D. Coding process and consistency

1. **Pilot 40–50 reviews:** Inspect around 8–10 API reviews per period. Verify date fields, usable text, and edge cases. Revise this codebook and retain a dated change log.
2. **Formal sample:** Randomly draw up to 40 reviews **within each complete period frame** (target n=200). Track fewer-than-40 periods, exclusions, and coding decisions.
3. **Code–recode:** After a break, independently re-code around **15–20%** of the coded sample without looking at the first labels. Calculate agreement for F0–F3 and review where topic tags differ; document disagreements and any definitions revised.
4. **Report:** Count feedback levels and gameplay-system topics, separately summarize business/technical issues, and show differences across periods with per-period sample sizes and appropriate caution.

**Limitations:** A single-coder repeat is **within-coder consistency**, not agreement across coders. Reviews can be edited after creation. Review year is not proof of expansion ownership; differences across periods cannot establish the causal effect of patches. Steam reviewers are self-selected.

## E. Change log

- **Nov 15:** Initial broad F0–F3 and issue labels used for two small, non-random visible-page feasibility checks.
- **Nov 16:** Responded to instructor's A4 feedback: five development-period strata; finer game-system labels, especially AI vs balance; documented illustrative examples and repeat-coding procedure. Formal API pilot and main sample remain uncollected.

**Release/period references:** [2K Rise and Fall](https://newsroom.2k.com/news/sid-meiers-civilizationr-vi-rise-and-fall-available-now) · [2K Gathering Storm](https://newsroom.2k.com/news/sid-meiers-civilizationr-vi-gathering-storm-now-available) · [2K New Frontier Pass](https://newsroom.2k.com/news/sid-meiers-civilizationr-vi-new-frontier-pass-set-to-deliver-bimonthly-new-content-beginning-may-21-2020).
