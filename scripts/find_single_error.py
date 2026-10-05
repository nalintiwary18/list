import json

with open("scripts/live_audit_results.json", "r", encoding="utf-8") as f:
    results = json.load(f)

for r in results:
    if r["website_check"]["code"] not in [200, 401, 403]:
        print(r["id"], r["company_name"], r["website"], r["website_check"])
