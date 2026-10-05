import json

with open("companies_data.json", "r", encoding="utf-8") as f:
    comps = json.load(f)

from check_more_disqualified import all_disqualified
retained = [c for c in comps if c["id"] not in all_disqualified]

print(f"Retained: {len(retained)}")

# Check emails: find any that are generic careers@ or info@ and see if we can improve them with founder/lead names
generic_emails = []
for c in retained:
    email = c["career_email"]
    if any(p in email for p in ['careers@', 'jobs@', 'hiring@', 'info@', 'contact@', 'support@', 'talent@']):
        generic_emails.append((c["id"], c["company_name"], email, c["hiring_decision_maker"]))

print(f"Retained companies with generic email aliases: {len(generic_emails)}")
for cid, name, email, dm in generic_emails[:20]:
    print(f"[{cid:3d}] {name:<25} | {email:<25} | DM: {dm[:35]}")
