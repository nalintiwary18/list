import json

with open("scripts/live_audit_results.json", "r", encoding="utf-8") as f:
    results = json.load(f)

print(f"Total results: {len(results)}")
errors = [r for r in results if r["website_check"]["code"] not in [200, 401, 403]]
print(f"Errors/Timeouts: {len(errors)}")

for r in errors:
    print(f"[{r['id']:3d}] {r['company_name']:<28} | URL: {r['website']:<32} | Check: {r['website_check']['code']} - {r['website_check']['detail']}")
