import json

with open("scripts/live_audit_results.json", "r", encoding="utf-8") as f:
    audit_data = json.load(f)

with open("companies_data.json", "r", encoding="utf-8") as f:
    comps = json.load(f)
    
comp_map = {c["id"]: c for c in comps}

print("=== 1. WEBSITE CHECK NOT 200 (DEAD / BROKEN SITES) ===")
dead_sites = []
for a in audit_data:
    code = a["website_check"]["code"]
    if code != 200:
        c = comp_map[a["id"]]
        dead_sites.append((c["id"], c["company_name"], c["website"], code, a["website_check"]["error"]))
        print(f"ID {c['id']:3d}: {c['company_name']:<25} | Code: {str(code):<5} | URL: {c['website']} | Err: {a['website_check']['error'][:50]}")

print(f"\nTotal broken websites: {len(dead_sites)}")

print("\n=== 2. WEBSITE REDIRECTS (ACQUIRED / REBRANDED / DOMAIN CHANGED) ===")
redirected = []
for a in audit_data:
    if a["website_check"]["host_changed"]:
        c = comp_map[a["id"]]
        orig = c["website"]
        dest = a["website_check"]["final_url"]
        redirected.append((c["id"], c["company_name"], orig, dest))
        print(f"ID {c['id']:3d}: {c['company_name']:<25} | {orig} -> {dest}")

print(f"\nTotal redirects: {len(redirected)}")

print("\n=== 3. CAREER PAGE ISSUES ===")
broken_careers = []
for a in audit_data:
    code = a["career_url_check"]["code"]
    if code != 200:
        c = comp_map[a["id"]]
        broken_careers.append((c["id"], c["company_name"], c["career_page_url"], code))

print(f"Total broken careers: {len(broken_careers)}")
