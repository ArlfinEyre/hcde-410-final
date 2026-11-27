# Civilization VI Steam review codebook (A5 revision, Nov 16, 2026)

**Purpose:** Code what English-language negative Steam reviews *say*, not whether the reviewer is right, whether the recommendation is helpful, or whether an update caused the problem. This codebook responds to the A4 instructor feedback about concrete examples, specific game systems (especially AI opponents), multiple development periods, and code–recode consistency.

**Status (Nov 25):** A genuine 50-review **API** pilot has been retrieved, preserved as an encrypted original-text archive, and read for a **provisional AI-assisted first-pass coding**. [See first-pass annotations](data/pilot_50_manual_codes.csv) and [findings](data/pilot_50_coding_findings.md). Codes are provisional pending a delayed independent re-code. This remains a nonrandom first-page pilot; it is not the formal random sample. The older `pilot_20_annotated_summaries.csv` and `latest_page_10_paraphrased.csv` were convenience samples coded using an earlier, broader topic scheme. They are retained for transparency; **do not treat them as if they had been re-coded under the new topic labels**.

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

### Additional non-gameplay topics identified from the genuine-text Pilot (Nov 25)

- `visual_style` — critiques of visual style, art direction, models, or graphics aesthetic; **not** synonymous with poor interface legibility.
- `content_representation` — critiques of historical, cultural, political, or geographic naming and representation. Code the **reviewer's stated position** without endorsing or fact-checking their claim.

**Pilot exclusions:** A first-page review consisting essentially of copied ASCII meme art was marked `EXCLUDED` (no usable issue). Another review was predominantly Portuguese even though the API page labeled it English, so it was excluded from the English-only pilot. These rules should be checked for consistency in the formal sample.

**Important temporal limitation:** `timestamp_created` selects the review stratum, but the **current text can have been edited years later**. The pilot identified 13 of 50 reviews with updates after creation. Distinguish the author's review date from the age of the content when discussing historical changes.

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

1. **Pilot 40–50 reviews (completed first pass Nov 25):** Read 10 original API reviews per period, apply codes, document exclusions and borderline cases. See the encrypted source archive and first-pass public code table. Do not claim population representativeness.
2. **Formal sample:** Randomly draw up to 40 reviews **within each complete period frame** (target n=200). Track fewer-than-40 periods, exclusions, and coding decisions.
3. **Code–recode:** After a break, independently re-code around **15–20%** of the coded sample without looking at the first labels. Calculate agreement for F0–F3 and review where topic tags differ; document disagreements and any definitions revised.
4. **Report:** Count feedback levels and gameplay-system topics, separately summarize business/technical issues, and show differences across periods with per-period sample sizes and appropriate caution.

**Limitations:** A single-coder repeat is **within-coder consistency**, not agreement across coders. Reviews can be edited after creation. Review year is not proof of expansion ownership; differences across periods cannot establish the causal effect of patches. Steam reviewers are self-selected.

## E. Change log

- **Nov 15:** Initial broad F0–F3 and issue labels used for two small, non-random visible-page feasibility checks.
- **Nov 16:** Responded to instructor's A4 feedback: five development-period strata; finer game-system labels, especially AI vs balance; documented illustrative examples and repeat-coding procedure.
- **Nov 25:** Original-text API Pilot completed (10 records in each of 5 periods). Added two emergent topics, language/meme exclusions, edited-review caveat, and [first-pass coding](data/pilot_50_manual_codes.csv). Formal 200-review random sample and code–recode remain incomplete.

**Release/period references:** [2K Rise and Fall](https://newsroom.2k.com/news/sid-meiers-civilizationr-vi-rise-and-fall-available-now) · [2K Gathering Storm](https://newsroom.2k.com/news/sid-meiers-civilizationr-vi-gathering-storm-now-available) · [2K New Frontier Pass](https://newsroom.2k.com/news/sid-meiers-civilizationr-vi-new-frontier-pass-set-to-deliver-bimonthly-new-content-beginning-may-21-2020).

## F. Borderline-case audit (Nov 25, 2026)

All 11 cases marked `medium` in the initial genuine-text Pilot were revisited against their original text. The F0–F3 labels were retained; one secondary hardware/performance topic was added. Rationale is recorded in [the audit](data/pilot_borderline_audit.md), and the 50-row [adjudicated code table](data/pilot_50_adjudicated_codes.csv) preserves initial decisions and review notes.

**Do not report these 11 checks as blinded code–recode reliability.** The reviewer knew the initial labels; an independent, delayed 15–20% re-code of the *formal sample* remains necessary. Specific methodological cautions include historical review text edited after its publication year and an English API tag that does not guarantee the comment is actually English.

## G. Formal 200-case sampling milestone (Nov 25, 2026)

The revised complete-frame collector succeeded: **3,191** matching review IDs across the five periods, with count-verified full pagination. It drew 40 primary candidates and 10 reserves per period (total 200+50). Four obviously unsuitable primary texts were excluded on initial screening and replaced deterministically from the random reserves, leaving 200 unique original-text records: 40 in each period. See [sample selection log](data/stratified_screening_log.csv) and [final screened IDs](data/stratified_screened_200_ids.csv).

**Quality rule clarified:** A meaningful negative adjective such as 'trash' can be F0. A numeral-only response, punctuation-only response or an uninterpretable isolated word can be excluded as no substantive text. Steam English metadata is not sufficient to establish that a comment is in English. Human review of the rest of the 200 is still required.

**Chronology:** 46 of these 200 records were edited after the creation timestamp. This is not evidence that the edited words were originally present. Consider a sensitivity analysis excluding edited historical reviews.

**Coding status:** No full-sample F0–F3 labels have been finalized. The 50-review pilot first pass and borderline adjudication were assisted by ChatGPT; they do not constitute an independent blinded coding reliability check. Before final submission, the student should verify the classification and complete a delayed blind 15–20% code–recode check with disagreements logged.

## H. Stage 4 provisional coding and independent reviewer checkpoint (Nov 26, 2026)

The 200-case complete-frame random selection now has an **AI-assisted first-pass code table** rather than only unclassified sample IDs: [200 anonymized first-pass codes](data/ai_first_pass_200_codes.csv). See the [provisional methods report](data/Stage4_AI_First_Pass_Report.md). The coding was generated with ChatGPT assistance and has **not yet been independently verified by the student**.

**Additional screening:** A non-substantive hostile fragment (`CIV6_2026_035`) was excluded and replaced sequentially by the next unused pre-randomized reserve (`CIV6_2026_044`), keeping 40 cases in each of five periods. Cumulative Stage 3 + Stage 4 exclusions: five. See the [replacement log](data/stage4_additional_exclusion.csv).

**New topics identified during source review:**
- `game_map_generation` — map layout and spawning rules, terrain generation, world-builder functionality. Do not conflate with diplomatic borders.
- `game_religion` — specific complaints about religion and religious competition, separate from ordinary diplomatic contact.
- `multiplayer_online` — match stability, cross-platform multiplayer, desynchronization, leavers and online server problems. Technical crashes may co-occur with this label.

**Conservative first-pass coding rules:** Treat global insults, "not fun", "trash" and vague dislike as F0. A recognizable failure to launch is F1/technical even without diagnosis. Naming a missing feature without explicitly asking for a change is F1, not automatically F2. F3 requires an articulated remedy/option or policy design, not merely "fix it." Two categories can both apply when the text explicitly describes both (e.g., AI behavior and diplomacy).

**Human validation:** The researcher is asked to blindly recode 40 original reviews, eight per period, without seeing model labels. This is an **AI–human validation comparison**, not an independent human code–recode reliability study. Long, edited and borderline comments require further close reading and potential recoding before reporting final conclusions. `model_confidence` is an informal review-priority flag, **not** a calibrated probability.
