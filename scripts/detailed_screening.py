import json

with open("companies_data.json", "r", encoding="utf-8") as f:
    comps = json.load(f)

with open("scripts/live_audit_results.json", "r", encoding="utf-8") as f:
    audit_data = json.load(f)

audit_map = {a["id"]: a for a in audit_data}

def check_range(start, end):
    print(f"\n=== BATCH {start+1} TO {end} ===")
    for i in range(start, min(end, len(comps))):
        c = comps[i]
        cid = c["id"]
        a = audit_map.get(cid, {})
        w = a.get("website_check", {})
        code = w.get("code")
        furl = w.get("final_url", "")
        print(f"[{cid:3d}] {c['company_name']:<28} | {c['funding_stage_investors'][:24]:<24} | {c['employee_count']:<7} | {code} {furl[:32]}")

check_range(150, 200)
check_range(200, 250)
check_range(250, 300)
check_range(300, 355)
