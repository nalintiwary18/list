import json

# Load existing companies
with open("companies_data.json", "r", encoding="utf-8") as f:
    comps = json.load(f)

# Load the disqualified set
from check_more_disqualified import all_disqualified

print(f"Total disqualified: {len(all_disqualified)}")
for cid, reason in sorted(all_disqualified.items()):
    c = comps[cid-1]
    print(f"[{cid:3d}] {c['company_name']:<28} | Reason: {reason}")
