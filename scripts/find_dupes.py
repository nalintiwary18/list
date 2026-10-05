import json

with open("companies_data.json", "r", encoding="utf-8") as f:
    comps = json.load(f)

names = [c["company_name"].strip().casefold() for c in comps]
seen = set()
dupes = []
for n in names:
    if n in seen:
        dupes.append(n)
    seen.add(n)

print("Duplicates:", dupes)
for d in dupes:
    for c in comps:
        if c["company_name"].strip().casefold() == d:
            print(f"ID {c['id']}: {c['company_name']} ({c['website']})")
