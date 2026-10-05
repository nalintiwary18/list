import json

with open("companies_data.json", "r", encoding="utf-8") as f:
    comps = json.load(f)

from plan_replacements import disqualified_ids

more_disqualified = {
    88: "Restroworks (Posist) - 250+ employees",
    136: "Wiz Freight - 300+ employees freight forwarding",
    175: "Freo (MoneyTap) - 300+ employees consumer lending",
    176: "CASHe - 400+ employees consumer lending NBFC",
    181: "IndiaLends - 300+ employees loan aggregator",
    190: "WorkIndia - 200+ employees blue-collar job portal",
    192: "Newton School - 200+ employees edtech",
    193: "Masai School - 200+ employees edtech",
    195: "Teachmint - 300+ employees edtech ($78M raised)",
    196: "Stashfin - 500+ employees lending NBFC",
    216: "Stellapps Technologies - 200+ employees dairy IoT",
    260: "Increff - 200+ employees inventory SaaS",
    266: "CityMall - 500+ employees social commerce",
}

all_disqualified = dict(disqualified_ids)
all_disqualified.update(more_disqualified)

print(f"Total disqualified now: {len(all_disqualified)}")
print(f"Total retained: {len(comps) - len(all_disqualified)}")

retained = [c for c in comps if c["id"] not in all_disqualified]

# Print remaining companies with funding or stage > Series B
for c in retained:
    f = c["funding_stage_investors"]
    name = c["company_name"]
    if "Series C" in f or "Series D" in f or "Unicorn" in f or "IPO" in f:
        print(f"Late stage: [{c['id']:3d}] {name:<25} | {f}")
