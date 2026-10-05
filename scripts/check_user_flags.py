import json

with open("companies_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

names = [c["company_name"] for c in data]
print(f"Total companies in companies_data.json: {len(data)}")

search_terms = [
    'scale', 'groq', 'perplexity', 'runway', 'glean', 'harness', 'vercel', 'supabase', 
    'midjourney', 'together', 'cursor', 'cognition', 'dyte', 'cacheflow', 'togai', 
    'neon', 'highlight', 'codeium', 'protect ai', 'phidata', 'keywords', 'factory', 
    'memfold', 'invoid', 'agri', 'blend', 'defer', 'vance', 'toplyne', 'customerglu', 
    'blusmart', 'anysphere'
]

matches = []
for c in data:
    name_low = c["company_name"].lower()
    for term in search_terms:
        if term in name_low:
            matches.append((c["id"], c["company_name"], c["website"], term))

print(f"Found {len(matches)} matching entries:")
for mid, mname, mweb, mterm in matches:
    print(f"ID {mid:3d}: {mname:<30} | {mweb:<35} | matched: {mterm}")
