import json

with open("companies_data.json", "r", encoding="utf-8") as f:
    comps = json.load(f)

with open("scripts/companies_list.txt", "w", encoding="utf-8") as out:
    out.write(f"Total companies: {len(comps)}\n")
    for c in comps:
        out.write(f"{c['id']}: {c['company_name']} | {c['website']} | {c['employee_count']} | {c['funding_stage_investors']} | {c['work_model_location']}\n")
