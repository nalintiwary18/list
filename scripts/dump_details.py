import json

with open("companies_data.json", "r", encoding="utf-8") as f:
    comps = json.load(f)

with open("scripts/companies_detailed_dump.txt", "w", encoding="utf-8") as out:
    for c in comps:
        out.write(f"ID {c['id']}: {c['company_name']}\n")
        out.write(f"  Website: {c['website']}\n")
        out.write(f"  Sector: {c['domain_sector']}\n")
        out.write(f"  Size: {c['employee_count']} | Funding: {c['funding_stage_investors']}\n")
        out.write(f"  Location: {c['work_model_location']}\n")
        out.write(f"  Career: {c['career_page_url']} | Email: {c['career_email']}\n")
        out.write(f"  Founder: {c['hiring_decision_maker']}\n")
        out.write(f"  Hook: {c['nalin_tech_fit_hook']}\n\n")

print("Dumped all 355 companies.")
