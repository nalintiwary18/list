import json
import re

with open("companies_data.json", "r", encoding="utf-8") as f:
    comps = json.load(f)

with open("scripts/live_audit_results.json", "r", encoding="utf-8") as f:
    audit_data = json.load(f)

audit_map = {a["id"]: a for a in audit_data}

# Known problematic companies to remove based on user instructions and audit
# 1. Flagged by user explicitly
# 2. Acquired / Rebranded
# 3. Dead / 404 / Squatted
# 4. Massive headcount > 100 or non-tech (pathology labs, sanitary pads, used phones, etc.)
# 5. Duplicates

disqualified = []
reasons = {}

for c in comps:
    cid = c["id"]
    name = c["company_name"]
    audit = audit_map.get(cid, {})
    w_check = audit.get("website_check", {})
    w_code = w_check.get("code")
    w_err = w_check.get("error", "")
    w_final = w_check.get("final_url", "")
    w_host_changed = w_check.get("host_changed", False)
    
    # Check 1: Explicit user flags & dead domains
    if any(k in name.lower() for k in [
        'agri10x', 'blend', 'defer.run', 'vance', 'toplyne', 'customerglu', 'blusmart',
        'chaos genius', 'houseware', 'bikayi', 'persapien', 'tune ai', 'wurkr',
        'leaf round', 'sprih', 'monsterapi', 'soothe healthcare', 'redcliffe',
        'cashify', 'cogoport', 'otipy', 'river mobility', 'baaz bikes', 'revfin'
    ]):
        disqualified.append(cid)
        reasons[cid] = "User-flagged / Dead / Acquired / Massively oversized / Non-tech"
        continue
        
    # Check 2: Acquired via host changed to known acquirer
    if 'flexera.com' in w_final or 'notion.site/bikayi-memo' in w_final:
        disqualified.append(cid)
        reasons[cid] = "Acquired / Shut down"
        continue

    # Check 3: Broken website (getaddrinfo failed or 404)
    if w_code == 404 or 'getaddrinfo failed' in w_err:
        disqualified.append(cid)
        reasons[cid] = f"Dead domain: {w_code} ({w_err})"
        continue

    # Check 4: Duplicate
    if cid == 339 and 'Quest Labs' in name:
        disqualified.append(cid)
        reasons[cid] = "Duplicate of ID 11"
        continue

print(f"Total initially disqualified from obvious rules: {len(disqualified)}")
for cid in disqualified:
    c = comps[cid-1]
    print(f"ID {cid:3d}: {c['company_name']:<25} | Reason: {reasons[cid]}")
