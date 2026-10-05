import json

with open("companies_data.json", "r", encoding="utf-8") as f:
    comps = json.load(f)

# Load disqualified ids from plan_replacements
from plan_replacements import disqualified_ids

retained = [c for c in comps if c["id"] not in disqualified_ids]
print(f"Retained count: {len(retained)}")

# Check for any remaining suspicious names or high employee counts
for c in retained:
    name = c["company_name"]
    emp = c["employee_count"]
    fund = c["funding_stage_investors"]
    # Check if employee count text says anything > 100
    if any(x in emp for x in ['100', '150', '200', '300', '400', '500']):
        print(f"Watch employee count: [{c['id']:3d}] {name:<25} | {emp:<10} | {fund}")
