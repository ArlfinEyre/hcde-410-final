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
