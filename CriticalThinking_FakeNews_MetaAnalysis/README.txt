====================================================================
  Critical Thinking Against Fake News: Meta-Analysis Package
  Digital Education Review (DER) – Special Issue Submission
====================================================================

SUBMISSION DETAILS
  Abstract deadline  : 30 September 2026
  Full paper deadline: 30 January 2027
  Email              : digital.education.review@ub.edu

FILES IN THIS FOLDER
--------------------------------------------------------------------
meta_analysis_critical_thinking_fake_news.md
  → Full manuscript (all sections, tables, references)
  → Appendix A = 499-word abstract ready for email submission
  → Open in any Markdown viewer or convert to DOCX with Pandoc

figure1_prisma.png
  → PRISMA 2020 flow diagram
  → 1,247 records → 14 included studies

figure2_forest_plot.png
  → Forest plot: 14 study effect sizes + pooled diamond
  → Hedges' g per study, colour-coded by technology type
  → Overall: g = 0.411 (95% CI [0.296, 0.526])

figure3_funnel_plot.png
  → Funnel plot for publication bias assessment
  → Egger's test: b = 1.87, p = .069
  → Trim-and-fill adjusted g = 0.362

CriticalThinking_FakeNews_MetaAnalysis.cma
  → Comprehensive Meta-Analysis (CMA v3) data file
  → Open with CMA software (Borenstein et al.)
  → Contains all 14 studies with g, SE, moderator codes
  → Software will re-compute pooled statistics on opening

generate_figures.py
  → Python script that produced the three figures
  → Requires: matplotlib, numpy
  → Run: python3 generate_figures.py

crossref_results.json
  → DOI verification results (CrossRef API)
  → Note: outbound network was restricted in this session;
    manual DOI verification recommended via doi.org

HOW TO CONVERT .md TO .docx
--------------------------------------------------------------------
  pandoc meta_analysis_critical_thinking_fake_news.md \
         -o MetaAnalysis_DER_Submission.docx \
         --reference-doc=your_template.docx

IMPORTANT NOTES
--------------------------------------------------------------------
• Some effect sizes in Table 2 are ESTIMATED from reported
  descriptive statistics (marked in the Table 2 note).
  Verify against primary papers before final submission.

• The CMA file study-level data is correct; open in CMA software
  to obtain the definitive pooled g and heterogeneity statistics.

• Reference DOI verification was partially completed via WebSearch
  agents. Full CrossRef verification recommended at:
  https://apps.crossref.org/SimpleTextQuery

====================================================================
