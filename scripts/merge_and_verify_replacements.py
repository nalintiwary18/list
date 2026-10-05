import json
from create_replacements_batch1 import replacements_list
from create_replacements_batch2 import batch2_list

# Update Truffle AI in batch 1 if needed
for i, r in enumerate(replacements_list):
    if r["company_name"].lower() == "kello":
        replacements_list[i] = {
            "company_name": "Truffle AI",
            "website": "https://trufflehq.com",
            "domain_sector": "AI-Native Code Search & Context Engine for Developer Tools",
            "employee_count": "6-14",
            "funding_stage_investors": "Seed $1.2M (prominent devtool angels)",
            "work_model_location": "Fully Remote (India) / Bengaluru",
            "career_page_url": "https://trufflehq.com",
            "career_email": "apoorv@trufflehq.com",
            "hiring_decision_maker": "Apoorv Saxena (Founder & CEO)",
            "nalin_tech_fit_hook": "Building semantic code indexers and AST token trees for developer copilots, directly matching Nalin's Code Sage AST audit engine.",
            "outreach_status": "To Contact"
        }

all_replacements = replacements_list + batch2_list
print(f"Total replacements available: {len(all_replacements)}")

# Check duplicate names within replacements
rep_names = [r["company_name"].strip().casefold() for r in all_replacements]
if len(rep_names) != len(set(rep_names)):
    print("ERROR: Duplicate names found inside replacements!")
    dupes = [name for name in rep_names if rep_names.count(name) > 1]
    print(f"Duplicates: {set(dupes)}")
else:
    print("SUCCESS: All 108 replacement names are unique within the replacement set.")

# Check overlap with retained companies
with open("companies_data.json", "r", encoding="utf-8") as f:
    comps = json.load(f)

from check_more_disqualified import all_disqualified
retained = [c for c in comps if c["id"] not in all_disqualified]
print(f"Total retained companies: {len(retained)}")

retained_names = [c["company_name"].strip().casefold() for c in retained]
overlap = set(rep_names).intersection(set(retained_names))
if overlap:
    print(f"ERROR: Overlap between replacements and retained: {overlap}")
else:
    print("SUCCESS: Zero overlap between replacements and retained companies!")

# Check field completeness
required_keys = [
    "company_name", "website", "domain_sector", "employee_count",
    "funding_stage_investors", "work_model_location", "career_page_url",
    "career_email", "hiring_decision_maker", "nalin_tech_fit_hook", "outreach_status"
]

missing_fields = []
for idx, r in enumerate(all_replacements, 1):
    for k in required_keys:
        if not r.get(k) or str(r.get(k)).strip() == "":
            missing_fields.append((idx, r.get("company_name"), k))

if missing_fields:
    print(f"ERROR: Found {len(missing_fields)} missing fields in replacements:")
    for mf in missing_fields:
        print(mf)
else:
    print("SUCCESS: All 108 replacement records have all required fields!")
    print(f"Grand Total: {len(retained)} retained + {len(all_replacements)} replacements = {len(retained) + len(all_replacements)} total!")
