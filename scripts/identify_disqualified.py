import json

with open("companies_data.json", "r", encoding="utf-8") as f:
    comps = json.load(f)

with open("scripts/live_audit_results.json", "r", encoding="utf-8") as f:
    audit_data = json.load(f)

audit_map = {a["id"]: a for a in audit_data}

# Known lists from industry analysis & prompt
disqualified_companies = {}

# 1. Flagged in prompt / known dead / squatted / acquired / merged / rebranded to acquirer
manual_flags = {
    # Acquired / Shut down
    "Chaos Genius": "Acquired by Flexera",
    "Houseware": "Shut down (2024)",
    "Bikayi": "Shut down / pivot to BIK",
    "PerSapien": "Shut down",
    "Tune AI": "Domain dead / inactive",
    "Wurkr": "Domain dead",
    "Leaf Round": "Domain dead",
    "Sprih": "Domain dead",
    "MonsterAPI": "Domain dead / unmaintained",
    "Dyte": "Acquired by Cloudflare",
    "Cacheflow": "Acquired by HubSpot",
    "Togai": "Acquired by Zuora",
    "Protect AI": "Acquired by Palo Alto Networks",
    "Memfold AI": "Redirects to alma.inc (acq/pivot)",
    "Invoid": "Acquired by Bureau",
    "Highlight.io": "Acquired by LaunchDarkly",
    "Codeium": "Rebranded to Windsurf/Cognition; >150 people",
    "Zevi.ai": "Acquired by CaratLane",
    "Senseforth.ai": "Acquired by Fractal",
    
    # Dead / Squatted / Spam from prompt & audit
    "Agri10x": "Gambling spam redirect",
    "Blend": "Domain squatted (HugeDomains)",
    "Defer.run": "Dead domain",
    "Vance": "Dead domain",
    "Toplyne": "Shut down / dead domain",
    "CustomerGlu": "Dead domain / 404",
    "BluSmart": "Mobility ride-hailing, 1000+ staff, dead/broken career page",
    "Shyplite": "DNS dead",
    "Charzer": "DNS dead",
    "Bik.ai": "HTTP 404 dead",
    "Maya AI": "DNS dead (cselect.ai)",

    # Massive headcount (>100 to 2000+) or Late Stage / Unicorn
    "Cashify": "Re-commerce, 1,500+ employees, Series E",
    "Cogoport": "Freight logistics, 1,000+ employees, Series B $50M+",
    "Redcliffe Labs": "Diagnostic labs, 2,000+ employees, Series C",
    "Wingify (VWO)": "Mature bootstrapped, 300+ employees",
    "Keka HR": "HRMS software, 600+ employees, Series A $57M",
    "Awign": "Gig workforce, 400+ employees, Series B",
    "SquadStack": "Tele-sales BPO, 250+ employees",
    "Fleetx.io": "Fleet IoT, 250+ employees, Series B",
    "Baaz Bikes": "EV bike hardware, non-AI",
    "Revfin": "EV financing / NBFC, non-AI",
    "Infeedo": "Amber chatbot, 150+ employees, 10+ yrs old",
    "Toddle": "K-12 LMS, 200+ employees, Series A $17M",
    "AdmitKard": "Study abroad agency, 200+ employees",
    "Bijak": "Agri B2B trading, 200+ employees",
    "BeatO": "Diabetes devices/app, 200+ employees",
    "Uolo": "Edtech school app, 300+ employees",
    "ConveGenius": "Govt edtech, 250+ employees",
    "Filo": "Tutoring marketplace, 200+ employees",
    "Unstop": "Student competition platform, 150+ employees",
    "Instahyre": "Job board SaaS, 150+ employees",
    "Leena AI": "Enterprise HR AI, 250+ employees, Series B $30M",
    "HROne": "Enterprise HRMS, 200+ employees",
    "Fyle": "Expense management, 150+ employees, Series B $30M",
    "Pepper Content": "Content marketplace, 200+ employees",
    "FloBiz (myBillBook)": "SME billing, 300+ employees, Series B $31M",
    "Soothe Healthcare": "Paree sanitary pads, 500+ employees, non-tech",
    "Otipy (Crofarm)": "Fresh grocery delivery, 500+ employees",
    "River Mobility": "Electric scooter hardware, 300+ employees, Series B $40M",
    "Turno": "Commercial EV financing, 200+ employees",
    "Credgenics": "Debt recovery SaaS, 300+ employees, Series B $50M",
    "Ultrahuman": "Hardware smart rings, 200+ employees, Series B $35M",
    "Sugar.fit": "Diabetes clinic/health, 150+ employees",
    "Orange Health": "Blood diagnostic labs, 300+ employees",
    "Doceree": "Pharma ad network, 150+ employees, Series B $35M",
    "ClaimBuddy": "Hospital insurance processing, 150+ employees",
    "Fitelo": "Dieticians app, 200+ employees",
    "Fitterfly": "Metabolic health clinics, 150+ employees",
    "Rooter": "Gaming streaming, 200+ employees",
    "Kutumb": "Community app, 200+ employees",
    "Stage": "Regional OTT video, 150+ employees",
    "Bolo Live": "Live streaming, 100+ employees",
    "Khabri": "Audio podcast, 100+ employees",
    "STAN": "Gaming community, 100+ employees",
    "Karbon Card": "Corporate credit cards, 100+ employees",
    "Loop Health": "Health insurance broker, 200+ employees",
    "Onsurity": "SME health insurance, 200+ employees",
    "Nova Benefits": "Corporate wellness broker, 150+ employees",
    "Uni Cards": "Fintech credit cards, 200+ employees",
    "Pazcare": "Employee insurance broker, 150+ employees",
    "SuperOps": "IT management SaaS, 150+ employees, Series B",
    "Sprinto": "Compliance automation, 200+ employees, Series B $20M",
    "Rocketlane": "Client onboarding SaaS, 150+ employees, Series B $24M",
    "Appsmith": "Low-code internal tools, 150+ employees, Series B",
    "Vahan.ai": "Gig worker recruitment, 150+ employees, Series A",
    "Stanplus (Red.Health)": "Ambulance emergency response, 500+ employees",
    "Everstage": "Sales commission software, 200+ employees, Series B $30M",
    "Beatoven.ai": "Music AI, restructured/small but check status",

    # Duplicates:
    "Quest Labs": "Duplicate of Questera (Quest Labs)"
}

to_replace = []
to_update = []

for c in comps:
    cid = c["id"]
    name = c["company_name"]
    audit = audit_map.get(cid, {})
    w_check = audit.get("website_check", {})
    code = w_check.get("code")
    err = w_check.get("error", "")
    final_url = w_check.get("final_url", "")

    # Check if in manual flags
    matched = None
    for flag_name, reason in manual_flags.items():
        if flag_name.lower() in name.lower() or name.lower() in flag_name.lower():
            matched = (flag_name, reason)
            break
            
    if matched:
        to_replace.append((cid, name, matched[1]))
    elif code == 404:
        to_replace.append((cid, name, f"HTTP 404 dead domain: {c['website']}"))
    elif "getaddrinfo failed" in err:
        to_replace.append((cid, name, f"DNS resolution failed: {c['website']}"))
    elif "flexera.com" in final_url or "notion.site/bikayi" in final_url or "pemudatogel" in final_url:
        to_replace.append((cid, name, f"Redirected to acquirer/spam: {final_url}"))

print(f"Total companies to replace: {len(to_replace)}")
for item in to_replace:
    print(f"[{item[0]:3d}] {item[1]:<30} | {item[2]}")
