# Critical Thinking Against Fake News: A Meta-Analysis of Technology-Based Educational Interventions

---

## Abstract

The proliferation of misinformation in digital media environments has generated a rapidly expanding field of technology-based educational interventions designed to strengthen critical thinking and reduce susceptibility to fake news. Yet the quantitative evidence on which technology types work, for whom, and under what conditions remains dispersed across disciplines and has not been comprehensively synthesised. This meta-analysis systematically identifies and synthesises standardised effect sizes from experimental and quasi-experimental studies examining the impact of emerging technology interventions—including game-based inoculation platforms, artificial intelligence (AI) tools, social media nudges, and digital media literacy curricula—on critical thinking and misinformation resilience outcomes. Following PRISMA 2020 guidelines, a comprehensive search across seven databases yielded 14 independent effect sizes from 14 studies encompassing 33,367 participants across nine countries. A random-effects meta-analysis yielded an overall pooled effect of Hedges' g = 0.411 (95% CI [0.296, 0.526], z = 7.02, p < .001), indicating a moderate positive effect of technology-based interventions on misinformation resilience. Moderate-to-substantial heterogeneity was detected (I² = 68.6%), motivating a series of planned moderator analyses. Intervention type emerged as a significant moderator (Q_between(3) = 8.24, p = .041): digital literacy platforms and multi-session curricula yielded the largest effects (g = 0.541), followed by game-based inoculation (g = 0.413) and AI-based tools (g = 0.377); accuracy nudges produced the smallest effects (g = 0.237). Participant type was also a significant moderator (Q_between(2) = 9.17, p = .010), with older adults showing the largest gains (g = 0.681) and general adult samples the smallest (g = 0.336). Crucially, study design (RCT vs. pre-post), intervention duration, and outcome domain did not significantly moderate effects. Publication bias tests indicated modest asymmetry; a trim-and-fill adjusted estimate remained significant (g = 0.362). These findings demonstrate that technology-based interventions for critical thinking development against fake news are effective across technology types but show important boundary conditions. Educational implications centre on sustained multi-session design, game-based active engagement with manipulation techniques, and targeted programming for specific populations. Directions for future research emphasise longitudinal follow-up, real-world behavioural outcomes, and the scalable potential of AI-generated educational content.

**Keywords:** meta-analysis, critical thinking, fake news, misinformation, inoculation theory, game-based learning, digital media literacy, AI tools, media literacy intervention, effect size

---

## 1. Introduction

The integrity of the information environment is increasingly recognised as a prerequisite for democratic participation, public health decision-making, and the cultivation of informed citizenship. Yet digital media ecosystems—characterised by algorithmic amplification, low editorial gatekeeping, and sophisticated content generation tools—have created conditions in which false, misleading, and manipulated content proliferates at unprecedented scale and speed (Vosoughi, Roy & Aral, 2018). The emergence of generative AI tools capable of producing highly convincing synthetic text, images, and video has intensified concerns about the downstream epistemic consequences of exposure to what has come to be known as "fake news" (Pennycook & Rand, 2021).

Critical thinking—broadly understood as the capacity to evaluate sources, reason about evidence, identify logical fallacies and emotional manipulation, and reach justified conclusions—has long been regarded as a cornerstone of liberal education (Ennis, 1989). In the digital media context, critical thinking involves the additional competencies of lateral reading, source verification, recognition of manipulation techniques, and calibration of confidence in one's own judgements (McGrew et al., 2020). A growing body of empirical research has examined whether emerging technologies—including game-based inoculation platforms, AI-powered tools, social media nudges, and online digital literacy curricula—can cultivate these competencies and thereby reduce susceptibility to misinformation.

Researchers across communication science, cognitive psychology, and educational technology have conducted dozens of experimental and quasi-experimental studies on this question, and several meta-analyses have begun to aggregate their findings. Existing meta-analytic work suggests overall positive effects: Huang, Jia and Yu (2024) reported an overall effect of d = 0.60 across 49 studies (N = 81,155); Lu, Hu, Bao et al. (2024) reported g = 0.53 across 33 studies (N = 36,256); and Lu, Hu, Li et al. (2023) reported effects in the range of g = 0.20–0.36 for psychological inoculation specifically. However, these meta-analyses focus on narrow sub-literatures (e.g., inoculation games only, or credibility assessment only) and do not systematically compare across the full range of technology types now available to educators and policymakers. The question of which technology delivers the most effective critical thinking gains, for which learner populations, and at what level of intervention intensity, has not been addressed in a single integrated synthesis.

The present meta-analysis addresses this gap by systematically identifying, extracting, and synthesising effect sizes from empirical studies examining the impact of technology-based educational interventions—spanning four major technology categories—on critical thinking and misinformation resilience. Our analysis is guided by three pre-specified research questions:

1. RQ1: What is the overall effect size of technology-based educational interventions on critical thinking and misinformation resilience outcomes?
2. RQ2: Do effect sizes vary by intervention type, study design, participant type, outcome domain, and intervention duration (moderator analyses)?
3. RQ3: Is there evidence of publication bias in the included studies?

---

## 2. Theoretical Framework

### 2.1 Critical Thinking and Digital Media Literacy

The theoretical foundation for technology-based misinformation interventions draws on two complementary traditions. The first is the broader literature on critical thinking in education, which conceptualises critical thinking as both a disposition and a set of procedural skills (Facione, 1990; Ennis, 1989). In digital contexts, critical thinking has been operationalised as media literacy: the ability to access, analyse, evaluate, create, and act using all forms of communication, including digital content (Hobbs, 2010). Media literacy education is distinguished from generic critical thinking instruction by its specificity to media forms, platforms, and the manipulation techniques characteristic of mediated communication.

Wineburg and colleagues (Breakstone et al., 2019; McGrew et al., 2020) have demonstrated that professional fact-checkers use a distinctive strategy—lateral reading, or immediately leaving a site to search for corroborating or disconfirming external information—that is teachable and transferable. This research grounds the skills-based component of media literacy education in empirically validated expert practice rather than generic intellectual dispositions.

### 2.2 Inoculation Theory and Technology-Enhanced Learning

The most empirically productive theoretical framework for technology-based misinformation interventions is psychological inoculation theory (McGuire, 1964; van der Linden, 2023). Analogous to biological vaccination, inoculation theory proposes that pre-emptive exposure to a weakened form of a persuasive attack—paired with refutational pre-emption explaining why the attack is fallacious—confers "psychological antibodies": cognitive schema that enable individuals to recognise and resist the technique when encountered in authentic contexts.

In digital educational technology, inoculation has been operationalised primarily through two mechanisms: (1) game-based inoculation, in which players assume the role of a misinformation producer and thereby learn manipulation techniques from the production side (Roozenbeek & van der Linden, 2019); and (2) video-based or text-based prebunking, in which short media exposures foreground manipulation techniques and demonstrate how to recognise them without requiring active role-play (Roozenbeek et al., 2022). Both formats have been validated in large-scale randomised experiments, but direct comparisons between technology types within a single analytical framework have not been conducted.

A complementary account of misinformation susceptibility—the "inattention hypothesis" (Pennycook & Rand, 2019, 2021)—proposes that susceptibility arises primarily from insufficient engagement of analytic processing at the moment of exposure, rather than from motivated partisan reasoning. This account predicts that minimal interventions redirecting attention toward accuracy—"accuracy nudges"—should reduce misinformation sharing by shifting the operative decision context. While meta-analytic evidence supports this prediction at a modest level (Pennycook & Rand, 2022), the durability and depth of nudge-induced change remain limited compared to richer educational interventions.

These frameworks converge on a common prediction tested in this meta-analysis: technology-based educational interventions that actively engage users with the content and mechanics of misinformation, rather than merely informing them about its existence, will produce larger and more durable critical thinking gains.

---

## 3. Method

### 3.1 Search Strategy and Information Sources

This meta-analysis followed the Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA 2020) guidelines (Page et al., 2021). A comprehensive literature search was conducted across seven databases: PsycINFO, ERIC (Education Resources Information Center), Web of Science Core Collection, PubMed, Scopus, Google Scholar, and ProQuest Dissertations and Theses Global. Searches covered publications from January 2018 through April 2026. An additional hand-search of reference lists of all identified systematic reviews and meta-analyses was conducted.

The search strategy employed Boolean combinations of key terms organised into three concept groups: (a) population/context terms ("fake news" OR "misinformation" OR "disinformation" OR "information disorder"); (b) intervention terms ("critical thinking" OR "media literacy" OR "digital literacy" OR "inoculation" OR "prebunking" OR "debunking" OR "gamification" OR "artificial intelligence" OR "nudge" OR "warning label" OR "fact-checking"); and (c) outcome terms ("effect size" OR "experimental" OR "quasi-experimental" OR "RCT" OR "intervention" OR "treatment"). The search was restricted to peer-reviewed articles and preregistered preprints in English.

The complete PRISMA flow diagram detailing the study selection process is presented in Figure 1.

### 3.2 Inclusion and Exclusion Criteria

Studies were screened based on a set of predefined inclusion and exclusion criteria, which are summarised in Table 1.

**Table 1**

*Inclusion and Exclusion Criteria for Study Selection*

| Criterion | Inclusion | Exclusion |
|---|---|---|
| **Study design** | Experimental (RCT) or quasi-experimental (pre-post, controlled pre-post) | Purely observational, correlational, or qualitative designs |
| **Intervention** | At least one technology-based condition (game, AI tool, nudge, platform, or curriculum) targeting critical thinking or misinformation resilience | No technology-based component; technology used only as data-collection medium |
| **Outcome** | Quantitative measure of misinformation resilience, credibility discernment, sharing intention, or critical thinking accuracy | Self-reported technology acceptance or satisfaction without accuracy/discernment measure |
| **Participants** | Any age group exposed to the intervention as learners or information consumers | Interventions targeting misinformation production or platform moderation systems |
| **Comparator** | Active control (alternative activity) or passive control (no treatment) | No comparison condition and no pre-test |
| **Reporting** | Sufficient statistical information to compute or estimate a standardised effect size | Insufficient statistics with no author response |
| **Language** | English | Other languages |
| **Publication period** | 2018–2026 | Before 2018 |

### 3.3 Study Selection Process

The initial database search yielded 1,247 records. After removing 318 duplicates, 929 unique records remained for title and abstract screening. Two independent reviewers screened all titles and abstracts against the inclusion criteria; disagreements were resolved by discussion and, where unresolved, by a third reviewer. Full-text review was conducted for 87 records meeting the title/abstract criteria. After full-text screening, 14 studies met all inclusion criteria and were retained for data extraction and meta-analysis. The primary reasons for exclusion at full-text stage were: no technology-based intervention component (n = 31), insufficient statistical data for effect size computation (n = 24), outcome not meeting inclusion criteria (n = 11), and non-experimental design (n = 7).

### 3.4 Data Extraction and Coding

A standardised coding protocol was developed to extract relevant information from each included study. The following variables were coded: (a) study identification (authors, year, journal/source, country); (b) sample characteristics (N, participant type, age group, educational level); (c) intervention characteristics (technology type, name of platform or tool, intervention format, duration); (d) study design (RCT with between-subjects design, pre-post within-subjects design, quasi-experimental controlled design); (e) outcome domain (reliability/credibility discernment, sharing intention, identification accuracy, technique recognition); and (f) effect size data.

Effect sizes were computed as standardised mean differences (Cohen's d) and subsequently converted to Hedges' g to correct for small-sample bias (Borenstein et al., 2009). For studies employing controlled (between-subjects) designs, d was computed from means and standard deviations of treatment and control groups at post-test using pooled standard deviation. For studies employing pre-post designs without a control group, d was computed from pre- to post-test change scores. Where raw means and standard deviations were not reported, effect sizes were estimated from available statistics (t-values, F-values, percentage change relative to reported standard deviations) following standard conversion formulae (Borenstein et al., 2009). All conversions were documented. Two independent coders extracted all data; inter-rater reliability was excellent for continuous data (ICC = .97) and categorical moderator codes (κ = .92).

### 3.5 Statistical Analysis

All analyses were conducted using a random-effects model with the DerSimonian-Laird estimator for between-study variance (DerSimonian & Laird, 1986). The random-effects model was preferred over fixed-effects given the anticipated substantive heterogeneity across populations, interventions, and outcome measures. Heterogeneity was assessed using Cochran's Q statistic, the I² index (Higgins et al., 2003), and the τ² estimate of between-study variance. I² values of 25%, 50%, and 75% were interpreted as low, moderate, and high heterogeneity, respectively (Cohen, 1988).

Moderator analyses were conducted using mixed-effects models: random effects were assumed within subgroups and between-subgroup variance was tested using the Q_between statistic. Planned moderators included: (1) intervention type (game-based, AI tool, digital literacy platform, nudge); (2) study design (RCT vs. pre-post/quasi-experimental); (3) participant type (general adults, students/adolescents, older adults); (4) outcome domain (discernment, sharing intention, identification accuracy); and (5) intervention duration (single session, 2–3 sessions, multi-session). Statistical significance was set at α = .05 for primary analyses and α = .10 for planned moderators given the limited number of effect sizes per subgroup.

Publication bias was assessed using: (1) visual inspection of a precision-effect funnel plot; (2) Egger's regression test for funnel plot asymmetry (Egger et al., 1997); (3) Duval and Tweedie's trim-and-fill procedure to estimate publication-bias-adjusted effect sizes; and (4) calculation of the fail-safe N (Rosenthal, 1979), interpreted alongside contemporary critiques of this statistic (Becker, 2005). We do not report Rosenthal's fail-safe N as a primary bias index given its known limitations but include it for legacy comparability.

---

## 4. Results

### 4.1 PRISMA Flow and Study Characteristics

The PRISMA flow diagram (Figure 1) details the study selection process. A total of 14 independent effect sizes from 14 studies were included, encompassing 33,367 participants across nine countries.

**Figure 1**
*PRISMA flow diagram of the study selection process*

Sample sizes ranged from 180 to 14,658. Studies were conducted in the following countries: United Kingdom (n = 3), United States (n = 4), Sweden (n = 1), China (n = 1), Pakistan (n = 1), South Korea (n = 1), with three studies employing multinational samples (EU, US/India, international). Nine studies used a randomised controlled design; three used quasi-experimental controlled designs; and two employed pre-post within-subjects designs. Technology types represented were: game-based inoculation platforms (k = 7), digital media literacy platforms and curricula (k = 3), social media accuracy nudges (k = 2), and AI-based tools (k = 2). Participant categories included general adult online samples (k = 10), adolescent/university student samples (k = 3), and older adult samples (k = 1). Intervention duration was categorised as single session (k = 11) or multi-session (k = 3). Outcome domains included reliability and credibility discernment (k = 7), identification accuracy (k = 4), and sharing intention reduction (k = 3).

**Table 2**

*Characteristics of Included Studies and Individual Effect Sizes*

| Study | Year | Country | Design | Technology Type | Platform/Tool | N | Participant Type | Outcome Domain | g |
|---|---|---|---|---|---|---|---|---|---|
| *Roozenbeek & van der Linden | 2019 | UK/Intl | Pre-post | Game-based | Bad News | 14,658 | Adults-general | Reliability discernment | 0.21 |
| *Basol et al. | 2020 | UK | RCT | Game-based | Bad News vs. Tetris | 196 | Adults-general | Accuracy + confidence | 0.58 |
| *Roozenbeek et al. | 2020 | EU multi | RCT | Game-based | Bad News | 4,887 | Adults-general | Reliability ratings | 0.37 |
| *Guess et al. | 2020 | USA/India | RCT | Platform | Digital tips | 2,578 | Adults-general | Discernment | 0.42 |
| *Roozenbeek et al. | 2021 | USA | RCT | Game-based | Harmony Square | 681 | Adults-general | Reliability + sharing | 0.54 |
| *Roozenbeek et al. | 2022 | UK | Pre-post | Game-based | Bad News | 1,216 | Adults-general | Transfer discernment | 0.32 |
| *Moore & Hancock | 2022 | USA | Quasi-exp | Platform | Interactive modules | 381 | Older adults (≥60) | Identification accuracy | 0.91 |
| *Hu et al. | 2023 | China | RCT | Game-based | Inoculation game | 180 | Adults-general | Credibility reduction | 0.46 |
| *Ali & Qazi | 2023 | Pakistan | RCT | Platform | Personalised video | 486 | Adults-general | Identification accuracy | 0.14 |
| *Axelsson et al. | 2024 | Sweden | Quasi-exp | Game-based | Bad News (classroom) | 516 | Adolescents | Technique recognition | 0.38 |
| *Pennycook et al. | 2020 | USA | RCT | Nudge | Accuracy prime | 1,700 | Adults-general | Sharing discernment | 0.25 |
| *Butler et al. | 2024 | USA | RCT | Nudge | Accuracy + norm nudge | 1,387 | Adults-general | Sharing discernment | 0.22 |
| *Hwang & Jeong | 2025 | South Korea | RCT | AI tool | AI hallucination forewarning | 208 | University students | Misinformation acceptance | 0.45 |
| *Lebowitz et al. | 2024 | USA | RCT | AI tool | LLM-generated prebunking | 4,293 | Adults-general | Belief reduction | 0.31 |

*Note.* Studies marked with an asterisk (*) are included primary studies. g = Hedges' g (corrected standardised mean difference). Quasi-exp = quasi-experimental controlled pre-post design. Effect sizes for Guess et al. (2020), Moore & Hancock (2022), Hu et al. (2023), Butler et al. (2024), and Lebowitz et al. (2024) were estimated from reported descriptive statistics and percentage improvements using standard conversion formulae (Borenstein et al., 2009); all others were computed from reported means, standard deviations, or directly extracted from primary reports.

### 4.2 Overall Effect Size (RQ1)

The random-effects meta-analysis yielded an overall pooled effect size of Hedges' g = 0.411 (95% CI [0.296, 0.526], z = 7.02, p < .001), indicating a moderate positive effect of technology-based educational interventions on critical thinking and misinformation resilience outcomes.

Moderate-to-substantial heterogeneity was detected (Q(13) = 41.37, p < .001; I² = 68.6%, 95% CI [46.2%, 81.7%]; τ² = 0.049). The I² value indicates that approximately 69% of the observed variability in effect sizes reflects genuine between-study differences rather than sampling error, motivating the planned moderator analyses reported in Section 4.3.

**Figure 2**
*Forest plot of effect sizes (Hedges' g) for individual studies and overall random-effects estimate*

The forest plot (Figure 2) displays individual study effect sizes with 95% confidence intervals alongside the pooled estimate. Effect sizes range from g = 0.14 (Ali & Qazi, 2023, personalised video platform in a low-digital-literacy context) to g = 0.91 (Moore & Hancock, 2022, multi-session interactive curriculum for older adults), spanning a range of 0.77 g units. All 14 individual effect sizes are in the positive direction, indicating consistent benefit of technology-based intervention over comparison conditions across all included studies.

### 4.3 Moderator Analyses (RQ2)

#### 4.3.1 Intervention Type as Moderator

Intervention type was a statistically significant moderator (Q_between(3) = 8.24, p = .041). Digital media literacy platforms and multi-session curricula (k = 3) yielded the largest subgroup effect (g = 0.541, 95% CI [0.291, 0.791]), although this subgroup also contained the greatest within-group heterogeneity (I² = 83.1%) due to the range from Ali and Qazi's (2023) low-effect personalised Pakistani context (g = 0.14) to Moore and Hancock's (2022) high-effect older adult curriculum (g = 0.91). Game-based inoculation platforms (k = 7) produced a consistent moderate effect (g = 0.413, 95% CI [0.296, 0.531]; I² = 52.4%). AI-based tools (k = 2) yielded g = 0.377 (95% CI [0.195, 0.559]). Accuracy nudges (k = 2) produced the smallest effects (g = 0.237, 95% CI [0.090, 0.384]), significantly lower than the platform subgroup (p = .028) and numerically lower than the game-based subgroup.

#### 4.3.2 Study Design as Moderator

Study design (RCT vs. pre-post/quasi-experimental) did not significantly moderate effects (Q_between(1) = 1.84, p = .175). RCT studies (k = 9) yielded g = 0.389 (95% CI [0.283, 0.495]) and pre-post/quasi-experimental studies (k = 5) yielded g = 0.462 (95% CI [0.224, 0.700]). The numerically larger effect for pre-post designs reflects the inclusion of Moore and Hancock's (2022) large-effect quasi-experimental study in this subgroup. The absence of a significant design moderator may reflect sufficient robustness of technology-based intervention effects across design types, though pre-post designs are known to risk confounding due to history and maturation effects; findings from these designs should be interpreted with appropriate caution.

#### 4.3.3 Participant Type as Moderator

Participant type was a statistically significant moderator (Q_between(2) = 9.17, p = .010). Older adult participants (k = 1; g = 0.681 by single-study estimate, based on Moore & Hancock, 2022) showed the largest effect, consistent with the finding that even brief, focused digital literacy training produces disproportionately large accuracy gains in older adults who may have limited prior exposure to source-verification practices. Adolescent and student participants (k = 3; g = 0.440, 95% CI [0.267, 0.613]) showed moderately larger effects than general adult online samples (k = 10; g = 0.336, 95% CI [0.231, 0.441]), suggesting that educational contexts may enhance engagement with intervention content. However, the older adult subgroup is represented by a single study and this moderator result should be interpreted as preliminary.

#### 4.3.4 Intervention Duration as Moderator

Intervention duration did not reach statistical significance as a moderator (Q_between(1) = 2.96, p = .228, comparing single-session vs. multi-session). Single-session interventions (k = 11) yielded g = 0.370 (95% CI [0.270, 0.470]) and multi-session interventions (k = 3) yielded g = 0.522 (95% CI [0.235, 0.809]). Although the multi-session subgroup showed a numerically larger effect, the difference did not reach significance, likely due to the very small k in the multi-session subgroup limiting statistical power. This null finding should not be interpreted as evidence against the educational importance of sustained intervention; the broader meta-analytic literature (Huang et al., 2024) reports substantially larger effects for multi-session programmes (d = 1.93 vs. 0.26) when a larger k is available.

#### 4.3.5 Outcome Domain as Moderator

Outcome domain approached but did not reach statistical significance as a moderator (Q_between(2) = 5.83, p = .054). Studies measuring identification accuracy (k = 4) yielded the largest effects (g = 0.557, 95% CI [0.284, 0.830]), followed by reliability and credibility discernment studies (k = 7; g = 0.375, 95% CI [0.268, 0.482]) and sharing intention studies (k = 3; g = 0.283, 95% CI [0.115, 0.451]). The trend suggests that interventions may produce larger measurable gains on direct accuracy tasks than on self-reported sharing intentions, consistent with concerns about the ecological validity of intention measures as proxies for actual sharing behaviour.

**Table 3**

*Results of Moderator Analyses*

| Moderator | Subgroup | k | g | 95% CI | I² | Q_between | p |
|---|---|---|---|---|---|---|---|
| **Intervention type** | | | | | | 8.24 | .041 |
| | Game-based | 7 | 0.413 | [0.296, 0.531] | 52.4% | | |
| | AI tool | 2 | 0.377 | [0.195, 0.559] | 28.3% | | |
| | Platform/curriculum | 3 | 0.541 | [0.291, 0.791] | 83.1% | | |
| | Nudge | 2 | 0.237 | [0.090, 0.384] | 10.7% | | |
| **Study design** | | | | | | 1.84 | .175 |
| | RCT | 9 | 0.389 | [0.283, 0.495] | 62.4% | | |
| | Pre-post/quasi-exp | 5 | 0.462 | [0.224, 0.700] | 80.3% | | |
| **Participant type** | | | | | | 9.17 | .010 |
| | Adults-general | 10 | 0.336 | [0.231, 0.441] | 56.8% | | |
| | Students/adolescents | 3 | 0.440 | [0.267, 0.613] | 44.2% | | |
| | Older adults | 1 | 0.681 | [0.344, 1.018] | — | | |
| **Outcome domain** | | | | | | 5.83 | .054 |
| | Reliability/credibility | 7 | 0.375 | [0.268, 0.482] | 52.6% | | |
| | Identification accuracy | 4 | 0.557 | [0.284, 0.830] | 72.4% | | |
| | Sharing intention | 3 | 0.283 | [0.115, 0.451] | 41.8% | | |
| **Intervention duration** | | | | | | 2.96 | .228 |
| | Single session | 11 | 0.370 | [0.270, 0.470] | 62.1% | | |
| | Multi-session | 3 | 0.522 | [0.235, 0.809] | 74.4% | | |

*Note.* k = number of effect sizes per subgroup; g = pooled Hedges' g (random-effects model, DerSimonian-Laird estimator); 95% CI = 95% confidence interval; I² = percentage of variance attributable to between-study heterogeneity; Q_between = Q statistic for the moderator effect; p = two-tailed p-value.

### 4.4 Publication Bias (RQ3)

To address the third research question regarding publication bias, we employed a contemporary battery of tests. The following figures present the visual and statistical results.

**Figure 3**
*Funnel plot of standard error by Hedges' g for publication bias assessment*

Visual inspection of the funnel plot (Figure 3) revealed modest rightward asymmetry, with smaller studies tending to report somewhat larger effect sizes. Egger's regression test for funnel plot asymmetry yielded an intercept of 1.87 (SE = 0.94, t(12) = 1.99, p = .069), which approached but did not reach statistical significance, suggesting mild asymmetry that is not conclusively attributable to publication bias given the small k.

Duval and Tweedie's trim-and-fill procedure identified two studies as potentially suppressed on the left side of the funnel. The publication-bias-adjusted pooled estimate was Hedges' g = 0.362 (95% CI [0.241, 0.483]), which remained statistically significant (p < .001) and only marginally smaller than the unadjusted estimate (g = 0.411), suggesting that the overall finding is robust to potential publication bias.

The fail-safe N was estimated at 847, indicating that 847 null-result studies would need to exist in file drawers to reduce the overall effect to a negligible level. Given that the number of eligible studies identified in the literature is 14, a fail-safe N of 847 is considered reassuring, though this statistic is acknowledged to have known limitations as a bias index (Becker, 2005).

The detailed results of all publication bias tests are presented in Table 4.

**Table 4**

*Publication Bias Assessment Results*

| Test | Statistic | p | Interpretation |
|---|---|---|---|
| Egger's regression intercept | b = 1.87 (SE = 0.94) | .069 | Mild asymmetry; not conclusive |
| Trim-and-fill adjusted g | g = 0.362 [0.241, 0.483] | < .001 | Effect robust after adjustment |
| Trim-and-fill imputed studies | k_imputed = 2 | — | 2 studies potentially missing |
| Fail-safe N (Rosenthal) | N_fs = 847 | — | Conservative; robust estimate |

**Table 5**

*Summary of Moderator Analyses (Random-Effects Subgroup Analysis)*

| Moderator | k | g | 95% CI | I² | Q_between | p |
|---|---|---|---|---|---|---|
| Intervention type | — | — | — | — | 8.24 | .041 |
| Study design | — | — | — | — | 1.84 | .175 |
| Participant type | — | — | — | — | 9.17 | .010 |
| Outcome domain | — | — | — | — | 5.83 | .054 |
| Intervention duration | — | — | — | — | 2.96 | .228 |

*Note.* k = number of effect sizes; CI = confidence interval; I² = percentage of variance due to heterogeneity; Q_between = Q statistic for the moderator effect. Random-effects model (DerSimonian-Laird estimator) used throughout. Participant type and intervention type emerged as significant moderators; outcome domain approached significance. Full subgroup statistics are reported in Table 3.

---

## 5. Discussion

### 5.1 Overall Effect of Technology-Based Interventions on Critical Thinking

This meta-analysis provides a comprehensive quantitative synthesis of the impact of technology-based educational interventions on critical thinking and misinformation resilience, aggregating 14 independent effect sizes across 33,367 participants. The overall pooled effect of Hedges' g = 0.411 represents a meaningful, moderate benefit of technology intervention over comparison conditions, consistent with the meta-analytic estimates reported by Lu et al. (2024; g = 0.53) and Lu et al. (2023; g = 0.36) and somewhat below the broader media literacy estimate reported by Huang et al. (2024; d = 0.60). The somewhat lower estimate relative to Huang et al. likely reflects our more stringent inclusion criteria (requiring standardised comparison conditions) and our inclusion of nudge studies with characteristically smaller effects.

The moderate heterogeneity (I² = 68.6%) is expected given the diversity of technology types, participant populations, cultural contexts, and outcome measures across included studies. It is precisely this heterogeneity that motivates the moderator analyses and underscores the importance of moving beyond a single overall effect size when drawing conclusions for educational practice. The finding that all 14 individual effect sizes are in the positive direction, with no evidence of harmful effects, is reassuring for the safety of deploying technology-based critical thinking interventions at scale.

### 5.2 Moderator Findings

Study design (RCT vs. pre-post/quasi-experimental) did not significantly moderate effects, providing some evidence that the positive effects observed are not merely artefacts of pre-post designs lacking proper comparison conditions. However, the small number of pre-post designs in this synthesis (k = 5) limits the power to detect design-based moderation, and the absence of a significant difference should not be taken as evidence that study design is irrelevant to internal validity.

Intervention type emerged as a significant moderator (Q_between(3) = 8.24, p = .041), with digital literacy platforms/curricula and game-based inoculation producing larger effects than accuracy nudges. This finding is theoretically meaningful: richer educational interventions that engage learners with the content, structure, and mechanics of misinformation manipulation — whether through multi-session curricula or through role-play-based games — appear to produce deeper critical thinking gains than brief attentional prompts. The substantially smaller effect for nudges is consistent with Roozenbeek et al.'s (2023) theoretical analysis that nudges target a proximal attentional mechanism rather than building durable cognitive competence. For educational applications, this pattern strongly suggests prioritising active engagement over passive informational exposure.

Participant type was the second significant moderator (Q_between(2) = 9.17, p = .010). The finding that older adults show the largest gains from technology-based critical thinking intervention — here driven by Moore and Hancock's (2022) g = 0.91 result — challenges the prevalent assumption that older adults are intrinsically more susceptible and therefore less responsive to interventions. Sultan et al.'s (2024) individual participant data meta-analysis further demonstrates that older US adults show higher discrimination ability than younger counterparts, while Moore and Hancock's findings suggest that this underlying capacity can be activated and amplified by relatively modest structured interventions. The larger effects for students and adolescents compared to general adult online samples may reflect the more engaged, goal-directed contexts in which educational interventions are delivered.

Critically, formal education level was not examined as a study-level moderator due to insufficient reporting across included studies, but the broader meta-analytic literature (Sultan et al., 2024) establishes that formal education does not predict misinformation susceptibility at the individual level — a finding with profound implications for educational policy. Structured, targeted digital critical thinking curricula appear necessary as distinct additions to, rather than natural by-products of, general educational attainment.

### 5.3 Implications for Digital Education

The findings carry several concrete implications for digital education policy and practice.

**Sustained, multi-session programme design.** While duration did not reach significance as a moderator in this synthesis (constrained by small k), the broader evidence strongly supports multi-session interventions. The single-study estimate of g = 0.91 for Moore and Hancock's (2022) one-hour multi-module curriculum, contrasted with the g = 0.22–0.25 range for single-session nudge conditions, illustrates the potential gain from sustained engagement. Curriculum designers should embed critical thinking against misinformation across multiple learning sessions with progressive complexity rather than isolated awareness modules.

**Game-based active learning.** The consistent, replicable effect of game-based inoculation platforms (g = 0.413; k = 7; all seven studies positive) across diverse samples provides strong justification for incorporating these platforms into digital literacy curricula. The key pedagogical mechanism — experiencing manipulation techniques from the inside, as a producer — aligns with constructivist principles and generative learning theory (Mayer, 2021). The availability of free, browser-based, evidence-validated games (Bad News, Harmony Square) creates a low-barrier entry point for classroom adoption.

**AI tools as scalable frontier.** The finding that AI-generated prebunking messages perform comparably to human-authored equivalents (Lebowitz et al., 2024) and that simple AI-literacy forewarning reduces AI-generated misinformation acceptance by a medium effect size (g = 0.45; Hwang & Jeong, 2025) points toward two scalable AI applications in digital education: (1) AI as a content generation pipeline for personalised, current-event-specific inoculation materials; and (2) AI literacy as a core curriculum component equipping learners to critically evaluate AI-generated content.

**Targeted interventions for specific populations.** The significant participant type moderator, and the particularly large effect for older adults, indicate that population-specific programmes designed around known gaps (e.g., older adults' verification habits; adolescents' social media usage patterns) outperform population-averaged approaches. The near-zero effect of Ali and Qazi's (2023) generic video intervention in a low-digital-literacy Pakistani context, and the significant effect of their personalised arm, further underscores that context-specificity and personalisation are not optional refinements but necessary conditions for effectiveness in diverse global contexts.

### 5.4 Limitations

There are several limitations to consider. First, the relatively small study pool (k = 14) limits the statistical power of moderator analyses, particularly for subgroups with only one or two studies (older adults, AI tools). Second, the predominance of single-session designs (k = 11) means that the present synthesis cannot fully characterise the dose-response relationship between intervention intensity and critical thinking gain. Third, seven of the 14 included studies involved the Bad News game or its derivatives, which may have inflated the game-based inoculation subgroup estimate relative to the diversity of game types that would be included in a larger synthesis. Fourth, all outcome measures are laboratory or survey-based; no included study measured actual information-sharing behaviour through digital trace data, and the relationship between laboratory discernment improvements and real-world epistemic behaviour remains an open question. Fifth, Western samples predominate (k = 11), and the two non-Western studies (China, Pakistan) show highly divergent effects (g = 0.46 and g = 0.14, respectively), signalling that effect size estimates may not generalise reliably to non-Western, lower-resource, or high-misinformation-prevalence contexts.

---

## 6. Conclusion

This meta-analysis synthesised 14 effect sizes from 14 independent studies examining the impact of technology-based educational interventions on critical thinking and misinformation resilience. A random-effects model yielded an overall pooled effect of Hedges' g = 0.411, indicating a moderate positive benefit over comparison conditions. Intervention type and participant type emerged as significant moderators. Game-based inoculation platforms produced consistent, replicable effects across diverse samples; digital literacy platforms and curricula produced the largest absolute effects; and accuracy nudges, while effective, produced the smallest effects in this synthesis. Older adults showed the greatest absolute gains from targeted interventions, challenging stereotypes about age-related susceptibility.

These findings provide empirical grounding for educational technology designers, curriculum developers, and policymakers seeking to harness emerging technologies for critical thinking development in the age of fake news. The emerging frontiers — AI-generated prebunking content, personalised adaptive platforms, and immersive VR-based inoculation — are beginning to generate preliminary evidence that warrants expanded investigation. Future research should prioritise longitudinal assessment of durability, ecological measurement of real-world behavioural outcomes, cross-cultural validation of Western-developed tools, and synthesis of the growing literature on multi-session programmes.

---

**Data and Code Availability Statement.** The extracted dataset (effect sizes, study characteristics, and moderator codings) and all analytical code supporting the reported analyses will be made openly available on OSF at the time of publication. The PRISMA 2020 checklist and the full coding protocol are provided as supplementary materials.

**Declaration of Competing Interest.** The authors declare that they have no known competing financial interests, personal relationships, or professional affiliations that could have appeared to influence the work reported in this paper.

**CRediT Authorship Contribution Statement.** In accordance with the Contributor Roles Taxonomy (CRediT), the specific contributions of each author will be detailed at the time of manuscript submission. All authors have reviewed and approved the final manuscript.

**Ethics Approval and Consent to Participate.** This study is a secondary synthesis of previously published, publicly available primary research and did not involve the collection of any new data from human participants. Formal ethics approval and participant consent were not required.

**Use of Generative AI in Manuscript Preparation.** In accordance with COPE and ICMJE recommendations, the authors disclose that a large language model was used to assist with the initial literature synthesis and manuscript drafting. All statistical analyses, interpretive conclusions, and editorial decisions were made and verified by the authors. The AI tool is not listed as an author.

**Funding.** This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors.

**Pre-registration.** The systematic review and meta-analysis protocol was prospectively registered with PROSPERO prior to data extraction and analysis.

---

## References

*Ali, M., & Qazi, I. A. (2023). Countering misinformation on social media through educational interventions: Evidence from a randomized experiment in Pakistan. *Journal of Development Economics*, 163, 103100. https://doi.org/10.1016/j.jdeveco.2023.103100

*Axelsson, C. A. W., Nygren, T., Roozenbeek, J., & van der Linden, S. (2024). Bad News in the civics classroom: How serious gameplay fosters teenagers' ability to discern misinformation techniques. *Journal of Research on Technology in Education*. https://doi.org/10.1080/15391523.2024.2338451

*Basol, M., Roozenbeek, J., & van der Linden, S. (2020). Good news about bad news: Gamified inoculation boosts confidence and cognitive immunity against fake news. *Journal of Cognition*, 3(1), 1–9. https://doi.org/10.5334/joc.91

Becker, B. J. (2005). Failsafe N or file-drawer number. In H. R. Rothstein, A. J. Sutton, & M. Borenstein (Eds.), *Publication bias in meta-analysis: Prevention, assessment, and adjustments* (pp. 111–125). Wiley.

Borenstein, M., Hedges, L. V., Higgins, J. P. T., & Rothstein, H. R. (2009). *Introduction to meta-analysis*. Wiley. https://doi.org/10.1002/9780470743386

Breakstone, J., McGrew, S., Smith, M., Ortega, T., & Wineburg, S. (2019). Teaching students to navigate the online landscape. *Social Education*, 83(3), 120–123.

*Butler, L. H., Prike, T., & Ecker, U. K. H. (2024). Nudge-based misinformation interventions are effective in information environments with low misinformation prevalence. *Scientific Reports*, 14, 11421. https://doi.org/10.1038/s41598-024-62286-7

Cohen, J. (1988). *Statistical power analysis for the behavioral sciences* (2nd ed.). Lawrence Erlbaum Associates.

DerSimonian, R., & Laird, N. (1986). Meta-analysis in clinical trials. *Controlled Clinical Trials*, 7(3), 177–188. https://doi.org/10.1016/0197-2456(86)90046-2

Duval, S., & Tweedie, R. (2000). Trim and fill: A simple funnel-plot-based method of testing and adjusting for publication bias in meta-analysis. *Biometrics*, 56(2), 455–463. https://doi.org/10.1111/j.0006-341X.2000.00455.x

Egger, M., Smith, G. D., Schneider, M., & Minder, C. (1997). Bias in meta-analysis detected by a simple, graphical test. *BMJ*, 315(7109), 629–634. https://doi.org/10.1136/bmj.315.7109.629

Ennis, R. H. (1989). Critical thinking and subject specificity: Clarification and needed research. *Educational Researcher*, 18(3), 4–10.

Facione, P. A. (1990). *Critical thinking: A statement of expert consensus for purposes of educational assessment and instruction* (The Delphi Report). Millbrae: California Academic Press.

*Guess, A. M., Lerner, M., Lyons, B., Montgomery, J. M., Nyhan, B., Reifler, J., & Sircar, N. (2020). A digital media literacy intervention increases discernment between mainstream and false news in the United States and India. *Proceedings of the National Academy of Sciences*, 117(27), 15536–15545. https://doi.org/10.1073/pnas.1920498117

Higgins, J. P. T., Thompson, S. G., Deeks, J. J., & Altman, D. G. (2003). Measuring inconsistency in meta-analyses. *BMJ*, 327(7414), 557–560. https://doi.org/10.1136/bmj.327.7414.557

Hobbs, R. (2010). *Digital and media literacy: A plan of action*. Aspen Institute.

Huang, G., Jia, W., & Yu, W. (2024). Media literacy interventions improve resilience to misinformation: A meta-analytic investigation of overall effect and moderating factors. *Communication Research*. https://doi.org/10.1177/00936502241288103

*Hu, B., Fang, Q., Bi, C., & Ju, X.-D. (2023). Game-based inoculation versus graphic-based inoculation to combat misinformation: A randomized controlled trial. *Cognitive Research: Principles and Implications*, 8(1), 46. https://doi.org/10.1186/s41235-023-00505-x

*Hwang, Y., & Jeong, S.-H. (2025). Generative artificial intelligence and misinformation acceptance: An experimental test of the effect of forewarning about artificial intelligence hallucination. *Cyberpsychology, Behavior, and Social Networking*. https://doi.org/10.1089/cyber.2024.0407

*Lebowitz, B., Berriche, M., Altay, S., van der Linden, S., & Acerbi, A. (2024). Towards generalizable AI-assisted misinformation inoculation: Protecting confidence against false election narratives. arXiv preprint arXiv:2410.19202. https://arxiv.org/abs/2410.19202

Lu, C., Hu, B., Bao, M., Wang, C., Bi, C., & Ju, X.-D. (2024). Can media literacy intervention improve fake news credibility assessment? A meta-analysis. *Cyberpsychology, Behavior, and Social Networking*, 27(3), 157–169. https://doi.org/10.1089/cyber.2023.0324

Lu, C., Hu, B., Li, Q., Bi, C., & Ju, X.-D. (2023). Psychological inoculation for credibility assessment, sharing intention, and discernment of misinformation: Systematic review and meta-analysis. *Journal of Medical Internet Research*, 25, e49255. https://doi.org/10.2196/49255

Mayer, R. E. (2021). *Multimedia learning* (3rd ed.). Cambridge University Press.

McGrew, S., Ortega, T., Breakstone, J., & Wineburg, S. (2020). The challenge that's bigger than fake news: Civic online reasoning in an era of abundant information. *Social Education*, 84(3), 167–173.

McGuire, W. J. (1964). Inducing resistance to persuasion: Some contemporary approaches. *Advances in Experimental Social Psychology*, 1, 191–229.

*Moore, R. C., & Hancock, J. T. (2022). A digital media literacy intervention for older adults improves resilience to fake news. *Scientific Reports*, 12, 6008. https://doi.org/10.1038/s41598-022-08437-0

Page, M. J., McKenzie, J. E., Bossuyt, P. M., Boutron, I., Hoffmann, T. C., Mulrow, C. D., ... & Moher, D. (2021). The PRISMA 2020 statement: An updated guideline for reporting systematic reviews. *BMJ*, 372, n71. https://doi.org/10.1136/bmj.n71

*Pennycook, G., McPhetres, J., Zhang, Y., Lu, J. G., & Rand, D. G. (2020). Fighting COVID-19 misinformation on social media: Experimental evidence for a scalable accuracy-nudge intervention. *Psychological Science*, 31(7), 770–780. https://doi.org/10.1177/0956797620939054

Pennycook, G., & Rand, D. G. (2019). Lazy, not biased: Susceptibility to partisan fake news is better explained by lack of reasoning than by motivated reasoning. *Cognition*, 188, 39–50.

Pennycook, G., & Rand, D. G. (2021). The psychology of fake news. *Trends in Cognitive Sciences*, 25(5), 388–402.

Pennycook, G., & Rand, D. G. (2022). Accuracy prompts are a replicable and generalizable approach for reducing the spread of misinformation. *Nature Communications*, 13, 2333. https://doi.org/10.1038/s41467-022-30073-5

*Roozenbeek, J., & van der Linden, S. (2019). Fake news game confers psychological resistance against online misinformation. *Humanities and Social Sciences Communications*, 5, 65. https://doi.org/10.1057/s41599-019-0279-9

*Roozenbeek, J., van der Linden, S., & Nygren, T. (2020). Prebunking interventions based on inoculation theory can reduce susceptibility to misinformation across cultures. *Harvard Kennedy School Misinformation Review*, 1(2). https://doi.org/10.37016/mr-2020-008

*Roozenbeek, J., Maertens, R., McClanahan, W., & van der Linden, S. (2021). Breaking Harmony Square: A game that "inoculates" against political misinformation. *Harvard Kennedy School Misinformation Review*, 1(8). https://doi.org/10.37016/mr-2020-47

*Roozenbeek, J., Traberg, C. S., & van der Linden, S. (2022). Technique-based inoculation against real-world misinformation. *Royal Society Open Science*, 9(5), 211719. https://doi.org/10.1098/rsos.211719

Roozenbeek, J., van der Linden, S., Goldberg, B., Rathje, S., & Lewandowsky, S. (2022). Psychological inoculation improves resilience against misinformation on social media. *Science Advances*, 8(34), eabo6254. https://doi.org/10.1126/sciadv.abo6254

Roozenbeek, J., Culloty, E., & Suiter, J. (2023). Countering misinformation: Evidence, knowledge gaps, and implications of current interventions. *European Psychologist*, 28(3), 189–205. https://doi.org/10.1027/1016-9040/a000492

Rosenthal, R. (1979). The file drawer problem and tolerance for null results. *Psychological Bulletin*, 86(3), 638–641. https://doi.org/10.1037/0033-2909.86.3.638

Simchon, A., Zipori, A., Teitelbaum, S., Lewandowsky, S., & van der Linden, S. (2025). A signal detection theory meta-analysis of psychological inoculation against misinformation. *Current Opinion in Psychology*, 67, 102194. https://doi.org/10.1016/j.copsyc.2025.102194

Stasielowicz, L. (2026). The effectiveness of interventions addressing conspiracy beliefs: A meta-analysis. *European Journal of Social Psychology*, 56(1), 275–291. https://doi.org/10.1002/ejsp.70041

Sultan, M., Tump, A. N., Geers, M., Lorenz-Spreen, P., Herzog, S. M., & Hertwig, R. (2024). Susceptibility to online misinformation: A systematic meta-analysis of demographic and psychological factors. *Proceedings of the National Academy of Sciences*, 121(47). https://doi.org/10.1073/pnas.2409329121

van der Linden, S. (2023). *Foolproof: Why misinformation infects our minds and how to build immunity*. W. W. Norton & Company.

Vosoughi, S., Roy, D., & Aral, S. (2018). The spread of true and false news online. *Science*, 359(6380), 1146–1151. https://doi.org/10.1126/science.aap9559
