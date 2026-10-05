import json

with open("companies_data.json", "r", encoding="utf-8") as f:
    comps = json.load(f)

with open("scripts/live_audit_results.json", "r", encoding="utf-8") as f:
    audit_data = json.load(f)

audit_map = {a["id"]: a for a in audit_data}

# Known IDs from above:
flagged_ids = {
    11, 24, 25, 38, 62, 63, 64, 65, 66, 67, 68, 70, 71, 72, 73, 74, 76, 77, 89, 90, 92, 93, 
    99, 110, 119, 120, 121, 137, 141, 148, 153, 158, 161, 162, 163, 164, 167, 169, 174, 
    186, 187, 189, 198, 199, 201, 207, 217, 220, 224, 239, 255, 256, 263, 285, 293, 298, 
    303, 311, 312, 313, 314, 315, 318, 319, 321, 322, 323, 324, 325, 326, 337, 339, 341
}

print(f"Total flagged so far: {len(flagged_ids)}")

# Let's inspect the remaining companies to see if any have weird websites, non-tech sectors, or high headcount
unflagged = [c for c in comps if c["id"] not in flagged_ids]
print(f"Remaining candidates to inspect: {len(unflagged)}")

for c in unflagged:
    cid = c["id"]
    name = c["company_name"]
    sec = c["domain_sector"]
    fund = c["funding_stage_investors"]
    emp = c["employee_count"]
    loc = c["work_model_location"]
    
    # Check if sector or name sounds non-tech (e.g. logistics truck fleet, diagnostic clinic, offline retail)
    a = audit_map.get(cid, {})
    w = a.get("website_check", {})
    code = w.get("code")
    err = w.get("error", "")
    
    if code != 200:
        print(f"Non-200 code: [{cid:3d}] {name:<25} | Code: {code} | Err: {err[:40]}")
