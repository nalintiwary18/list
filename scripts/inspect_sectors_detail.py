import json

with open("companies_data.json", "r", encoding="utf-8") as f:
    comps = json.load(f)

# List of known safe and active startups
# Let's inspect remaining companies and print their company_name, domain_sector, employee_count
for c in comps:
    name = c["company_name"]
    sec = c["domain_sector"]
    emp = c["employee_count"]
    fund = c["funding_stage_investors"]
    # Check if any have large funding or suspicious sector
    if any(k in sec.lower() for k in ['logistic', 'hospital', 'health', 'finance', 'ev ', 'mobility', 'agri', 'hr', 'legal']):
        print(f"[{c['id']:3d}] {name:<25} | {sec:<35} | {emp:<8} | {fund[:30]}")
