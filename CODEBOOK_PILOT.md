# Pilot coding guide — Civilization VI negative Steam reviews

This is a preliminary manual codebook, not an outcome of a representative study. It draws on two *separate* sets of public Steam Community listings (an older 20-review convenience pilot and a newer 10-review page check). The newer page displays day/month without year, so the date attribution needs confirmation from API metadata.

## Feedback level (one highest supported level per nonblank review)

- **F0 — General negative evaluation.** No specific identifiable game, product, or service problem.
- **F1 — Specific problem.** The review states an identifiable issue but **does not explicitly request a change**.
- **F2 — Explicit desired change.** The author directly asks for a feature, policy, behavior, or experience to change, without detailed implementation design.
- **F3 — Concrete proposed remedy.** The author suggests a specific method, implementation, or alternate policy, not merely a desired outcome.
- **EXCLUDED — Unreadable/blank.** Blank/whitespace-only text; retain exclusion counts in the flow diagram, not in the F0–F3 denominator.
- **UNCLEAR — Ambiguous.** Pause coding, document the ambiguity, and revisit later, rather than guess intention.

Examples of **illustrative phrases, not real quotations**:
- F0: "I dislike it."
- F1: "The UI text is too small."
- F2: "Please let us scale the UI."
- F3: "Add a UI scale slider with 100%–200% options."

Do not assume a critical review addresses developers; warning other consumers is not F2 unless there is an explicit requested product/policy change. More specificity is not the same as higher practical usefulness or technical feasibility.

## Issue topics (multi-label)

- `gameplay_rules` — mechanics, progression, unit movement, maps, difficulty structure.
- `ai_balance` — AI strategy, opponent strength, competitive balance.
- `ui_onboarding` — interface legibility, controller support, accessibility, tutorials.
- `technical_performance` — bugs, crashes, optimization, compatibility.
- `update_mods` — patches, mod compatibility, unannounced updates.
- `privacy_terms` — terms of service, privacy policies, consumer rights.
- `launcher` — publisher launcher, installation or launch workflow.
- `dlc_pricing` — bundles, purchase eligibility, DLC prices, commercial model.
- `general_comparison` — broad comparisons to other Civilization games without a clearer topic.
- `other` — other identifiable issues; note description.
- `no_identifiable_issue` — appropriate for F0 where no other topic is supported.

Sample data columns: sample ID, review-creation date (API if available), text (private only), F level, multi-label topics, notes, code confidence. Do not use the webpage's displayed playtime as historical `playtime_at_review`. Track the number of reviews excluded before reporting F0–F3 percentages.

## Analysis boundaries

- Random sampling only after retrieving and verifying the complete defined API frame or documenting the reachable frame.
- Never pool helpfulness-ranked and recent-page convenience samples and treat them as representative.
- Do a code–recode check on 15–20% of the main sample; acknowledge it is **intra-coder** consistency.
- Keep reviewer identities and bulk original review text out of the public GitHub repository.