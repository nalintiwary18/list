import json
with open("companies_data.json", "r", encoding="utf-8") as f:
    comps = json.load(f)

for c in comps:
    if "kello" in c["company_name"].lower():
        print(c["id"], c["company_name"], c["website"])
