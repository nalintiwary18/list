import json

with open("companies_data.json", "r", encoding="utf-8") as f:
    comps = json.load(f)

with open("scripts/live_audit_results.json", "r", encoding="utf-8") as f:
    audit_data = json.load(f)

audit_map = {a["id"]: a for a in audit_data}

# Print companies where website code != 200 or host changed
print("=== WEBSITE ISSUES ===")
for c in comps:
    cid = c["id"]
    a = audit_map.get(cid, {})
    w_check = a.get("website_check", {})
    code = w_check.get("code")
    err = w_check.get("error", "")
    final_url = w_check.get("final_url", "")
    host_changed = w_check.get("host_changed", False)
    
    if code != 200 or host_changed:
        print(f"[{cid:3d}] {c['company_name']:<25} | Code: {code} | HostChanged: {host_changed} | Final: {final_url} | Err: {err[:40]}")
