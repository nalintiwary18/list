import json

with open("companies_data.json", "r", encoding="utf-8") as f:
    comps = json.load(f)

print(f"Total: {len(comps)}")

# Let's inspect companies by batches (50 at a time)
def summarize_batch(start, end):
    print(f"\n=== BATCH {start} to {end} ===")
    for c in comps[start-1:end]:
        print(f"[{c['id']}] {c['company_name']} | {c['website']} | {c['domain_sector'][:40]} | Size: {c['employee_count']} | {c['work_model_location'][:35]}")

summarize_batch(101, 150)
summarize_batch(151, 200)
summarize_batch(201, 250)
summarize_batch(251, 300)
summarize_batch(301, 355)
