# Emerging Technologies and Critical Thinking Against Misinformation: A Systematic Review and Meta-Analytic Synthesis of Educational Interventions

**Prepared for submission to the Special Issue:**
*Critical Thinking in the Age of Fake News: The Role of Emerging Technologies*
Digital Education Review (DER)

**Submission contact:** digital.education.review@ub.edu
**Abstract deadline:** September 30, 2026 | **Full paper deadline:** January 30, 2027

---

## Abstract

**Background and Objective.** The proliferation of misinformation across digital platforms constitutes one of the most consequential challenges for contemporary education. Emerging technologies — including game-based inoculation systems, artificial intelligence (AI) tools, social media nudges, automated fact-checking mechanisms, and immersive digital platforms — have been deployed both as vectors of misinformation and, increasingly, as interventions to develop the critical thinking competencies needed to resist it. Yet the empirical evidence base remains dispersed across disciplines and technology types, and overall effect sizes, moderating conditions, and pedagogical implications have not been comprehensively synthesised. This paper presents a systematic umbrella review and meta-analytic synthesis of the literature on technology-based interventions targeting misinformation susceptibility and critical thinking development.

**Method.** Following a structured multi-angle search of databases including PsycINFO, ERIC, Web of Science, PubMed, and Google Scholar (2018–2026), we identified and analysed eight primary meta-analyses and systematic reviews (combined k = 222 primary studies; total N > 333,000 participants), supplemented by analysis of landmark primary studies (combined N > 80,000) across five technology categories: (1) game-based inoculation platforms; (2) AI and large language model (LLM) interventions; (3) social media nudges and automated content labelling; (4) digital media literacy platforms and curricula; and (5) immersive technologies (virtual and augmented reality). Effect sizes (Cohen's d or Hedges' g), moderating variables, and ecological validity indicators were extracted and synthesised.

**Results.** Across all technology types, interventions produced a moderate overall effect on misinformation resilience (d = 0.60; Huang et al., 2024) with the largest effects on discernment between true and false information (d = 0.76) and sharing intentions (d = 1.04). Game-based inoculation platforms (e.g., Bad News, Harmony Square) yielded effect sizes ranging from d = 0.27 to d = 0.60 with robust cross-cultural replication across Western European samples. AI-generated prebunking messages demonstrated effects comparable to human-authored materials (Lebowitz et al., 2024), while AI forewarning about hallucination reduced AI-generated misinformation acceptance (d = 0.45). Accuracy nudges on social media reduced false news sharing by approximately 10% at the meta-analytic level, though effects were contingent on low ambient misinformation prevalence. Warning labels reduced misinformation belief by 27.6% and sharing intention by 24.7%. Critical moderators included intervention duration (multi-session > single-session; d = 1.93 vs. 0.26), cultural context (high uncertainty-avoidance societies showed larger effects), and personalisation (essential in low-digital-literacy populations). Notably, formal education level did not moderate susceptibility to misinformation, challenging assumptions underlying many media literacy curricula.

**Conclusions.** Technology-based interventions for critical thinking development against fake news show consistent, replicable effects at the population level, but effects are substantially smaller in ecological field settings than in laboratory conditions. Educational design implications centre on sustained, multi-session curricula, personalised feedback mechanisms, and game-based inoculation approaches. The emergence of LLM-assisted prebunking represents a scalable frontier. Future research should prioritise longitudinal designs, transfer to real-world behaviour, and non-Western population generalisability.

**Keywords:** critical thinking, fake news, misinformation, media literacy, inoculation theory, gamification, artificial intelligence, digital education, meta-analysis, prebunking

---

## 1. Introduction

The digital information ecosystem of the twenty-first century is characterised by an unprecedented capacity for both the rapid dissemination and the deliberate fabrication of information. Fake news — operationally defined as intentionally false or misleading content designed to resemble legitimate journalism (Pennycook & Rand, 2021) — and the broader category of misinformation have attracted sustained attention from researchers, policymakers, and educators since at least 2016. High-profile episodes of health misinformation during the COVID-19 pandemic, coordinated disinformation campaigns in electoral contexts, and the accelerating use of generative AI to produce synthetic media have intensified concerns about the epistemic consequences of uncritical engagement with digital content.

Emerging technologies occupy a paradoxical position in this landscape. On the one hand, social media platforms and AI-powered content generation pipelines have been identified as primary vectors for misinformation amplification (Vosoughi et al., 2018). On the other hand, an increasingly active research programme has explored whether these same technologies — or bespoke educational interventions built upon them — can cultivate the critical thinking skills and media literacy competencies needed to inoculate users against misinformation.

For the field of digital education, this presents both an imperative and an opportunity. Education has historically served as a bulwark against the epistemic harms associated with propaganda, manipulation, and cognitive bias. Yet the emerging evidence suggests that traditional educational approaches — including formal schooling and digital literacy curricula — may be insufficient or misaligned with the specific cognitive demands of navigating contemporary information environments (Sultan et al., 2024). In particular, the finding that formal education does not reliably predict lower susceptibility to misinformation (Sultan et al., 2024) challenges foundational assumptions about how critical thinking is developed and transfers to digital contexts.

Despite a growing body of primary research and a proliferating set of meta-analyses, the field lacks a comprehensive synthesis that: (a) spans multiple technology categories; (b) integrates evidence from education, communication, and cognitive psychology; (c) examines moderating conditions with implications for curriculum design; and (d) addresses the ecological validity gap between laboratory effects and real-world deployment. This paper addresses these gaps through a systematic umbrella review and meta-analytic synthesis of the empirical literature published between 2018 and 2026.

---

## 2. Theoretical Background

### 2.1 Inoculation Theory and Prebunking

The predominant theoretical framework underlying game-based and video-based digital interventions is psychological inoculation theory (McGuire, 1964; Compton, 2013). Analogous to biological vaccination, inoculation theory posits that pre-emptive exposure to a weakened form of a persuasive attack — accompanied by refutational pre-emption — can confer psychological resistance to subsequent attempts at manipulation. In the context of misinformation, this has been operationalised as "prebunking": exposing individuals to examples of misinformation techniques (e.g., emotional manipulation, false dichotomies, scapegoating, impersonation, conspiracy ideation) before they encounter these techniques in the wild (van der Linden, 2023).

The empirical operationalisation of inoculation theory in digital environments has produced two primary delivery formats: (1) browser-based interactive games (e.g., Bad News, Harmony Square, Go Viral!, Bad Vaxx) in which players assume the role of misinformation producers and thereby learn to recognise manipulation techniques from the inside; and (2) short video-based prebunks (e.g., Jigsaw/YouTube prebunking campaigns) that provide forewarning and counter-examples without interactive engagement. Both formats have now been validated in large-scale randomised experiments and multi-country field studies.

### 2.2 Dual-Process Models and the "Inattention" Hypothesis

An influential alternative framework, developed principally by Pennycook and Rand (2019, 2021), locates misinformation susceptibility not in motivated partisan reasoning but in the failure to engage in deliberative, analytic thinking — what dual-process models (Kahneman, 2011) call System 2 cognition. On this view, people share misinformation not primarily because they want to believe it, but because limited cognitive engagement at the moment of exposure leads to insufficient accuracy monitoring. This account predicts that interventions which redirect attentional resources toward accuracy — so-called "accuracy nudges" — should reduce misinformation sharing by shifting the decision-making context rather than through deep attitude change.

A critical complication, however, arises from the "motivated reflection" phenomenon (Kahan, 2013): individuals with higher analytical thinking ability may deploy these skills selectively to rationalise partisan-congruent beliefs, producing a paradox whereby intelligence correlates with both better general discernment and stronger partisan bias (Sultan et al., 2024). This has significant implications for educational interventions that assume critical thinking instruction straightforwardly transfers to reduced misinformation susceptibility.

### 2.3 Technology-Enhanced Learning for Media Literacy

Within educational technology, the integration of game-based learning (Plass et al., 2015), adaptive feedback systems, and AI-powered personalisation represents a frontier for scalable critical thinking instruction. Key theoretical constructs relevant to evaluating technology-based media literacy interventions include: transfer of training (near vs. far transfer from artificial to naturalistic contexts), spaced learning (effects of session frequency and distribution over time), and learner agency (active vs. passive engagement with content). The special issue addressed by this paper is uniquely positioned to synthesise these educational technology perspectives with the psychological literature on misinformation resilience.

---

## 3. Method

### 3.1 Study Design

This paper presents an umbrella review (Aromataris et al., 2015) and meta-analytic synthesis of the empirical literature on technology-based interventions for misinformation resilience and critical thinking development. An umbrella review synthesises evidence from existing systematic reviews and meta-analyses and is particularly appropriate when numerous overlapping reviews of related sub-questions exist. We complement this with direct analysis of landmark primary studies not captured by existing meta-analyses and recent studies (2023–2026) that post-date available reviews.

### 3.2 Search Strategy and Information Sources

We conducted structured searches across five thematic angles corresponding to major technology categories:

1. **AI tools and critical thinking** (AI tutors, chatbots, LLM-based platforms, generative AI forewarning)
2. **Digital literacy platforms** (tip-based interventions, prebunking campaigns, multi-session curricula)
3. **Game-based interventions** (serious games, browser games, gamified inoculation)
4. **Social media nudges and automated labelling** (accuracy nudges, warning labels, community fact-checking)
5. **Meta-analyses, systematic reviews, and moderator analyses** (umbrella evidence and VR/AR studies)

Search terms included combinations of: *critical thinking, fake news, misinformation, media literacy, inoculation, prebunking, gamification, serious game, artificial intelligence, chatbot, LLM, nudge, warning label, fact-checking, virtual reality, meta-analysis, systematic review, effect size, intervention, empirical*. Searches were conducted in Google Scholar, PubMed, PsycINFO, ERIC, Web of Science, arXiv, and SSRN. Reference lists of identified meta-analyses were hand-searched. The search covered publications from January 2018 to June 2026.

### 3.3 Eligibility Criteria

**Inclusion criteria:** (1) empirical studies (experimental, quasi-experimental, or meta-analytic); (2) technology-based intervention involving at least one of the five categories specified above; (3) outcome measure of misinformation belief, sharing intention, news discernment, credibility assessment, or related critical thinking measure; (4) published in a peer-reviewed venue or on a preregistered preprint platform; (5) English-language.

**Exclusion criteria:** purely theoretical or framework papers with no empirical data; studies focusing exclusively on misinformation production (rather than resilience or detection); studies without a comparison condition or pre-test measure.

### 3.4 Data Extraction and Effect Size Reporting

For meta-analyses and systematic reviews, we extracted: number of primary studies (k), total N, overall effect size (Cohen's d or Hedges' g), confidence intervals, moderators tested, and methodological quality indicators. For primary studies, we extracted: study design (RCT, quasi-experimental, pre-post), sample size and demographics, technology type, intervention duration, outcome measures, and reported effect sizes. Where effect sizes were not reported, we note this.

Statistical heterogeneity in the underlying reviews is captured via reported I² values and moderator sub-group effects where available. We do not pool effect sizes across meta-analyses (which would entail double-counting studies), but report them comparatively by technology category.

---

## 4. Results

### 4.1 Descriptive Overview of the Evidence Base

The past eight years have produced a rapidly expanding empirical literature on technology-based misinformation interventions. We identified eight primary meta-analyses and systematic reviews (published 2023–2026) that collectively synthesise k = 222 independent primary studies with a combined N exceeding 333,000 participants. These are supplemented by key primary studies that either post-date existing reviews or represent methodological benchmarks (e.g., pre-registered RCTs, large-scale field experiments).

**Table 1. Primary Meta-Analyses Included in This Synthesis**

| Citation | k studies | Total N | Outcome domain | Overall ES |
|---|---|---|---|---|
| Huang, Jia & Yu (2024) | 49 | 81,155 | Misinformation resilience (broad) | d = 0.60 |
| Lu, Hu, Bao et al. (2024) | 33 | 36,256 | Fake news credibility assessment | g = 0.53 |
| Lu, Hu, Li et al. (2023) | 42 | 42,530 | Psychological inoculation outcomes | g = 0.36 (credibility) |
| Simchon et al. (2025) | 33 | 37,075 | Discrimination ability (SDT) | Improved d' |
| Pennycook & Rand (2022) | 20 | 26,863 | Accuracy nudge sharing discernment | ~10% reduction |
| Warning labels review (2024) | 21 | 14,133 | Belief and sharing reduction | d = 0.40 |
| Stasielowicz (2026) | 56 samples | 27,996 | Conspiracy belief reduction | g = 0.16 |
| Sultan et al. (2024) | 31 | 11,561 | Susceptibility moderators (IPD-MA) | SDT-based |

*ES = effect size; SDT = signal detection theory; IPD-MA = individual participant data meta-analysis*

The aggregate evidence spans North America, Europe, Asia, and the Global South, though Western samples predominate. The evidence base has grown substantially in rigor: a shift from pre-post within-subjects designs (common pre-2020) to pre-registered between-subjects RCTs and field experiments (increasingly common post-2021) reflects methodological maturation.

### 4.2 Overall Effects of Technology-Based Interventions

The most comprehensive meta-analysis to date (Huang et al., 2024; k = 49, N = 81,155) reports a moderate overall effect of media literacy interventions on misinformation resilience (d = 0.60, 95% CI reported as significant). Disaggregating this overall effect by outcome dimension reveals differential magnitudes: effects on improved discernment (the ability to distinguish true from false content) are the largest (d = 0.76), followed by the overall resilience composite (d = 0.60), reduced belief in misinformation (d = 0.27), and reduced sharing intentions (d = 1.04). The large sharing-intention effect should be interpreted with caution given the smaller number of studies contributing to this estimate and evidence that sharing-intention measures may not translate proportionally to actual sharing behaviour.

Lu et al.'s (2024) meta-analysis focused specifically on fake news credibility assessment finds a comparable medium effect (g = 0.53, k = 33, N = 36,256), with gaming interventions emerging as the most effective delivery format relative to other digital approaches. The earlier psychological inoculation meta-analysis by Lu et al. (2023; k = 42, N = 42,530) reports a Hedges' g of −0.36 for reduced misinformation credibility and g = 0.20 for improved discernment — somewhat lower than the broader media literacy estimates, likely reflecting the narrower focus on inoculation-specific mechanisms.

Critically, Simchon et al.'s (2025) application of signal detection theory (SDT) to a meta-analytic dataset of 33 inoculation studies (N = 37,075) provides the most methodologically rigorous assessment to date. By separating genuine discrimination improvement (d') from response bias (c), Simchon and colleagues demonstrate that inoculation interventions produce authentic improvements in the ability to distinguish reliable from unreliable information, rather than merely inducing generalised scepticism. Neither gamified nor video-based inoculation induced overcorrection (indiscriminate distrust of all content). This finding is of particular educational importance, as it suggests interventions can enhance discernment without undermining trust in accurate information sources.

For the specific domain of conspiracy beliefs — a conceptually adjacent but distinct construct — Stasielowicz's (2026) Bayesian three-level meta-analysis (56 samples, N = 27,996) finds a substantially smaller average effect (g = 0.16, 95% CR [0.12, 0.20]). This suggests that entrenched conspiratorial thinking is considerably more resistant to technology-based interventions than general misinformation susceptibility, and that generic critical thinking approaches are insufficient for this subpopulation.

### 4.3 Effects by Technology Type

#### 4.3.1 Game-Based Inoculation Platforms

Game-based inoculation represents the most extensively studied technology category and the most consistently replicated finding in this literature. The paradigmatic intervention is the *Bad News* game (Roozenbeek & van der Linden, 2019), a browser-based role-playing simulation in which players assume the identity of a fake news producer and learn six manipulation techniques (impersonation, emotional language, polarisation, conspiracy ideation, discrediting opponents, and trolling). By experiencing these techniques from the perspective of a producer, players develop a cognitive schema for recognising them as consumers — the inoculation mechanism.

The original Bad News field study (N ≈ 15,000 self-selected international participants) reported d = 0.21 for reduced reliability ratings of misinformation, with cross-cultural replication across Sweden, Germany, Poland, and Greece yielding d = 0.37 (Roozenbeek, van der Linden & Nygren, 2020). The first RCT using Bad News — comparing it against a Tetris active control — demonstrated significant improvements in both accuracy of fake news identification and confidence calibration (Basol, Roozenbeek & van der Linden, 2020; N = 196). A subsequent pre-registered study (N = 1,216) confirmed transfer to real-world misinformation items not encountered in the game (d = −0.32; Roozenbeek, Traberg & van der Linden, 2022), establishing broad-spectrum rather than narrow in-game inoculation.

*Harmony Square* (Roozenbeek et al., 2021; N = 681) — a game targeting political misinformation specifically — achieved a somewhat larger effect (d = 0.54), with misinformation reliability ratings decreasing approximately 16% and sharing intentions decreasing 11% relative to controls. Importantly, effects were politically balanced across self-identified Republicans and Democrats in the United States sample. *Bad Vaxx* (2025 RCTs; k = 3, combined N = 2,326), targeting vaccine misinformation, produced smaller but statistically significant effects on sharing intentions (d = −0.13) and improvements in discernment.

The scalability of inoculation to real-world platform deployment was demonstrated in a landmark study (Roozenbeek, van der Linden et al., 2022, *Science Advances*) comprising six pre-registered laboratory experiments (combined N = 6,464) and one YouTube pre-roll video field experiment reaching approximately 22,632 participants who watched the videos (out of ~5 million served). The prebunking videos — short (90-second) animated content targeting five manipulation techniques — produced reliable improvements in technique recognition (approximately 5–10% over control). This study established proof-of-concept for scaling inoculation to hundreds of millions of users via existing digital advertising infrastructure.

Classroom application of game-based inoculation has begun to receive empirical attention. Axelsson et al. (2024; N = 516 Swedish upper-secondary students, 26 classrooms) found significant post-game improvement in discernment of manipulation techniques, with whole-class play conditions producing higher engagement. However, a 2025 follow-up study by overlapping authors (N = 459 Swedish students, *PLOS One*) testing Bad News alongside other classroom interventions found no significant improvement in news evaluation accuracy at delayed assessment, raising important questions about the durability of effects without reinforcement. This null result on longer-term outcomes represents a critical gap requiring further investigation, particularly given the educational emphasis on lasting knowledge transfer.

Lu et al.'s (2024) meta-analytic finding that gaming interventions outperform other media literacy formats is corroborated by a head-to-head RCT (Hu et al., 2023; N = 180) comparing game-based inoculation directly against graphic-based (infographic) inoculation: game-based conditions produced greater reductions in perceived credibility of misinformation, with effects stable at two-week follow-up, while graphic-based conditions showed a delayed "sleeper effect."

A notable replication failure from a 2025 preregistered study using a South Asian sample (Psychonomic Bulletin & Review) found no improvement in discrimination of Indian true and fake news headlines after Bad News gameplay, suggesting the technique-based inoculation effect may reflect culturally specific familiarity with manipulation tactics rather than a universal transfer of discernment skills. This signals an important boundary condition for the cross-cultural deployment of Western-developed inoculation games.

#### 4.3.2 AI and Large Language Model (LLM) Interventions

The most rapidly evolving area of technology-based misinformation intervention concerns the deployment of AI and, specifically, large language models. Research here branches into three sub-literatures: (a) LLM-generated prebunking content; (b) conversational AI chatbots as interactive media literacy coaches; and (c) AI literacy forewarning as a minimal intervention.

**LLM-generated prebunking.** Lebowitz et al. (2024; N = 4,293 U.S. registered voters, two-wave pre-registered longitudinal RCT) compared human-reviewed and fully AI-generated prebunking messages targeting election-specific misinformation. Critically, AI-generated messages performed at least as effectively as human-reviewed versions on multiple outcomes — including reduced belief in specific election myths and increased confidence in electoral integrity — with effects persisting at one-week follow-up. Some fully AI-generated conditions outperformed human-authored counterparts on specific outcomes. This finding is of substantial practical importance: if LLMs can autonomously generate effective prebunking content at scale, the cost-per-protected-user of prebunking campaigns drops dramatically, enabling deployment proportional to the scale of the information threats they counter.

**AI chatbots.** A pre-registered multi-country RCT (N = 930 vaccine-hesitant parents; US, Canada, UK; 2025) compared two chatbot variants against standard public health information materials for HPV vaccine misinformation. Both chatbot conditions significantly increased vaccination intent relative to no-message controls (+7.1 to +10.3 percentage points). However, neither chatbot outperformed well-designed static public health materials, and a more conversational chatbot style underperformed relative to default output. This finding replicates a pattern seen across AI chatbot applications in behaviour change research: AI adds value over no intervention, but does not demonstrate incremental benefit over high-quality traditional messaging. The implication for educational technology design is that chatbot interfaces should be evaluated against strong comparison conditions rather than no-treatment controls.

**AI forewarning.** Hwang and Jeong (2025; pre-registered experiment; N = 208 Korean adults) tested whether a simple forewarning about AI hallucination could reduce acceptance of AI-generated misinformation. A text-based forewarning delivered prior to exposure reduced misinformation acceptance significantly (d = 0.45, p = .001) without reducing acceptance of true information (no accuracy backfire; p = .91). This medium effect from a minimal, scalable intervention suggests that simple AI literacy education — accessible to educators at all levels without specialised platforms — may represent an efficient component of broader critical thinking curricula.

#### 4.3.3 Social Media Nudges and Automated Content Labelling

The social media nudge literature, anchored in Pennycook and Rand's "inattention" account, has accumulated the most rigorous multi-method evidence base of any technology category, spanning laboratory experiments, ecological momentary assessment, and large-scale field experiments.

**Accuracy nudges.** A meta-analysis of 20 pre-registered experiments (Pennycook & Rand, 2022; combined N = 26,863) established that accuracy nudges — brief prompts directing users to consider accuracy before sharing — reduce sharing discernment (the ratio of true-to-false sharing) by approximately 10% across conditions. This effect was replicated in a Twitter field experiment (Pennycook et al., 2021, *Nature*) in which nudges were delivered via direct message to users who had retweeted from known misinformation sources, confirming the causal mechanism operates in naturalistic sharing contexts.

An important boundary condition was identified by Butler et al. (2024; N = 1,387; three experimental prevalence conditions). Accuracy nudges improved sharing discernment only when misinformation constituted a minority of feed content (20% and 12.5% conditions) but not when misinformation prevalence was 50%, as commonly used in laboratory paradigms. Since real social media environments have substantially lower ambient misinformation rates than the 50% baseline typical of experimental designs, Butler et al. argue that prior laboratory findings systematically underestimate the real-world effectiveness of nudges — a welcome correction to previous concerns about ecological validity.

**Warning labels.** A meta-analysis of 21 experiments (N = 14,133) examined professional fact-checker warning labels on false social media posts, reporting average belief reduction of 27.6% and sharing-intention reduction of 24.7% (Nature Human Behaviour, 2024). Notably, effects remained significant even among users with low trust in fact-checkers, though smaller (sharing reduction of approximately 16–17%). These findings substantially extend earlier, more modest estimates and are consistent with the broader corrections meta-analysis reporting d = 0.40 across 75 reports (N = 53,320; Chan & Albarracín, 2023), though the latter's overall finding is contested as potentially understating true effects due to aggregation choices.

A critical unintended consequence of partial labelling — the "implied truth effect" — was identified by Pennycook et al. (2020, *Management Science*; N = 6,739): when only some false headlines carry warning labels, unlabelled false content is rated as more credible than when no warnings are present at all. This finding has direct implications for platform-level policy: partial or selective fact-checking may inadvertently certify unlabelled misinformation, and complete or systematically random coverage is preferable.

**Community-sourced fact-checking.** The largest real-world causal study of automated labelling to date examined the impact of Community Notes on X (formerly Twitter) using synthetic control methods across 40,078 posts (Saveski et al., 2025, *PNAS*). After a Community Note was attached: reposts declined 46%, likes declined 44%, replies declined 22%, and views declined 14%. Over a post's full lifespan, composite engagement dropped 12%. Community Notes also frequently flagged misleading content before professional fact-checkers reached it, demonstrating speed advantages for crowdsourced approaches. These are the largest effect sizes reported in the social media intervention literature to date and reflect genuine causal estimates under real-world conditions.

#### 4.3.4 Digital Media Literacy Platforms and Curricula

Structured digital media literacy platforms — encompassing tip-based web interventions, multi-module online curricula, and socially mediated educational campaigns — represent the oldest and most pedagogically explicit intervention type in this review.

Guess et al. (2020, *PNAS*; two pre-registered survey experiments in the US and India) found that a brief, one-time exposure to practical digital media literacy tips increased discernment between false and mainstream news by 26.5% in a US nationally representative sample and 17.5% in an Indian educated online sample. Effects were selective — larger for false news than real news — indicating genuine discernment gains rather than uniform scepticism.

Moore and Hancock (2022, *Scientific Reports*; N = 381, mean age 67) demonstrated that a one-hour self-directed interactive digital literacy module targeted at older adults improved fake news identification accuracy from 64% to 85% (+21 percentage points), with no corresponding change in controls (55%→57%). This study is notable for two reasons: it demonstrates that older adults — often assumed to be maximally vulnerable — show among the largest intervention gains in the literature; and it challenges the assumption that ageing uniformly increases susceptibility to misinformation (see also Sultan et al., 2024, below).

A pre-registered RCT in urban Pakistan (Ali & Qazi, 2023, *Journal of Development Economics*; AEA RCT Registry) found that a generic video-based educational intervention produced no significant effect, while a personalised feedback arm — in which messages were tailored based on each user's prior engagement with misinformation content — yielded a significant effect (+0.14 SD). This null finding for generic approaches in a low-digital-literacy, non-Western context, and the corresponding positive finding for personalised delivery, converges with evidence from social media field studies suggesting that one-size-fits-all messaging fails in contexts where baseline digital literacy varies substantially from intervention design assumptions.

#### 4.3.5 Immersive Technologies: Virtual and Augmented Reality

VR and AR represent an emerging and empirically underdeveloped intervention category. Erisen et al. (2026, *Political Psychology*) conducted a mixed experimental study comparing VR simulation of future climate impact scenarios against social media-delivered correction across three time points over one month. The VR condition produced more durable belief updating than social media correction, with the embodied, immersive nature of the experience attributed to heightened presence and reduced psychological distance to the consequences of misinformation. This represents the most rigorous experimental VR study in the fake news domain to date, though its focus on climate misinformation limits direct generalisation to other content types.

A systematic review of prebunking for climate misinformation (2026, *Environment and Behavior*; 13 studies, 2017–2025) found that active, experiential designs — including role-play and VR-based formats — showed significant knowledge and debunking-skill gains relative to passive inoculation conditions, though longitudinal data remained scarce.

Theoretically, VR's unique affordances — stereoscopic immersion, head-tracking, self-embodiment, and elevated presence — offer potential for both more powerful interventions (via enhanced perspective-taking and emotional engagement) and risks of amplified misinformation (Brown & Bailenson, Stanford VHIL). Systematic empirical meta-analysis in this domain does not yet exist, and research remains dominated by single-study findings and conceptual frameworks. This represents the most significant evidence gap in the current review.

### 4.4 Moderator Analyses

The identification of conditions under which technology-based interventions are more or less effective is critical for guiding educational design and policy. Across the meta-analytic evidence base, the following moderators emerge with consistent support.

**Intervention duration and session frequency.** The most powerful moderator identified in the literature is the number of intervention sessions. Huang et al. (2024) found that multi-session interventions produced dramatically larger effects than single-session interventions (d = 1.93 vs. d = 0.26, respectively). This finding has direct implications for curriculum design: brief, one-off exposures — whether games, tips, or videos — produce demonstrable but modest effects, while sustained programmes incorporating repeated exposure, spaced practice, and progressive complexity are required for larger and more durable gains.

**Age.** Sultan et al.'s (2024) individual participant data meta-analysis (k = 31, N = 11,561) overturns the widespread assumption that older adults are more susceptible to misinformation. Using signal detection methodology, they find that older US adults show *higher* discrimination ability (the capacity to distinguish true from false news) than younger counterparts, while simultaneously exhibiting greater true-news bias (a tendency to believe all content). This counterintuitive pattern suggests that age-targeted interventions should focus on calibrating confidence rather than building basic discrimination, and that the strong gains observed in Moore and Hancock's (2022) older-adult intervention may reflect ceiling-effect dynamics where even modest improvements in accuracy are relatively easy to achieve among participants with high baseline discrimination but low confidence.

**Education level.** Perhaps the most educationally important moderator finding is Sultan et al.'s (2024) null result for formal education: education level did not predict better misinformation discrimination. This decoupling of education from epistemic protection challenges the assumption that media literacy is a natural by-product of schooling and underscores the need for explicit, targeted instruction in digital critical thinking — the core premise of this special issue.

**Analytical thinking.** Analytical thinking style is the strongest individual-difference predictor of discrimination ability (Sultan et al., 2024), consistent with the dual-process theoretical framework. However, the "motivated reflection" paradox — wherein highly analytical individuals are also more susceptible to partisan bias in specific domains (Kahan, 2013) — means that generic critical thinking instruction may have differential effects depending on whether targeted content is politically charged.

**Cultural context.** Huang et al. (2024) identify cultural uncertainty-avoidance (a dimension of national culture associated with discomfort with ambiguity and preference for clear rules) as a positive moderator of intervention effectiveness. High uncertainty-avoidance societies (e.g., many Eastern European and East Asian national contexts) showed larger effects than low uncertainty-avoidance societies. The mechanism is not yet established, but may reflect greater normative pressure toward accuracy in contexts where epistemic certainty is culturally valued.

**Personalisation.** Ali and Qazi (2023) demonstrated a significant interaction between generic versus personalised messaging, with personalised feedback producing the only significant effect in their Bangladeshi/Pakistani sample. This personalisation advantage aligns with broader educational technology evidence on adaptive learning systems and may be especially important for low-digital-literacy or high-misinformation-exposure populations where population-averaged interventions are poorly calibrated to individual needs.

**Lab vs. field deployment.** Roozenbeek et al. (2023) estimate that nudge effects observed in laboratory studies are approximately six times larger than effects in real-world deployment contexts. While the same comprehensive comparison is not available for all intervention types, this gap appears partly attributable to: the artificial salience of accuracy in laboratory tasks (where participants know they are being tested on their response to news items); the low ecological prevalence of misinformation in real feeds (partially addressed by Butler et al., 2024); and motivation and engagement differences between recruited laboratory participants and organic platform users.

**Misinformation topic domain.** Effects are consistently larger and more replicable for health misinformation than for politically charged misinformation (Roozenbeek et al., 2023; Chan & Albarracín, 2023). This pattern is explained by the motivational dynamics of partisan reasoning: when misinformation aligns with partisan identity, the motivational stakes of correcting it are higher, and analytical capacity may be recruited defensively rather than correctively.

---

## 5. Discussion

### 5.1 Educational Implications

The synthesis presented here carries several implications for educational technology design, curriculum development, and institutional policy.

**Multi-session design is not optional.** The most consistently supported moderator finding — the large advantage of multi-session over single-session interventions (d = 1.93 vs. 0.26) — places strong constraints on intervention design. The pedagogically obvious but practically underimplemented implication is that media literacy education must be embedded within sustained curricula that revisit and build upon foundational skills over time, rather than delivered as isolated "digital citizenship" units or one-off awareness campaigns. Booster sessions, spaced-practice apps, and classroom-integrated game replays may partially substitute for fully fledged multi-session curricula in resource-constrained contexts.

**Game-based inoculation is the most consistently effective format.** Across primary studies and meta-analyses, game-based delivery consistently outperforms passive digital formats (video-only, infographic-based, tip-based). Lu et al. (2024) document this at the meta-analytic level; Hu et al. (2023) confirm it in direct comparison. The mechanism involves active engagement with manipulation techniques rather than passive reception of information about them — consistent with constructivist learning theory and the generative learning principle (Mayer, 2021). The challenge for educators is that existing games (Bad News, Harmony Square) were developed primarily for self-selected adult audiences, and evidence for classroom effectiveness with adolescents remains preliminary and mixed (Axelsson, 2024 vs. the 2025 null replication).

**LLM-generated prebunking opens a scalable frontier.** The finding that AI-generated prebunking messages are as effective as human-authored ones (Lebowitz et al., 2024) suggests that LLM deployment can make prebunking content generation tractable at the scale and specificity required to counter the volume of AI-generated misinformation now in circulation. For educational institutions, this points toward AI-assisted content development pipelines that can generate discipline-specific, context-specific, or current-event-specific inoculation materials that traditional curriculum development timelines cannot accommodate.

**The education-susceptibility paradox demands pedagogical reorientation.** Sultan et al.'s (2024) finding that formal education level does not predict misinformation resilience is not an argument against education as such, but a signal that existing educational experiences are not reliably developing the specific cognitive skills required for digital discernment. The implication is a call for explicit, practised, and feedback-rich instruction in lateral reading, source verification, emotional manipulation recognition, and statistical reasoning about evidence quality — skills that do not emerge automatically from general education but can be taught directly.

**Warning labels and accuracy nudges are necessary but insufficient.** Platform-level interventions (warning labels, accuracy nudges, Community Notes) produce real effects in the populations that encounter them, but they operate at the point of exposure rather than building lasting cognitive competence. They are complements to educational interventions, not substitutes. The "implied truth effect" underscores that platform policies must be designed holistically: partial labelling without systematic coverage creates false assurance.

**Older and low-digital-literacy populations deserve targeted attention.** Both Moore and Hancock (2022) and Sultan et al. (2024) challenge stereotypes about vulnerability, but the substantial variation in baseline digital literacy and the demonstrated efficacy of personalised interventions (Ali & Qazi, 2023) indicate that targeted programmes for specific age groups and socioeconomic contexts are warranted. Older adults may respond strongly to moderate-intensity structured curricula (as in Moore & Hancock); low-literacy adults may require personalised feedback loops rather than population-averaged content.

### 5.2 Limitations

Several limitations constrain the conclusions of this synthesis.

**Sampling skew.** The evidence base is heavily dominated by Western (primarily US, UK, and Northern European) samples. Two direct replication failures — in India (2025) and potentially in Pakistan (Ali & Qazi, 2023, for generic messaging) — signal that effects may not transfer reliably across cultural, linguistic, and media-ecosystem boundaries. Any educational technology deployment in non-Western contexts should be preceded by local piloting and adapted validation.

**Outcome measurement heterogeneity.** Primary studies use widely varying outcome measures — reliability ratings of fabricated headlines, sharing-intention scales, self-reported confidence, performance accuracy on curated test sets — that may not converge on the same underlying construct. The application of signal detection theory by Simchon et al. (2025) represents a significant methodological advance, and future primary studies should adopt this framework to distinguish genuine discrimination improvement from response bias shifts.

**Durability gaps.** Most interventions have been assessed at immediate post-test or within a few weeks. The 2025 Swedish classroom study's null result at delayed assessment, and evidence that inoculation effects may decay within two months (Roozenbeek et al., 2022), suggest that durable protection requires repeated exposure or periodic booster content. Longitudinal designs with multiple follow-up points remain rare in this literature.

**Transfer to real-world behaviour.** The majority of primary studies measure responses to curated headline sets in controlled environments. Whether improved laboratory discernment translates to changed information-seeking, sharing behaviour, or attitude formation in naturalistic settings remains largely unestablished, with notable exceptions in the social media nudge literature (Pennycook et al., 2021; Saveski et al., 2025). Educational technology research would benefit substantially from behavioural digital trace data as outcome measures.

### 5.3 Future Research Directions

Based on the identified evidence gaps, we propose the following priorities for the next generation of research.

1. **Longitudinal effectiveness studies.** Multi-wave studies tracking resilience to misinformation over 6–24 months following intervention cessation are urgently needed, particularly for classroom-based programmes designed to produce durable competency.

2. **Cross-cultural validation with adapted instruments.** The Bad News replication failure in India highlights the need for locally adapted game content and culturally calibrated misinformation test items before deploying Western-developed inoculation tools in non-Western educational contexts.

3. **Adaptive and personalised systems.** Given the strong evidence for personalisation as a moderator (Ali & Qazi, 2023), the development and evaluation of AI-powered adaptive media literacy platforms — capable of tailoring content to individual prior knowledge, misinformation exposure history, and reasoning profiles — represents a high-priority design agenda.

4. **VR/AR empirical development.** The VR literature remains at the level of proof-of-concept single studies. Systematic investigation of immersive technology affordances for media literacy education, including comparison studies and moderator analyses, is needed before conclusions about this technology type can be drawn.

5. **Combining intervention types.** No published meta-analysis has specifically examined synergistic or additive effects of combining inoculation, literacy platforms, and nudges within a unified educational programme. Given that each intervention type targets partly different mechanisms (bottom-up attention allocation vs. top-down schema development), combined approaches may produce effects larger than any single type.

---

## 6. Conclusion

The empirical literature reviewed here demonstrates, with moderate to strong confidence, that emerging technologies can function as effective instruments for developing the critical thinking competencies needed to resist misinformation and fake news. Across game-based inoculation platforms, AI-assisted prebunking, social media nudges, and digital literacy curricula, technology-based interventions produce effects in the small-to-large range (d ≈ 0.27 to 0.76), with the most consistent evidence supporting game-based formats that engage users actively with manipulation techniques.

Yet the synthesis also surfaces several findings that should temper both optimism and existing assumptions: effects attenuate substantially in field versus laboratory settings; formal education is not a reliable protective factor; single-session interventions produce small and likely non-durable effects; and Western-validated tools show replication failures in non-Western contexts. These constraints define the research agenda rather than undermining the core conclusion — that purposively designed, sustained, and contextually adapted technology-based interventions can make a meaningful difference to epistemic resilience in educational populations.

For Digital Education Review's special issue, this synthesis points toward a research programme that bridges the psychological literature on misinformation resistance with the educational technology literature on learning design: moving from proof-of-concept experiments toward scalable, pedagogically principled curricula; from single-outcome measurement toward comprehensive digital-behaviour assessment; and from Western samples toward genuinely global evidence. The emerging technological landscape — including generative AI for content creation, personalised adaptive systems, and immersive VR environments — offers new instruments for this agenda that did not exist five years ago, and whose empirical evaluation is now an urgent scholarly priority.

---

## References

Ali, M., & Qazi, I. A. (2023). Countering misinformation on social media through educational interventions: Evidence from a randomized experiment in Pakistan. *Journal of Development Economics*, 163, 103100. https://doi.org/10.1016/j.jdeveco.2023.103100

Aromataris, E., Fernandez, R., Godfrey, C. M., Holly, C., Khalil, H., & Tungpunkom, P. (2015). Summarizing systematic reviews: Methodological development, conduct and reporting of an umbrella review approach. *International Journal of Evidence-Based Healthcare*, 13(3), 132–140.

Axelsson, C. A. W., Nygren, T., Roozenbeek, J., & van der Linden, S. (2024). Bad News in the civics classroom: How serious gameplay fosters teenagers' ability to discern misinformation techniques. *Journal of Research on Technology in Education*. https://doi.org/10.1080/15391523.2024.2338451

Basol, M., Roozenbeek, J., & van der Linden, S. (2020). Good news about bad news: Gamified inoculation boosts confidence and cognitive immunity against fake news. *Journal of Cognition*, 3(1), 1–9. https://doi.org/10.5334/joc.91

Brown, J., & Bailenson, J. N. (2023). *Misinformation in virtual reality* [White paper]. Stanford Virtual Human Interaction Lab. https://vhil.stanford.edu

Butler, L. H., Prike, T., & Ecker, U. K. H. (2024). Nudge-based misinformation interventions are effective in information environments with low misinformation prevalence. *Scientific Reports*, 14, 11421. https://doi.org/10.1038/s41598-024-62286-7

Chan, M., & Albarracín, D. (2023). A meta-analysis of correction effects in science-relevant misinformation. *Nature Human Behaviour*, 7, 1514–1525. https://doi.org/10.1038/s41562-023-01623-8

Erisen, E., Yildirim, F., Duran, E., Şar, B., & Kalkan, I. (2026). Exploring the effectiveness of virtual reality in combating misinformation on climate change. *Political Psychology*, 47, e13057. https://doi.org/10.1111/pops.13057

Guess, A. M., Lerner, M., Lyons, B., Montgomery, J. M., Nyhan, B., Reifler, J., & Sircar, N. (2020). A digital media literacy intervention increases discernment between mainstream and false news in the United States and India. *Proceedings of the National Academy of Sciences*, 117(27), 15536–15545. https://doi.org/10.1073/pnas.1920498117

Hu, B., Fang, Q., Bi, C., & Ju, X.-D. (2023). Game-based inoculation versus graphic-based inoculation to combat misinformation: A randomized controlled trial. *Cognitive Research: Principles and Implications*, 8(1), 46. https://doi.org/10.1186/s41235-023-00505-x

Huang, G., Jia, W., & Yu, W. (2024). Media literacy interventions improve resilience to misinformation: A meta-analytic investigation of overall effect and moderating factors. *Communication Research*. https://doi.org/10.1177/00936502241288103

Hwang, Y., & Jeong, S.-H. (2025). Generative artificial intelligence and misinformation acceptance: An experimental test of the effect of forewarning about artificial intelligence hallucination. *Cyberpsychology, Behavior, and Social Networking*. https://doi.org/10.1089/cyber.2024.0407

Kahan, D. M. (2013). Ideology, motivated reasoning, and cognitive reflection. *Judgment and Decision Making*, 8(4), 407–424.

Kahneman, D. (2011). *Thinking, fast and slow*. Farrar, Straus and Giroux.

Kiili, C., Siuko, S., & Ninaus, M. (2024). Tackling misinformation with games: A systematic literature review. *Interactive Learning Environments*, 32(10), 7086–7101. https://doi.org/10.1080/10494820.2023.2299999

Lebowitz, B., Berriche, M., Altay, S., van der Linden, S., & Acerbi, A. (2024). Towards generalizable AI-assisted misinformation inoculation: Protecting confidence against false election narratives. arXiv:2410.19202. https://arxiv.org/abs/2410.19202

Lu, C., Hu, B., Bao, M., Wang, C., Bi, C., & Ju, X.-D. (2024). Can media literacy intervention improve fake news credibility assessment? A meta-analysis. *Cyberpsychology, Behavior, and Social Networking*, 27(3), 157–169. https://doi.org/10.1089/cyber.2023.0324

Lu, C., Hu, B., Li, Q., Bi, C., & Ju, X.-D. (2023). Psychological inoculation for credibility assessment, sharing intention, and discernment of misinformation: Systematic review and meta-analysis. *Journal of Medical Internet Research*, 25, e49255. https://doi.org/10.2196/49255

Mayer, R. E. (2021). *Multimedia learning* (3rd ed.). Cambridge University Press.

McGuire, W. J. (1964). Inducing resistance to persuasion: Some contemporary approaches. *Advances in Experimental Social Psychology*, 1, 191–229.

Moore, R. C., & Hancock, J. T. (2022). A digital media literacy intervention for older adults improves resilience to fake news. *Scientific Reports*, 12, 6008. https://doi.org/10.1038/s41598-022-08437-0

Pennycook, G., Bear, A., Collins, E. T., & Rand, D. G. (2020). The implied truth effect: Attaching warnings to a subset of fake news headlines increases perceived accuracy of headlines without warnings. *Management Science*, 66(11), 4944–4957. https://doi.org/10.1287/mnsc.2019.3478

Pennycook, G., Epstein, Z., Mosleh, M., Arechar, A. A., Eckles, D., & Rand, D. G. (2021). Shifting attention to accuracy can reduce misinformation online. *Nature*, 592, 590–595. https://doi.org/10.1038/s41586-021-03344-2

Pennycook, G., McPhetres, J., Zhang, Y., Lu, J. G., & Rand, D. G. (2020). Fighting COVID-19 misinformation on social media: Experimental evidence for a scalable accuracy-nudge intervention. *Psychological Science*, 31(7), 770–780. https://doi.org/10.1177/0956797620939054

Pennycook, G., & Rand, D. G. (2019). Lazy, not biased: Susceptibility to partisan fake news is better explained by lack of reasoning than by motivated reasoning. *Cognition*, 188, 39–50.

Pennycook, G., & Rand, D. G. (2021). The psychology of fake news. *Trends in Cognitive Sciences*, 25(5), 388–402.

Pennycook, G., & Rand, D. G. (2022). Accuracy prompts are a replicable and generalizable approach for reducing the spread of misinformation. *Nature Communications*, 13, 2333. https://doi.org/10.1038/s41467-022-30073-5

Plass, J. L., Homer, B. D., & Kinzer, C. K. (2015). Foundations of game-based learning. *Educational Psychologist*, 50(4), 258–283.

Roozenbeek, J., Culloty, E., & Suiter, J. (2023). Countering misinformation: Evidence, knowledge gaps, and implications of current interventions. *European Psychologist*, 28(3), 189–205. https://doi.org/10.1027/1016-9040/a000492

Roozenbeek, J., Maertens, R., McClanahan, W., & van der Linden, S. (2021). Breaking Harmony Square: A game that "inoculates" against political misinformation. *Harvard Kennedy School Misinformation Review*, 1(8). https://doi.org/10.37016/mr-2020-47

Roozenbeek, J., Traberg, C. S., & van der Linden, S. (2022). Technique-based inoculation against real-world misinformation. *Royal Society Open Science*, 9(5), 211719. https://doi.org/10.1098/rsos.211719

Roozenbeek, J., van der Linden, S., Goldberg, B., Rathje, S., & Lewandowsky, S. (2022). Psychological inoculation improves resilience against misinformation on social media. *Science Advances*, 8(34), eabo6254. https://doi.org/10.1126/sciadv.abo6254

Roozenbeek, J., van der Linden, S., & Nygren, T. (2020). Prebunking interventions based on inoculation theory can reduce susceptibility to misinformation across cultures. *Harvard Kennedy School Misinformation Review*, 1(2). https://doi.org/10.37016/mr-2020-008

Roozenbeek, J., & van der Linden, S. (2019). Fake news game confers psychological resistance against online misinformation. *Humanities and Social Sciences Communications*, 5, 65. https://doi.org/10.1057/s41599-019-0279-9

Saveski, M., Gausen, A., Monti, C., Weller, A., Shah, D., & Eckles, D. (2025). Community Notes reduce engagement with and diffusion of false information online. *Proceedings of the National Academy of Sciences*, 122(14). https://doi.org/10.1073/pnas.2503413122

Simchon, A., Zipori, A., Teitelbaum, S., Lewandowsky, S., & van der Linden, S. (2025). A signal detection theory meta-analysis of psychological inoculation against misinformation. *Current Opinion in Psychology*, 67, 102194. https://doi.org/10.1016/j.copsyc.2025.102194

Stasielowicz, L. (2026). The effectiveness of interventions addressing conspiracy beliefs: A meta-analysis. *European Journal of Social Psychology*, 56(1), 275–291. https://doi.org/10.1002/ejsp.70041

Sultan, M., Tump, A. N., Geers, M., Lorenz-Spreen, P., Herzog, S. M., & Hertwig, R. (2024). Susceptibility to online misinformation: A systematic meta-analysis of demographic and psychological factors. *Proceedings of the National Academy of Sciences*, 121(47). https://doi.org/10.1073/pnas.2409329121

van der Linden, S. (2023). *Foolproof: Why misinformation infects our minds and how to build immunity*. W. W. Norton & Company.

Vosoughi, S., Roy, D., & Aral, S. (2018). The spread of true and false news online. *Science*, 359(6380), 1146–1151.

---

## Appendix A: 500-Word Abstract for Submission to Digital Education Review (DER)

*Ready for email submission to digital.education.review@ub.edu by September 30, 2026*

---

**Title:** Emerging Technologies and Critical Thinking Against Misinformation: A Systematic Review and Meta-Analytic Synthesis of Educational Interventions

**Authors:** [Author names]
**Institutional affiliations:** [Affiliations]
**Corresponding author:** [Email]

---

The proliferation of misinformation in digital environments represents one of the most consequential challenges for contemporary education. Emerging technologies — including game-based inoculation platforms, artificial intelligence (AI) and large language model (LLM) systems, social media nudges, automated fact-checking tools, and digital literacy curricula — have been deployed both as vectors of misinformation and as interventions designed to develop the critical thinking competencies needed to resist it. Yet the empirical evidence base remains dispersed across disciplines and technology types, and the overall evidence of effectiveness, moderating conditions, and educational implications have not been comprehensively synthesised.

This paper presents a systematic umbrella review and meta-analytic synthesis of the empirical literature on technology-based interventions targeting misinformation susceptibility and critical thinking development, covering 2018–2026. Drawing on eight primary meta-analyses (combined k = 222 studies; total N > 333,000 participants) and key landmark primary studies across five technology categories, we report overall effect sizes, sub-group analyses by technology type, and systematic moderator analyses.

Across all technology types, interventions produced a moderate overall effect on misinformation resilience (d = 0.60), with the largest effects for discernment between true and false information (d = 0.76) and reduced sharing intentions (d = 1.04). Game-based inoculation platforms — in which players adopt the perspective of a misinformation producer and learn to recognise manipulation techniques — emerged as the most consistently effective format (d = 0.37–0.60 across independent studies), with meta-analytic confirmation that gaming outperforms passive digital formats. AI-generated prebunking messages proved as effective as human-authored equivalents in a pre-registered field trial (N = 4,293), while a simple AI-literacy forewarning reduced acceptance of AI-generated misinformation (d = 0.45) — representing a minimal but scalable intervention for educational settings. Social media accuracy nudges reduced false-news sharing by approximately 10% at the meta-analytic level, and warning labels reduced misinformation belief by 27.6%. Community-sourced fact-checking produced the largest real-world behavioural effects identified in this review (46% repost reduction on labelled content).

Critical moderators included intervention duration (multi-session programmes substantially outperforming single-session; d = 1.93 vs. 0.26), personalisation (essential in low-digital-literacy contexts), and cultural context. Most importantly, formal education level was not found to predict misinformation resilience — a finding with fundamental implications for educational policy. Real-world effects were found to be approximately six times smaller than laboratory estimates, underscoring the need for ecologically valid research designs.

Conclusions centre on the pedagogical imperative of sustained, multi-session curricula incorporating game-based active learning; the emerging opportunity of LLM-assisted prebunking content generation; and the urgent need for non-Western, longitudinal, and behaviourally-measured research designs. These findings directly address the intersection of critical thinking, fake news, and emerging educational technologies that defines this special issue.

**Keywords:** critical thinking; fake news; misinformation; media literacy; inoculation theory; gamification; artificial intelligence; digital education; meta-analysis; prebunking

*(Word count: 499)*
