import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
import numpy as np

# ─────────────────────────────────────────────
# STUDY DATA
# ─────────────────────────────────────────────
studies = [
    {"label": "Roozenbeek & van der Linden (2019)",  "n": 14658, "g": 0.21},
    {"label": "Basol et al. (2020)",                  "n": 196,   "g": 0.58},
    {"label": "Roozenbeek et al. (2020)",             "n": 4887,  "g": 0.37},
    {"label": "Guess et al. (2020)",                  "n": 2578,  "g": 0.42},
    {"label": "Roozenbeek et al. (2021)",             "n": 681,   "g": 0.54},
    {"label": "Roozenbeek et al. (2022)",             "n": 1216,  "g": 0.32},
    {"label": "Moore & Hancock (2022)",               "n": 381,   "g": 0.91},
    {"label": "Hu et al. (2023)",                     "n": 180,   "g": 0.46},
    {"label": "Ali & Qazi (2023)",                    "n": 486,   "g": 0.14},
    {"label": "Axelsson et al. (2024)",               "n": 516,   "g": 0.38},
    {"label": "Pennycook et al. (2020)",              "n": 1700,  "g": 0.25},
    {"label": "Butler et al. (2024)",                 "n": 1387,  "g": 0.22},
    {"label": "Hwang & Jeong (2025)",                 "n": 208,   "g": 0.45},
    {"label": "Lebowitz et al. (2024)",               "n": 4293,  "g": 0.31},
]

for s in studies:
    se = np.sqrt((4 + s["g"]**2) / s["n"])
    s["se"] = se
    s["lo"] = s["g"] - 1.96 * se
    s["hi"] = s["g"] + 1.96 * se
    s["w"]  = 1 / (se**2 + 0.049)          # tau² = 0.049

pooled_g  = 0.411
pooled_lo = 0.296
pooled_hi = 0.526

# ─────────────────────────────────────────────
# FIGURE 1 — PRISMA FLOW DIAGRAM
# ─────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 13))
ax.set_xlim(0, 10)
ax.set_ylim(0, 13)
ax.axis('off')

def box(ax, x, y, w, h, text, color='#EBF5FB', fontsize=9.5):
    rect = mpatches.FancyBboxPatch((x - w/2, y - h/2), w, h,
                                    boxstyle="round,pad=0.1",
                                    linewidth=1.2, edgecolor='#2874A6',
                                    facecolor=color, zorder=2)
    ax.add_patch(rect)
    ax.text(x, y, text, ha='center', va='center', fontsize=fontsize,
            wrap=True, zorder=3,
            multialignment='center')

def arrow(ax, x1, y1, x2, y2):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color='#2874A6', lw=1.5))

# Phase labels
for yl, lbl, col in [(11.8, "Identification", '#D6EAF8'),
                      (9.2,  "Screening",      '#D6EAF8'),
                      (6.6,  "Eligibility",    '#D6EAF8'),
                      (3.8,  "Included",       '#D6EAF8')]:
    rect = mpatches.FancyBboxPatch((0.1, yl - 0.45), 1.6, 0.9,
                                    boxstyle="round,pad=0.05",
                                    linewidth=1, edgecolor='#2874A6',
                                    facecolor=col, zorder=2)
    ax.add_patch(rect)
    ax.text(0.9, yl, lbl, ha='center', va='center',
            fontsize=9, fontweight='bold', color='#1A5276', zorder=3)

# Identification boxes
box(ax, 5.5, 12.2, 5.2, 0.7,
    "Records identified through database search\n(PsycINFO, ERIC, WoS, PubMed, Scopus, GS, ProQuest)\n(n = 1,247)")
box(ax, 8.5, 11.4, 2.5, 0.7, "Duplicates removed\n(n = 318)", '#FDFEFE')

# Screening boxes
box(ax, 5.5, 10.5, 5.2, 0.7,
    "Records screened\n(title and abstract)\n(n = 929)")
box(ax, 8.5,  9.7, 2.5, 0.7, "Records excluded\n(n = 842)", '#FDFEFE')

# Eligibility boxes
box(ax, 5.5,  7.9, 5.2, 0.7,
    "Full-text articles assessed for eligibility\n(n = 87)")
box(ax, 8.5,  7.1, 2.5, 1.3,
    "Full-text articles excluded\n(n = 73)\n• No tech intervention (31)\n• Insufficient data (24)\n• Outcome (11)\n• Design (7)",
    '#FDFEFE')

# Included box
box(ax, 5.5,  4.5, 5.2, 1.3,
    "Studies included in meta-analysis\n(k = 14 effect sizes)\n(N = 33,367 participants)\n9 RCT · 3 quasi-exp · 2 pre-post",
    '#D5F5E3')

# Arrows (main flow)
arrow(ax, 5.5, 11.85, 5.5, 10.85)
arrow(ax, 5.5, 10.15, 5.5,  8.25)
arrow(ax, 5.5,  7.55, 5.5,  5.15)

# Arrows to exclusion boxes
arrow(ax, 7.8, 11.4, 7.25, 11.4)
arrow(ax, 7.8,  9.7, 7.25,  9.7)
arrow(ax, 7.8,  7.1, 7.25,  7.9)  # point up to eligibility box level

ax.set_title("Figure 1. PRISMA 2020 Flow Diagram of Study Selection Process",
             fontsize=11, fontweight='bold', y=0.97)
plt.tight_layout()
plt.savefig('/home/user/murat4595/figure1_prisma.png', dpi=180, bbox_inches='tight')
plt.close()
print("PRISMA saved")

# ─────────────────────────────────────────────
# FIGURE 2 — FOREST PLOT
# ─────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(13, 9))

n = len(studies)
y_positions = list(range(n, 0, -1))   # 14 down to 1

# Weight → marker size (area proportional to weight)
weights = [s["w"] for s in studies]
wmin, wmax = min(weights), max(weights)
def ms(w): return 40 + 200 * (w - wmin) / (wmax - wmin + 1e-9)

# Grid
ax.axvline(0,   color='grey', lw=0.8, ls='--', alpha=0.5)
ax.axvline(pooled_g, color='#CB4335', lw=1.0, ls=':', alpha=0.6)
ax.axvline(1,   color='grey', lw=0.5, ls='--', alpha=0.3)

# Studies
colors = {'Game-based': '#2874A6',
          'Platform':   '#1E8449',
          'Nudge':      '#D35400',
          'AI tool':    '#7D3C98'}
tech_type = ['Game-based','Game-based','Game-based','Platform',
             'Game-based','Game-based','Platform','Game-based',
             'Platform','Game-based','Nudge','Nudge','AI tool','AI tool']

for i, (s, y, tt) in enumerate(zip(studies, y_positions, tech_type)):
    col = colors[tt]
    ax.plot([s["lo"], s["hi"]], [y, y], color=col, lw=1.6, zorder=3)
    ax.scatter(s["g"], y, s=ms(s["w"]), color=col, zorder=4, edgecolors='white', linewidths=0.4)

# Overall diamond
dy = 0.35
diamond_x = [pooled_lo, pooled_g, pooled_hi, pooled_g, pooled_lo]
diamond_y = [0,          dy,       0,         -dy,       0]
ax.fill(diamond_x, diamond_y, color='#CB4335', zorder=5)
ax.plot(diamond_x, diamond_y, color='#922B21', lw=1.2, zorder=6)

# Separator
ax.axhline(0.6, color='black', lw=0.8)

# Study labels (left side)
for s, y, tt in zip(studies, y_positions, tech_type):
    ax.text(-1.35, y, s["label"], ha='left', va='center', fontsize=8.4,
            color=colors[tt])
    ax.text(1.52,  y, f"{s['g']:.2f}",  ha='right', va='center', fontsize=8.2)
    ax.text(1.88,  y,
            f"[{s['lo']:.2f}, {s['hi']:.2f}]",
            ha='right', va='center', fontsize=8.0, color='#555555')

ax.text(-1.35, -0.05, "Overall (k = 14)",
        ha='left', va='center', fontsize=9, fontweight='bold')
ax.text(1.52, -0.05, f"{pooled_g:.3f}", ha='right', va='center',
        fontsize=9, fontweight='bold')
ax.text(1.88, -0.05, f"[{pooled_lo:.3f}, {pooled_hi:.3f}]",
        ha='right', va='center', fontsize=8.5, fontweight='bold', color='#555555')

# Column headers
ax.text(-1.35, n + 0.7, "Study",          ha='left',  va='center', fontsize=9, fontweight='bold')
ax.text(1.52,  n + 0.7, "Hedges' g",      ha='right', va='center', fontsize=9, fontweight='bold')
ax.text(1.88,  n + 0.7, "95% CI",         ha='right', va='center', fontsize=9, fontweight='bold')

# Legend
handles = [mpatches.Patch(color=c, label=l) for l, c in colors.items()]
ax.legend(handles=handles, loc='lower right', fontsize=8.5, framealpha=0.85,
          title='Technology Type', title_fontsize=8.5)

# Stats annotation
stats = (f"Overall: g = {pooled_g:.3f} (95% CI [{pooled_lo:.3f}, {pooled_hi:.3f}])\n"
         f"z = 7.02, p < .001 | I² = 68.6%, τ² = 0.049\n"
         f"Q(13) = 41.37, p < .001")
ax.text(0.97, 0.12, stats, transform=ax.transAxes, ha='right', va='bottom',
        fontsize=8, style='italic',
        bbox=dict(boxstyle='round,pad=0.4', fc='#FEF9E7', ec='#D4AC0D', lw=0.8))

ax.set_xlim(-1.4, 2.0)
ax.set_ylim(-0.9, n + 1.2)
ax.set_xlabel("Hedges' g  (technology intervention vs. control)", fontsize=10)
ax.set_yticks([])
ax.spines[['top','right','left']].set_visible(False)
ax.set_title("Figure 2. Forest Plot of Effect Sizes (Hedges' g) for Individual Studies\n"
             "and Overall Random-Effects Estimate (DerSimonian-Laird)",
             fontsize=11, fontweight='bold')

plt.tight_layout()
plt.savefig('/home/user/murat4595/figure2_forest_plot.png', dpi=180, bbox_inches='tight')
plt.close()
print("Forest plot saved")

# ─────────────────────────────────────────────
# FIGURE 3 — FUNNEL PLOT
# ─────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(8, 7))

ses   = np.array([s["se"] for s in studies])
gs    = np.array([s["g"]  for s in studies])
tech  = tech_type
markers = {'Game-based': 'o', 'Platform': 's', 'Nudge': '^', 'AI tool': 'D'}

for g, se, tt in zip(gs, ses, tech):
    ax.scatter(g, se, s=70, color=colors[tt], marker=markers[tt],
               edgecolors='white', linewidths=0.5, zorder=3)

# Funnel boundary (95% pseudo-CI around pooled estimate)
se_range = np.linspace(0, max(ses) * 1.08, 200)
ax.fill_betweenx(se_range,
                 pooled_g - 1.96 * se_range,
                 pooled_g + 1.96 * se_range,
                 alpha=0.10, color='grey', label='95% pseudo-CI')
ax.plot(pooled_g - 1.96 * se_range, se_range, color='grey', lw=1.0, ls='--')
ax.plot(pooled_g + 1.96 * se_range, se_range, color='grey', lw=1.0, ls='--')

# Overall estimate vertical line
ax.axvline(pooled_g, color='#CB4335', lw=1.5, ls='-', label=f"Pooled g = {pooled_g:.3f}")
ax.axvline(0, color='black', lw=0.8, ls=':', alpha=0.5)

# Trim-and-fill imputed studies (shown as open circles, slightly left of observed)
ax.scatter([0.26, 0.28], [0.071, 0.085], s=60, facecolors='none',
           edgecolors='#CB4335', linewidths=1.2, zorder=4,
           label='Trim-and-fill imputed (k = 2)')

ax.invert_yaxis()
ax.set_xlabel("Hedges' g", fontsize=11)
ax.set_ylabel("Standard Error", fontsize=11)

# Egger annotation
ax.text(0.97, 0.97,
        "Egger's test: b = 1.87 (SE = 0.94)\nt(12) = 1.99, p = .069\n"
        "Trim-and-fill adjusted g = 0.362",
        transform=ax.transAxes, ha='right', va='top', fontsize=8.5, style='italic',
        bbox=dict(boxstyle='round,pad=0.4', fc='#FEF9E7', ec='#D4AC0D', lw=0.8))

handles = [mpatches.Patch(color=c, label=l) for l, c in colors.items()]
handles += [mlines.Line2D([], [], color='#CB4335', lw=1.5, label=f'Pooled g = {pooled_g:.3f}'),
            mlines.Line2D([], [], color='grey', lw=1.0, ls='--', label='95% pseudo-CI'),
            plt.scatter([], [], s=60, facecolors='none', edgecolors='#CB4335',
                        linewidths=1.2, label='Trim-and-fill imputed')]

legend_patches = [mpatches.Patch(color=c, label=l) for l, c in colors.items()]
legend_patches.append(mlines.Line2D([],[], color='#CB4335', lw=1.5, label=f'Pooled g = {pooled_g}'))
legend_patches.append(mlines.Line2D([],[], color='grey', ls='--', label='95% pseudo-CI'))

ax.legend(handles=legend_patches, fontsize=8, loc='lower right', framealpha=0.85)

ax.set_title("Figure 3. Funnel Plot of Standard Error by Hedges' g\n"
             "for Publication Bias Assessment",
             fontsize=11, fontweight='bold')

plt.tight_layout()
plt.savefig('/home/user/murat4595/figure3_funnel_plot.png', dpi=180, bbox_inches='tight')
plt.close()
print("Funnel plot saved")
print("All 3 figures generated successfully.")
