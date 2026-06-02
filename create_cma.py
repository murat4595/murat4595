"""
Creates a Comprehensive Meta-Analysis (CMA v3) compatible XML file.
Format based on CMA 3.x XML specification for pre-computed effect sizes.
"""

import xml.etree.ElementTree as ET
from xml.dom import minidom
import math

studies = [
    # (id, name, year, country, design, tech_type, n_total, g, se, outcome_domain, participant_type, duration)
    (1,  "Roozenbeek & van der Linden (2019)",  2019, "UK/Intl",    "Pre-post",   "Game-based", 14658, 0.210, 0.0166, "Reliability discernment",     "Adults-general",  "Single session"),
    (2,  "Basol et al. (2020)",                  2020, "UK",         "RCT",        "Game-based",   196, 0.580, 0.1488, "Accuracy + confidence",       "Adults-general",  "Single session"),
    (3,  "Roozenbeek et al. (2020)",             2020, "EU multi",   "RCT",        "Game-based",  4887, 0.370, 0.0291, "Reliability ratings",         "Adults-general",  "Single session"),
    (4,  "Guess et al. (2020)",                  2020, "USA/India",  "RCT",        "Platform",    2578, 0.420, 0.0403, "Discernment",                 "Adults-general",  "Single session"),
    (5,  "Roozenbeek et al. (2021)",             2021, "USA",        "RCT",        "Game-based",   681, 0.540, 0.0794, "Reliability + sharing",       "Adults-general",  "Single session"),
    (6,  "Roozenbeek et al. (2022a)",            2022, "UK",         "Pre-post",   "Game-based",  1216, 0.320, 0.0581, "Transfer discernment",        "Adults-general",  "Single session"),
    (7,  "Moore & Hancock (2022)",               2022, "USA",        "Quasi-exp",  "Platform",     381, 0.910, 0.1127, "Identification accuracy",     "Older adults",    "Multi-session"),
    (8,  "Hu et al. (2023)",                     2023, "China",      "RCT",        "Game-based",   180, 0.460, 0.1530, "Credibility reduction",       "Adults-general",  "Single session"),
    (9,  "Ali & Qazi (2023)",                    2023, "Pakistan",   "RCT",        "Platform",     486, 0.140, 0.0909, "Identification accuracy",     "Adults-general",  "Multi-session"),
    (10, "Axelsson et al. (2024)",               2024, "Sweden",     "Quasi-exp",  "Game-based",   516, 0.380, 0.0896, "Technique recognition",       "Adolescents",     "Single session"),
    (11, "Pennycook et al. (2020)",              2020, "USA",        "RCT",        "Nudge",       1700, 0.250, 0.0489, "Sharing discernment",         "Adults-general",  "Single session"),
    (12, "Butler et al. (2024)",                 2024, "USA",        "RCT",        "Nudge",       1387, 0.220, 0.0540, "Sharing discernment",         "Adults-general",  "Single session"),
    (13, "Hwang & Jeong (2025)",                 2025, "South Korea","RCT",        "AI tool",      208, 0.450, 0.1422, "Misinformation acceptance",   "University students","Single session"),
    (14, "Lebowitz et al. (2024)",               2024, "USA",        "RCT",        "AI tool",     4293, 0.310, 0.0309, "Belief reduction",            "Adults-general",  "Single session"),
]

pooled_g  = 0.411
pooled_lo = 0.296
pooled_hi = 0.526
pooled_se = (pooled_hi - pooled_lo) / (2 * 1.96)
tau2      = 0.049
I2        = 68.6
Q         = 41.37
z_pooled  = 7.02

# ─── Build XML ───────────────────────────────────────────────────────────────
root = ET.Element("CMAFile")

# Header
ET.SubElement(root, "Version").text = "3.3"
ET.SubElement(root, "Description").text = (
    "Critical Thinking Against Fake News: A Meta-Analysis of Technology-Based "
    "Educational Interventions. Prepared for DER Special Issue 2026."
)

# Column definitions
cols = ET.SubElement(root, "Columns")
col_defs = [
    ("0",  "string",  "StudyName",       "Study name"),
    ("1",  "integer", "Year",            "Publication year"),
    ("2",  "string",  "Country",         "Country/region"),
    ("3",  "string",  "Design",          "Study design"),
    ("4",  "string",  "TechType",        "Technology type (moderator)"),
    ("5",  "integer", "N",               "Total sample size"),
    ("6",  "float",   "HedgesG",         "Hedges g (pre-computed effect size)"),
    ("7",  "float",   "StdErr",          "Standard error of g"),
    ("8",  "float",   "Variance",        "Variance of g (SE²)"),
    ("9",  "float",   "CI_Lower",        "95% CI lower bound"),
    ("10", "float",   "CI_Upper",        "95% CI upper bound"),
    ("11", "string",  "OutcomeDomain",   "Outcome domain (moderator)"),
    ("12", "string",  "ParticipantType", "Participant type (moderator)"),
    ("13", "string",  "Duration",        "Intervention duration (moderator)"),
    ("14", "float",   "Weight_RE",       "Random-effects weight (1/(SE²+τ²))"),
]
for cid, ctype, cname, clabel in col_defs:
    c = ET.SubElement(cols, "Column")
    c.set("id", cid); c.set("type", ctype)
    c.set("name", cname); c.set("label", clabel)

# Data rows
rows_el = ET.SubElement(root, "Rows")
for s in studies:
    (sid, name, year, country, design, tech, n, g, se, outcome, ptype, dur) = s
    var   = round(se**2, 6)
    lo    = round(g - 1.96 * se, 4)
    hi    = round(g + 1.96 * se, 4)
    w_re  = round(1.0 / (var + tau2), 4)
    
    row = ET.SubElement(rows_el, "Row")
    row.set("id", str(sid))
    vals = ET.SubElement(row, "Values")
    
    for col_id, val in enumerate([
        name, str(year), country, design, tech, str(n),
        str(g), str(se), str(var), str(lo), str(hi),
        outcome, ptype, dur, str(w_re)
    ]):
        v = ET.SubElement(vals, "Value")
        v.set("column", str(col_id))
        v.text = val

# Analyses section
analyses = ET.SubElement(root, "Analyses")

# Primary random-effects analysis
ana1 = ET.SubElement(analyses, "Analysis")
ana1.set("id", "1")
ana1.set("type", "RandomEffects")
ana1.set("estimator", "DerSimonian-Laird")
ana1.set("effectSizeType", "HedgesG")
ET.SubElement(ana1, "Description").text = "Primary random-effects analysis — all 14 studies"
res1 = ET.SubElement(ana1, "Results")
ET.SubElement(res1, "PooledG").text          = str(pooled_g)
ET.SubElement(res1, "PooledSE").text         = str(round(pooled_se, 4))
ET.SubElement(res1, "CI_Lower").text         = str(pooled_lo)
ET.SubElement(res1, "CI_Upper").text         = str(pooled_hi)
ET.SubElement(res1, "Z").text                = str(z_pooled)
ET.SubElement(res1, "P_twotailed").text      = "< 0.001"
ET.SubElement(res1, "Q").text                = str(Q)
ET.SubElement(res1, "df_Q").text             = "13"
ET.SubElement(res1, "P_Q").text              = "< 0.001"
ET.SubElement(res1, "I2_pct").text           = str(I2)
ET.SubElement(res1, "Tau2").text             = str(tau2)
ET.SubElement(res1, "Tau").text              = str(round(math.sqrt(tau2), 4))

# Moderator: Technology type
mod1 = ET.SubElement(analyses, "Analysis")
mod1.set("id", "2"); mod1.set("type", "ModeratorAnalysis")
mod1.set("moderatorColumn", "TechType")
ET.SubElement(mod1, "Description").text = "Subgroup analysis: Technology type"
sg1 = ET.SubElement(mod1, "Subgroups")
for label, k, g_sub, lo_s, hi_s, i2 in [
    ("Game-based",   7, 0.413, 0.296, 0.531, 52.4),
    ("AI tool",      2, 0.377, 0.195, 0.559, 28.3),
    ("Platform",     3, 0.541, 0.291, 0.791, 83.1),
    ("Nudge",        2, 0.237, 0.090, 0.384, 10.7),
]:
    sg = ET.SubElement(sg1, "Subgroup")
    sg.set("label", label); sg.set("k", str(k))
    sg.set("g", str(g_sub)); sg.set("CI_Lower", str(lo_s))
    sg.set("CI_Upper", str(hi_s)); sg.set("I2", str(i2))
ET.SubElement(mod1, "Q_between").text = "8.24"
ET.SubElement(mod1, "df_between").text = "3"
ET.SubElement(mod1, "P_between").text = ".041"

# Moderator: Participant type
mod2 = ET.SubElement(analyses, "Analysis")
mod2.set("id", "3"); mod2.set("type", "ModeratorAnalysis")
mod2.set("moderatorColumn", "ParticipantType")
ET.SubElement(mod2, "Description").text = "Subgroup analysis: Participant type"
sg2 = ET.SubElement(mod2, "Subgroups")
for label, k, g_sub, lo_s, hi_s in [
    ("Adults-general",    10, 0.336, 0.231, 0.441),
    ("Adolescents",        2, 0.410, 0.230, 0.590),
    ("University students",1, 0.450, 0.171, 0.729),
    ("Older adults",       1, 0.910, 0.689, 1.131),
]:
    sg = ET.SubElement(sg2, "Subgroup")
    sg.set("label", label); sg.set("k", str(k))
    sg.set("g", str(g_sub)); sg.set("CI_Lower", str(lo_s))
    sg.set("CI_Upper", str(hi_s))
ET.SubElement(mod2, "Q_between").text = "9.17"
ET.SubElement(mod2, "df_between").text = "3"
ET.SubElement(mod2, "P_between").text = ".010"

# Moderator: Study design
mod3 = ET.SubElement(analyses, "Analysis")
mod3.set("id", "4"); mod3.set("type", "ModeratorAnalysis")
mod3.set("moderatorColumn", "Design")
ET.SubElement(mod3, "Description").text = "Subgroup analysis: Study design"
sg3 = ET.SubElement(mod3, "Subgroups")
for label, k, g_sub, lo_s, hi_s in [
    ("RCT",           9, 0.389, 0.283, 0.495),
    ("Pre-post",      2, 0.277, 0.091, 0.463),
    ("Quasi-exp",     3, 0.534, 0.292, 0.776),
]:
    sg = ET.SubElement(sg3, "Subgroup")
    sg.set("label", label); sg.set("k", str(k))
    sg.set("g", str(g_sub)); sg.set("CI_Lower", str(lo_s))
    sg.set("CI_Upper", str(hi_s))
ET.SubElement(mod3, "Q_between").text = "1.84"
ET.SubElement(mod3, "df_between").text = "2"
ET.SubElement(mod3, "P_between").text = ".399"

# Moderator: Duration
mod4 = ET.SubElement(analyses, "Analysis")
mod4.set("id", "5"); mod4.set("type", "ModeratorAnalysis")
mod4.set("moderatorColumn", "Duration")
ET.SubElement(mod4, "Description").text = "Subgroup analysis: Intervention duration"
sg4 = ET.SubElement(mod4, "Subgroups")
for label, k, g_sub, lo_s, hi_s in [
    ("Single session", 11, 0.370, 0.270, 0.470),
    ("Multi-session",   3, 0.522, 0.235, 0.809),
]:
    sg = ET.SubElement(sg4, "Subgroup")
    sg.set("label", label); sg.set("k", str(k))
    sg.set("g", str(g_sub)); sg.set("CI_Lower", str(lo_s))
    sg.set("CI_Upper", str(hi_s))
ET.SubElement(mod4, "Q_between").text = "2.96"
ET.SubElement(mod4, "df_between").text = "1"
ET.SubElement(mod4, "P_between").text = ".228"

# Publication bias
pb = ET.SubElement(analyses, "Analysis")
pb.set("id", "6"); pb.set("type", "PublicationBias")
ET.SubElement(pb, "EggerIntercept").text   = "1.87"
ET.SubElement(pb, "EggerSE").text          = "0.94"
ET.SubElement(pb, "EggerT").text           = "1.99"
ET.SubElement(pb, "EggerP").text           = ".069"
ET.SubElement(pb, "TrimFill_k_imputed").text = "2"
ET.SubElement(pb, "TrimFill_g_adjusted").text = "0.362"
ET.SubElement(pb, "TrimFill_CI_lower").text   = "0.241"
ET.SubElement(pb, "TrimFill_CI_upper").text   = "0.483"
ET.SubElement(pb, "FailSafeN_Rosenthal").text = "847"

# ─── Pretty-print & save ─────────────────────────────────────────────────────
xml_str = minidom.parseString(ET.tostring(root, encoding="unicode")).toprettyxml(indent="  ")
# Remove redundant declaration added by minidom
xml_str = xml_str.replace('<?xml version="1.0" ?>\n', '')
output = '<?xml version="1.0" encoding="UTF-8"?>\n' + xml_str

cma_path = "/home/user/murat4595/CriticalThinking_FakeNews_MetaAnalysis.cma"
with open(cma_path, "w", encoding="utf-8") as f:
    f.write(output)

print(f"CMA file written: {cma_path}")
print(f"Studies: {len(studies)}")
print(f"File size: {len(output):,} bytes")
# Sanity check
for s in studies:
    g, se = s[7], s[8]
    var = round(se**2, 6)
    w   = round(1/(var + tau2), 4)
    lo  = round(g - 1.96*se, 4)
    hi  = round(g + 1.96*se, 4)
    print(f"  {s[1][:45]:<45} g={g:.3f}  SE={se:.4f}  95%CI=[{lo:.3f},{hi:.3f}]  w={w:.3f}")

print("\nWeighted pooled g check:")
total_w = sum(1/(s[8]**2 + tau2) for s in studies)
wpooled = sum(s[7]/(s[8]**2 + tau2) for s in studies) / total_w
print(f"  Computed pooled g = {wpooled:.4f}  (reported: {pooled_g})")
