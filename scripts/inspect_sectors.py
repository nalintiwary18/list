import json

with open("companies_data.json", "r", encoding="utf-8") as f:
    comps = json.load(f)

print(f"Total companies in file: {len(comps)}")

# Let's inspect companies in batches of 50 to see sectors, descriptions, etc.
sectors = {}
for c in comps:
    sec = c.get("domain_sector", "Unknown")
    sectors[sec] = sectors.get(sec, 0) + 1

for s, cnt in sorted(sectors.items(), key=lambda x: x[1], reverse=True)[:25]:
    print(f"{s:<40} : {cnt}")
