import requests, json, time, sys

refs = [
    # (key, display_citation, doi_or_None)
    ("ali2023",      "Ali & Qazi (2023) – J Dev Econ",                "10.1016/j.jdeveco.2023.103100"),
    ("axelsson2024", "Axelsson et al. (2024) – JRTE",                  "10.1080/15391523.2024.2338451"),
    ("basol2020",    "Basol et al. (2020) – J Cognition",              "10.5334/joc.91"),
    ("becker2005",   "Becker (2005) – book chapter",                   None),
    ("borenstein2009","Borenstein et al. (2009) – book",               "10.1002/9780470743386"),
    ("breakstone2019","Breakstone et al. (2019) – Social Education",   None),
    ("butler2024",   "Butler et al. (2024) – Sci Reports",             "10.1038/s41598-024-62286-7"),
    ("cohen1988",    "Cohen (1988) – book",                            None),
    ("dersimonian1986","DerSimonian & Laird (1986) – Controlled Clin", "10.1016/0197-2456(86)90046-2"),
    ("duval2000",    "Duval & Tweedie (2000) – Biometrics",            "10.1111/j.0006-341X.2000.00455.x"),
    ("egger1997",    "Egger et al. (1997) – BMJ",                      "10.1136/bmj.315.7109.629"),
    ("ennis1989",    "Ennis (1989) – Educ Researcher",                 None),
    ("facione1990",  "Facione (1990) – Delphi Report",                 None),
    ("guess2020",    "Guess et al. (2020) – PNAS",                     "10.1073/pnas.1920498117"),
    ("higgins2003",  "Higgins et al. (2003) – BMJ",                    "10.1136/bmj.327.7414.557"),
    ("hobbs2010",    "Hobbs (2010) – Aspen Institute",                 None),
    ("huang2024",    "Huang, Jia & Yu (2024) – Commun Res",            "10.1177/00936502241288103"),
    ("hu2023",       "Hu et al. (2023) – Cogn Res P&I",               "10.1186/s41235-023-00505-x"),
    ("hwang2025",    "Hwang & Jeong (2025) – Cyberpsychol",            "10.1089/cyber.2024.0407"),
    ("lebowitz2024", "Lebowitz et al. (2024) – arXiv",                 None),   # preprint, no DOI yet
    ("lu2024",       "Lu et al. (2024) – Cyberpsychol B&SN",           "10.1089/cyber.2023.0324"),
    ("lu2023",       "Lu et al. (2023) – JMIR",                        "10.2196/49255"),
    ("mayer2021",    "Mayer (2021) – book",                            None),
    ("mcgrew2020",   "McGrew et al. (2020) – Social Education",        None),
    ("mcguire1964",  "McGuire (1964) – Adv Exp Soc Psych",             None),
    ("moore2022",    "Moore & Hancock (2022) – Sci Reports",           "10.1038/s41598-022-08437-0"),
    ("page2021",     "Page et al. (2021) – BMJ (PRISMA 2020)",         "10.1136/bmj.n71"),
    ("pennycook2020ps","Pennycook et al. (2020) – Psychol Sci",        "10.1177/0956797620939054"),
    ("pennycook2019","Pennycook & Rand (2019) – Cognition",            "10.1016/j.cognition.2019.03.011"),
    ("pennycook2021","Pennycook & Rand (2021) – Trends Cogn Sci",      "10.1016/j.tics.2021.02.007"),
    ("pennycook2022","Pennycook & Rand (2022) – Nat Commun",           "10.1038/s41467-022-30073-5"),
    ("roozenbeek2019","Roozenbeek & van der Linden (2019) – HSSCOMM",  "10.1057/s41599-019-0279-9"),
    ("roozenbeek2020","Roozenbeek et al. (2020) – HKS MisinfoRev",     "10.37016/mr-2020-008"),
    ("roozenbeek2021","Roozenbeek et al. (2021) – HKS MisinfoRev",     "10.37016/mr-2020-47"),
    ("roozenbeek2022rsos","Roozenbeek et al. (2022) – Royal Soc Open Sci","10.1098/rsos.211719"),
    ("roozenbeek2022sa","Roozenbeek et al. (2022) – Sci Advances",     "10.1126/sciadv.abo6254"),
    ("roozenbeek2023","Roozenbeek et al. (2023) – Eur Psychol",        "10.1027/1016-9040/a000492"),
    ("rosenthal1979","Rosenthal (1979) – Psychol Bull",                "10.1037/0033-2909.86.3.638"),
    ("simchon2025",  "Simchon et al. (2025) – Curr Opin Psychol",      "10.1016/j.copsyc.2025.102194"),
    ("stasielowicz2026","Stasielowicz (2026) – Eur J Soc Psychol",     "10.1002/ejsp.70041"),
    ("sultan2024",   "Sultan et al. (2024) – PNAS",                    "10.1073/pnas.2409329121"),
    ("vanderlinden2023","van der Linden (2023) – book",                None),
    ("vosoughi2018", "Vosoughi, Roy & Aral (2018) – Science",          "10.1126/science.aap9559"),
]

HEADERS = {"User-Agent": "MetaAnalysisRefCheck/1.0 (mailto:murat4595@gmail.com)"}
BASE = "https://api.crossref.org/works/"

results = []
print(f"{'#':<3} {'STATUS':<10} {'TYPE':<12} {'CITATION'}")
print("-" * 80)

for i, (key, citation, doi) in enumerate(refs, 1):
    if doi is None:
        results.append({"key": key, "citation": citation, "doi": None,
                        "status": "NO_DOI", "title": "N/A (book/report/preprint)",
                        "crossref_title": None, "year_ok": None, "match": None})
        print(f"{i:<3} {'NO_DOI':<10} {'no DOI':<12} {citation}")
        continue

    try:
        r = requests.get(BASE + doi, headers=HEADERS, timeout=15)
        time.sleep(0.3)  # polite delay
        if r.status_code == 200:
            data = r.json()["message"]
            cr_title = data.get("title", [""])[0] if data.get("title") else ""
            cr_year  = (data.get("published-print") or data.get("published-online") or {})
            cr_year  = cr_year.get("date-parts", [[None]])[0][0]
            cr_type  = data.get("type", "")
            results.append({"key": key, "citation": citation, "doi": doi,
                            "status": "VERIFIED", "title": cr_title,
                            "crossref_title": cr_title, "year": cr_year,
                            "type": cr_type, "match": True})
            print(f"{i:<3} {'✅ VERIFIED':<10} {str(cr_type)[:12]:<12} {citation}")
            print(f"    CrossRef title: {cr_title[:90]}")
        elif r.status_code == 404:
            results.append({"key": key, "citation": citation, "doi": doi,
                            "status": "NOT_FOUND", "title": None, "match": False})
            print(f"{i:<3} {'❌ NOT FOUND':<10} {'404':<12} {citation}  DOI: {doi}")
        else:
            results.append({"key": key, "citation": citation, "doi": doi,
                            "status": f"HTTP_{r.status_code}", "match": None})
            print(f"{i:<3} {'⚠ HTTP '+str(r.status_code):<10} {'':<12} {citation}")
    except Exception as e:
        results.append({"key": key, "citation": citation, "doi": doi,
                        "status": "ERROR", "error": str(e), "match": None})
        print(f"{i:<3} {'⚠ ERROR':<10} {'':<12} {citation}  [{e}]")

# Summary
verified  = [r for r in results if r["status"] == "VERIFIED"]
not_found = [r for r in results if r["status"] == "NOT_FOUND"]
no_doi    = [r for r in results if r["status"] == "NO_DOI"]
errors    = [r for r in results if r["status"] not in ("VERIFIED","NOT_FOUND","NO_DOI")]

print("\n" + "=" * 80)
print(f"CROSSREF VERIFICATION SUMMARY")
print(f"  Total references   : {len(refs)}")
print(f"  ✅ DOI verified    : {len(verified)}")
print(f"  ❌ DOI not found   : {len(not_found)}")
print(f"  📚 No DOI (books)  : {len(no_doi)}")
print(f"  ⚠  Errors/other   : {len(errors)}")
print(f"  Verification rate  : {100*len(verified)/(len(refs)-len(no_doi)):.1f}% (of citable refs)")
print("=" * 80)

if not_found:
    print("\nREFERENCES REQUIRING ATTENTION (DOI not found in CrossRef):")
    for r in not_found:
        print(f"  • {r['citation']}  —  DOI: {r['doi']}")

with open("/home/user/murat4595/crossref_results.json", "w") as f:
    json.dump(results, f, indent=2, default=str)
print("\nFull results saved to crossref_results.json")
