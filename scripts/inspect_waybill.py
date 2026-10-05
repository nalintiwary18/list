import json

with open("companies_data.json", "r", encoding="utf-8") as f:
    comps = json.load(f)

for c in comps:
    if c["company_name"] == "Waybill":
        print(json.dumps(c, indent=2))
