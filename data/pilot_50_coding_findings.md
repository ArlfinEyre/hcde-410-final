# Genuine-text pilot: first-pass qualitative coding (25 Nov 2026)

The 50 records in [real_steam_pilot_features.csv](real_steam_pilot_features.csv) were obtained through the official Steam API and their **original full text was read** for this exploratory coding pass. [First-pass annotated table](pilot_50_manual_codes.csv) contains only anonymized codes and brief paraphrased notes, **not copied original reviews**. Decrypted originals are deliberately private; the encrypted archive is preserved separately.

## Coding results (descriptive pilot only)

| Feedback level | Count |
|---|---:|
| F0 – general dissatisfaction | 9 |
| F1 – identifies a specific problem | 31 |
| F2 – requests an improvement/outcome | 7 |
| F3 – offers concrete remedy | 1 |
| EXCLUDED (meme or wrong language) | 2 |
| **Total** | **50** |

Valid coded reviews: **48**. This is the **first 10 API-recent comments from each period**, so these fractions are NOT population estimates.

## Reviewed topics

| Topic | Coded reviews mentioning it |
|---|---:|
| `technical_performance` | 15 |
| `game_other` | 9 |
| `dlc_pricing` | 9 |
| `game_city_management` | 6 |
| `game_ai_opponents` | 5 |
| `game_pacing_progression` | 5 |
| `game_diplomacy` | 4 |
| `ui_onboarding` | 4 |
| `visual_style` | 3 |
| `privacy_terms` | 2 |
| `game_combat_units` | 2 |
| `content_representation` | 2 |
| `update_mods` | 2 |
| `game_balance` | 1 |
| `launcher` | 1 |

Topic labels are **not exclusive**, so columns can total more than 48. Compared with raw keyword matching, manual reading separates AI behavior from balancing, and distinguishes ordinary technical crashes from complaints about updates, pricing, UI and game design.

## Codebook changes prompted by actual reviews

1. Add `content_representation`: criticisms of historical/cultural/geopolitical representation. Coding a claim does not endorse or validate that claim.
2. Add `visual_style`: criticisms of art direction, visual presentation, or graphics aesthetic distinct from interface usability.
3. Explicitly exclude non-substantive ASCII-art/meme reviews and predominantly non-English reviews mistakenly labeled English by Steam.
4. **Chronology limitation:** some early-dated reviews have been edited substantially years later, so their current text may describe events outside their creation-period stratum.
5. A comparative list of absent features is **not automatically an explicit improvement request**. Only F2 when a request is actually made; F3 only when a concrete remedy is proposed.
6. Consider whether `game_other` is too broad after examining a larger, truly random sample.

## Uncertain / borderline coding

- `steam_pilot_003`
- `steam_pilot_008`
- `steam_pilot_011`
- `steam_pilot_015`
- `steam_pilot_021`
- `steam_pilot_023`
- `steam_pilot_024`
- `steam_pilot_025`
- `steam_pilot_029`
- `steam_pilot_032`
- `steam_pilot_042`

These 11 comments need careful second review. **No delayed independent re-code has yet been done.** Agreement figures should be calculated later on a fresh 15–20% subset without viewing the first codes.

## Sampling implications

This pilot proves the API and original review text are usable. It does **not** validate the period-stratified 200-review estimates: each period's full review frame must be paginated to completion before random sampling, not simply take the first ten. If meaningful across-period comparison is the goal, historical reviews edited after their period should be flagged and a sensitivity analysis considered.

Data privacy: the public project publishes coding decisions, methodological notes and aggregate statistics, never bulk verbatim review text or reviewer SteamIDs.
