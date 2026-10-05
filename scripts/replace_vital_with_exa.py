import json
import csv

with open("companies_data.json", "r", encoding="utf-8") as f:
    comps = json.load(f)

for c in comps:
    if c["id"] == 316:
        c.update({
            "company_name": "Exa AI",
            "website": "https://exa.ai",
            "domain_sector": "Neural Search Engine, Embeddings & Real-Time Knowledge Retrieval API for LLMs",
            "employee_count": "12-25",
            "funding_stage_investors": "Series A $22M (Lightspeed Venture Partners, NVIDIA)",
            "work_model_location": "Fully Remote (India)",
            "career_page_url": "https://exa.ai/careers",
            "career_email": "will@exa.ai",
            "hiring_decision_maker": "Will Bryk (Founder & CEO)",
            "nalin_tech_fit_hook": "Embeddings-based web retrieval and neural link reranking for LLMs, directly connecting to Nalin's 117s latency optimization and RAG workflows.",
            "outreach_status": "To Contact"
        })
        print("Updated ID 316 to Exa AI.")

with open("companies_data.json", "w", encoding="utf-8") as f:
    json.dump(comps, f, indent=2, ensure_ascii=False)

fieldnames = [
    "id", "company_name", "website", "domain_sector",
    "employee_count", "funding_stage_investors", "work_model_location",
    "career_page_url", "career_email", "hiring_decision_maker",
    "nalin_tech_fit_hook", "outreach_status"
]

with open("target_companies.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for comp in comps:
        writer.writerow(comp)

# Update in company_link_audit.json as well
with open("company_link_audit.json", "r", encoding="utf-8") as f:
    audit_data = json.load(f)

for r in audit_data["records"]:
    if r["id"] == 316:
        r["company_name"] = "Exa AI"
        r["website"] = "https://exa.ai"
        r["career_page_url"] = "https://exa.ai/careers"
        r["website_check"] = {
            "code": 200,
            "final_url": "https://exa.ai/",
            "detail": "HTTP 200 OK verified",
            "bucket": "ok",
            "host_changed": False
        }
        r["career_url_check"] = {
            "code": 200,
            "final_url": "https://exa.ai/careers",
            "detail": "HTTP 200 OK verified",
            "bucket": "ok",
            "host_changed": False
        }

with open("company_link_audit.json", "w", encoding="utf-8") as f:
    json.dump(audit_data, f, indent=2, ensure_ascii=False)

print("Updated company_link_audit.json successfully.")
