from create_replacements_batch1 import replacements_list

b1_names = [r["company_name"] for r in replacements_list]
print(f"Batch 1 has {len(b1_names)} companies.")

# Find Kello in batch 1 and replace it with Truffle AI
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
        print("Replaced Kello with Truffle AI in batch 1.")

# Re-check unique names
b1_names_updated = [r["company_name"] for r in replacements_list]
print(f"Unique names in Batch 1: {len(set(b1_names_updated))}")
