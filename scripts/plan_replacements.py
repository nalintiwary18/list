import json

with open("companies_data.json", "r", encoding="utf-8") as f:
    comps = json.load(f)

with open("scripts/live_audit_results.json", "r", encoding="utf-8") as f:
    audit_data = json.load(f)

audit_map = {a["id"]: a for a in audit_data}

# Disqualification criteria:
# 1. Dead / 404 / DNS failure / Spam
# 2. Acquired / Shut down
# 3. Headcount > 100 or Late Stage (Series C+, Unicorn, mature 300+ people)
# 4. Non-tech / Offline physical businesses (pathology labs, sanitary pads, electric scooters, hospital TPA, used phones)
# 5. Duplicate records

disqualified_ids = {
    # Acquired / Shut down / Dead / Spam
    24: "Houseware - Shut down (2024)",
    25: "Chaos Genius - Acquired by Flexera",
    38: "Tune AI - Domain dead / inactive",
    99: "PerSapien - Shut down (404)",
    141: "Shyplite - DNS failure / dead domain",
    167: "Bikayi - Shut down / pivot memo",
    201: "Leaf Round - Domain dead",
    217: "Charzer - DNS failure / dead domain",
    220: "Sprih - Domain dead",
    224: "Zevi.ai - Acquired by CaratLane",
    239: "Senseforth.ai - Acquired by Fractal",
    263: "Bik.ai - 404 dead domain",
    298: "MonsterAPI - Domain dead / unmaintained",
    337: "Wurkr - Domain dead",
    339: "Quest Labs - Duplicate of ID 11 (Questera)",
    341: "Maya AI - DNS dead (cselect.ai)",
    
    # Non-responsive / dead / non-software
    19: "Slang Labs - SSL handshake alert / dead",
    47: "Kindling - No public product site / US storytelling",
    115: "CogniSaaS - SSL internal failure",
    222: "Digantara - Spacetech hardware & satellites",
    223: "Headfone - Audio podcast / timeout",
    347: "Spry - Timeout / non-responsive",

    # Oversized (>100 to 2000+) or Late Stage / Mature
    62: "Toddle - K-12 LMS, 200+ employees",
    63: "Infeedo - Amber chatbot, 150+ employees",
    64: "AdmitKard - Study abroad consultancy, 200+ employees",
    65: "Fleetx.io - Fleet IoT, 250+ employees, Series B",
    66: "Bijak - Agri B2B trading, 200+ employees",
    67: "BeatO - Diabetes devices/app, 200+ employees",
    68: "Redcliffe Labs - Diagnostic pathology labs, 2,000+ employees, Series C",
    70: "Uolo - Edtech school app, 300+ employees",
    71: "ConveGenius - Govt edtech, 250+ employees",
    72: "Filo - Tutoring marketplace, 200+ employees",
    73: "Unstop - Student competition platform, 150+ employees",
    74: "Instahyre - Job board SaaS, 150+ employees",
    76: "Leena AI - Enterprise HR AI, 250+ employees, Series B $30M",
    77: "HROne - Enterprise HRMS, 200+ employees",
    89: "Wingify (VWO) - Mature bootstrapped, 300+ employees",
    90: "SquadStack - Tele-sales BPO, 250+ employees",
    92: "Baaz Bikes - EV bike hardware, non-AI",
    93: "Revfin - EV financing / NBFC, non-AI",
    110: "Appsmith - Low-code internal tools, 150+ employees, Series B",
    119: "SuperOps - IT management SaaS, 150+ employees, Series B",
    120: "Rocketlane - Client onboarding SaaS, 150+ employees, Series B $24M",
    121: "Sprinto - Compliance automation, 200+ employees, Series B $20M",
    134: "Pando - Supply chain control tower, 150+ employees, Series B $30M",
    137: "Cogoport - Freight logistics, 1,000+ employees, Series B $50M+",
    143: "Vakilsearch (Zolvit) - Legal consultation BPO, 500+ employees",
    144: "IndiaFilings - Legal tax filing BPO, 500+ employees",
    148: "Fyle - Expense management, 150+ employees, Series B $30M",
    152: "Springworks - HR SaaS tools, 150+ employees",
    153: "Keka HR - HRMS software, 600+ employees, Series A $57M",
    158: "Karbon Card - Corporate credit cards, 100+ employees",
    160: "Plum Benefits - Group health insurance broker, 250+ employees",
    161: "Loop Health - Health insurance broker, 200+ employees",
    162: "Onsurity - SME health insurance, 200+ employees",
    163: "Pazcare - Employee insurance broker, 150+ employees",
    164: "Nova Benefits - Corporate wellness broker, 150+ employees",
    169: "Vahan.ai - Gig worker recruitment, 150+ employees, Series A",
    174: "Uni Cards - Fintech credit cards, 200+ employees",
    186: "FloBiz (myBillBook) - SME billing, 300+ employees, Series B $31M",
    187: "Pepper Content - Content marketplace, 200+ employees",
    189: "Awign - Gig workforce, 400+ employees, Series B",
    197: "Battery Smart - Two-wheeler EV battery swapping, 500+ employees",
    198: "Cashify - Re-commerce, 1,500+ employees, Series E",
    199: "Soothe Healthcare - Paree sanitary pads, 500+ employees, non-tech",
    200: "Pee Safe - Hygiene products & pads, non-tech",
    207: "Turno - Commercial EV financing, 200+ employees",
    229: "Ergos - Grain warehousing B2B, 150+ employees",
    230: "Gramophone - Agri input marketplace, 200+ employees",
    255: "Stanplus (Red.Health) - Ambulance & emergency response, 500+ employees",
    256: "Otipy (Crofarm) - Fresh grocery delivery, 500+ employees",
    257: "Agrim - B2B Agri marketplace, 150+ employees",
    259: "Locad - Logistics warehousing, 150+ employees",
    268: "Biddano - Pharma distribution, 150+ employees",
    282: "VoltUp - EV battery swapping stations, hardware",
    284: "Statiq - EV charging stations, hardware",
    285: "River Mobility - Electric scooter hardware, 300+ employees, Series B $40M",
    293: "Everstage - Sales commission software, 200+ employees, Series B $30M",
    303: "Credgenics - Debt recovery SaaS, 300+ employees, Series B $50M",
    306: "HexaHealth - Surgery hospital concierge, 200+ employees",
    310: "Curebay - Rural healthcare physical clinics",
    311: "Ultrahuman - Hardware smart rings, 200+ employees, Series B $35M",
    312: "Sugar.fit - Diabetes clinic/health, 150+ employees",
    313: "Orange Health - Blood diagnostic labs, 300+ employees",
    314: "Doceree - Pharma ad network, 150+ employees, Series B $35M",
    315: "ClaimBuddy - Hospital insurance processing, 150+ employees",
    317: "Clinikk - Outpatient physical clinics",
    318: "Fitelo - Dieticians app, 200+ employees",
    319: "Fitterfly - Metabolic health clinics, 150+ employees",
    321: "Stage - Regional OTT video, 150+ employees",
    322: "Bolo Live - Live streaming, 100+ employees",
    323: "Khabri - Audio podcast, 100+ employees",
    324: "STAN - Gaming community, 100+ employees",
    325: "Rooter - Gaming streaming, 200+ employees",
    326: "Kutumb - Community app, 200+ employees",
}

print(f"Total disqualified: {len(disqualified_ids)}")
print(f"Total retained: {len(comps) - len(disqualified_ids)}")
