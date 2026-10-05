import json

with open("companies_data.json", "r", encoding="utf-8") as f:
    comps = json.load(f)

existing_names = set(c["company_name"].lower() for c in comps)

from create_replacements_batch1 import replacements_list
b1_names = set(r["company_name"].lower() for r in replacements_list)

overlap = b1_names.intersection(existing_names)
print(f"Overlap between Batch 1 and existing dataset: {overlap}")
