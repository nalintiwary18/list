import json

with open("companies_data.json", "r", encoding="utf-8") as f:
    comps = json.load(f)

with open("scripts/live_audit_results.json", "r", encoding="utf-8") as f:
    audit_data = json.load(f)

audit_map = {a["id"]: a for a in audit_data}

# Categorize issues:
# Category A: Dead / 404 / DNS failure / Timeout
# Category B: Acquired or Merged or Redirected to unrelated domain
# Category C: Headcount > 100 or Late Stage (Series C+ / Growth / Unicorn / 200+ employees)
# Category D: Completely Non-Tech / Non-AI (Pathology, consumer retail, bikes, pads, etc.)
# Category E: Duplicates
# Category F: US-only without India hiring / payroll

issues = []

# List of known companies exceeding 100 employees or Series C+
oversized_or_late = {
    "Cashify", "Cogoport", "Wingify (VWO)", "Keka HR", "Awign", "SquadStack", "Fleetx.io",
    "Baaz Bikes", "Revfin", "Infeedo", "Toddle", "AdmitKard", "Bijak", "BeatO", "Redcliffe Labs",
    "Uolo", "ConveGenius", "Filo", "Unstop", "Instahyre", "Leena AI", "HROne", "Fyle",
    "Pepper Content", "FloBiz (myBillBook)", "Soothe Healthcare", "Otipy (Crofarm)", "River Mobility",
    "Turno", "Credgenics", "Ultrahuman", "Sugar.fit", "Orange Health", "Doceree", "ClaimBuddy",
    "Fitelo", "Fitterfly", "Rooter", "Kutumb", "Stage", "Bolo Live", "Khabri", "STAN",
    "Karbon Card", "Loop Health", "Onsurity", "Nova Benefits", "Uni Cards", "Pazcare",
    "SuperOps", "Sprinto", "Rocketlane", "Appsmith", "Vahan.ai", "Toplyne", "CustomerGlu",
    "BluSmart", "Agri10x", "Blend", "Defer.run", "Vance"
}

# Known acquired / merged
acquired_or_rebranded = {
    "Chaos Genius": "Acquired by Flexera",
    "Houseware": "Shut down (2024)",
    "Bikayi": "Shut down / pivot to BIK",
    "PerSapien": "Shut down",
    "Tune AI": "Domain dead",
    "Wurkr": "Domain dead",
    "Leaf Round": "Domain dead",
    "Sprih": "Domain dead",
    "MonsterAPI": "Domain dead",
    "Dyte": "Acquired by Cloudflare",
    "Cacheflow": "Acquired by HubSpot",
    "Togai": "Acquired by Zuora",
    "Protect AI": "Acquired by Palo Alto Networks",
    "Memfold AI": "Redirects to alma.inc",
    "Invoid": "Acquired by Bureau",
    "Highlight.io": "Acquired by LaunchDarkly",
    "Codeium": "Rebranded to Windsurf, >150 people",
    "Zevi.ai": "Acquired by CaratLane",
    "Senseforth.ai": "Acquired by Fractal",
    "Ritivel": "Rebranded to TensorTest (tensortest.com)",
    "GigaML": "Website moved to giga.ai",
    "Questera (Quest Labs)": "Duplicate of Quest Labs (questera.ai)",
    "Quest Labs": "Duplicate of Questera",
    "SuperKalam": "Website moved to superkalam.com",
    "Dozee": "Website moved to dozeehealth.ai",
    "Wysa": "Website moved to wysa.com",
    "NeuralGarage": "Website moved to visualdub.ai"
}

for c in comps:
    cid = c["id"]
    name = c["company_name"]
    audit = audit_map.get(cid, {})
    w_check = audit.get("website_check", {})
    code = w_check.get("code")
    err = w_check.get("error", "")
    final_url = w_check.get("final_url", "")
    host_changed = w_check.get("host_changed", False)
    
    # 1. Acquired / Rebranded
    for acq_name, detail in acquired_or_rebranded.items():
        if acq_name.lower() in name.lower():
            issues.append((cid, name, "Acquired/Rebranded/Dead", detail))
            break
            
    # 2. Oversized / Late stage
    for over_name in oversized_or_late:
        if over_name.lower() in name.lower() and not any(i[0] == cid for i in issues):
            issues.append((cid, name, "Oversized/LateStage", f">100 employees or Series C+"))
            break
            
    # 3. Dead website / DNS failure
    if not any(i[0] == cid for i in issues):
        if code == 404:
            issues.append((cid, name, "DeadWebsite", f"HTTP 404 Not Found ({c['website']})"))
        elif "getaddrinfo failed" in err:
            issues.append((cid, name, "DeadWebsite", f"DNS Failure ({c['website']})"))
        elif host_changed and ("flexera.com" in final_url or "notion.site" in final_url):
            issues.append((cid, name, "AcquiredOrShutDown", f"Redirected to {final_url}"))

print(f"Total flagged issues in current dataset: {len(issues)}")
for cid, name, category, reason in issues:
    print(f"[{cid:3d}] {name:<30} | {category:<22} | {reason}")
