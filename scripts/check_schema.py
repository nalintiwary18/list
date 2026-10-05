import json

with open("companies_data.json", "r", encoding="utf-8") as f:
    comps = json.load(f)

print(f"Total entries: {len(comps)}")

# Let's inspect fields of a sample entry
print("Schema fields:")
for k, v in comps[0].items():
    print(f"  {k}: {type(v).__name__} (e.g. {repr(v)[:50]})")
