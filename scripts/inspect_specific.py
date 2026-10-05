import json

with open("companies_data.json", "r", encoding="utf-8") as f:
    comps = json.load(f)

with open("scripts/live_audit_results.json", "r", encoding="utf-8") as f:
    audit_data = json.load(f)

audit_map = {a["id"]: a for a in audit_data}

# Inspect ID 12 (Beatoven.ai), ID 290 (Fold), ID 255 (Stanplus), ID 293 (Everstage)
for cid in [12, 67, 255, 290, 293, 321, 324]:
    c = comps[cid-1]
    a = audit_map.get(cid, {})
    w_check = a.get("website_check", {})
    print(f"ID {cid:3d}: {c['company_name']:<25} | URL: {c['website']:<30} | Audit: {w_check.get('code')} {w_check.get('final_url', '')}")
