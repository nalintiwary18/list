import json

with open("companies_data.json", "r", encoding="utf-8") as f:
    comps = json.load(f)

with open("scripts/live_audit_results.json", "r", encoding="utf-8") as f:
    audit = {a["id"]: a for a in json.load(f)}

print(f"Loaded {len(comps)} companies and {len(audit)} audit records.")

# Let's inspect all fields and classify every company
for c in comps:
    cid = c["id"]
    a = audit.get(cid, {})
    w_check = a.get("website_check", {})
    code = w_check.get("code")
    err = w_check.get("error", "")
    final_url = w_check.get("final_url", "")
    host_changed = w_check.get("host_changed", False)
    
    # Print if error or redirect or special status
    if code != 200 or host_changed:
        pass
