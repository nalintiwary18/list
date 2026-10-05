import json
import csv

# 1. Load original companies
with open("companies_data.json", "r", encoding="utf-8") as f:
    comps = json.load(f)

# 2. Load disqualified IDs
from check_more_disqualified import all_disqualified

# 3. Load replacements
from create_replacements_batch1 import replacements_list
from create_replacements_batch2 import batch2_list

# Update Truffle AI in batch 1
for i, r in enumerate(replacements_list):
    if r["company_name"].lower() == "kello":
        replacements_list[i] = {
            "company_name": "Truffle AI",
            "website": "https://trufflehq.com",
            "domain_sector": "AI-Native Code Search & Context Engine for Developer Tools",
            "employee_count": "6-14",
            "funding_stage_investors": "Seed $1.2M (prominent devtool angels)",
            "work_model_location": "Fully Remote (India) / Bengaluru",
            "career_page_url": "https://trufflehq.com",
            "career_email": "apoorv@trufflehq.com",
            "hiring_decision_maker": "Apoorv Saxena (Founder & CEO)",
            "nalin_tech_fit_hook": "Building semantic code indexers and AST token trees for developer copilots, directly matching Nalin's Code Sage AST audit engine.",
            "outreach_status": "To Contact"
        }

all_replacements = replacements_list + batch2_list
assert len(all_replacements) == 108, f"Expected 108 replacements, got {len(all_replacements)}"

# Known fixes for retained companies
retained_fixes = {
    9: { # GigaML
        "website": "https://giga.ai",
        "career_page_url": "https://giga.ai/careers",
        "career_email": "varun@giga.ai"
    },
    37: { # Waybill
        "website": "https://waybill.to",
        "career_page_url": "https://waybill.to",
        "career_email": "rishi@waybill.to",
        "work_model_location": "Delhi-NCR (Gurugram) / Hybrid",
        "funding_stage_investors": "Seed $500K (Y Combinator S26)",
        "hiring_decision_maker": "Rishi Laddha (Co-Founder & CEO) & Tushar Goyal (Co-Founder & CTO)"
    },
    40: { # K-Dense
        "website": "https://www.k-dense.ai",
        "career_page_url": "https://www.k-dense.ai",
        "career_email": "prateek@k-dense.ai"
    },
    44: { # August AI
        "website": "https://www.meetaugust.ai",
        "career_page_url": "https://www.meetaugust.ai/careers",
        "career_email": "anuruddh@meetaugust.ai",
        "work_model_location": "Delhi-NCR (Gurugram) / Remote"
    },
    83: { # Ritivel -> TensorTest
        "company_name": "TensorTest (formerly Ritivel)",
        "website": "https://tensortest.com",
        "career_page_url": "https://tensortest.com/careers",
        "career_email": "ritik@tensortest.com"
    },
    247: { # Dozee
        "website": "https://www.dozeehealth.ai",
        "career_page_url": "https://www.dozeehealth.ai/careers",
        "career_email": "mudit@dozeehealth.ai"
    },
    252: { # Wysa
        "website": "https://www.wysa.com",
        "career_page_url": "https://www.wysa.com/careers",
        "career_email": "jo@wysa.com"
    },
    305: { # SuperKalam
        "website": "https://superkalam.com",
        "career_page_url": "https://superkalam.com/careers",
        "career_email": "vimal@superkalam.com"
    },
    330: { # NeuralGarage -> VisualDub
        "company_name": "VisualDub (formerly NeuralGarage)",
        "website": "https://visualdub.ai",
        "career_page_url": "https://visualdub.ai/careers",
        "career_email": "mandar@visualdub.ai"
    }
}

final_companies = []
rep_idx = 0

for c in comps:
    cid = c["id"]
    if cid in all_disqualified:
        # Substitute with a replacement
        rep = dict(all_replacements[rep_idx])
        rep_idx += 1
        final_companies.append(rep)
    else:
        # Keep company, apply fixes if any
        c_copy = dict(c)
        if cid in retained_fixes:
            c_copy.update(retained_fixes[cid])
        final_companies.append(c_copy)

assert len(final_companies) == 355, f"Expected 355 companies, got {len(final_companies)}"
assert rep_idx == 108, f"Expected to use all 108 replacements, used {rep_idx}"

# Re-index sequentially from 1 to 355
for i, comp in enumerate(final_companies, 1):
    comp["id"] = i

# Save to companies_data.json
with open("companies_data.json", "w", encoding="utf-8") as f:
    json.dump(final_companies, f, indent=2, ensure_ascii=False)

print("Saved updated 355 companies to companies_data.json.")

# Export to target_companies.csv
fieldnames = [
    "id", "company_name", "website", "domain_sector",
    "employee_count", "funding_stage_investors", "work_model_location",
    "career_page_url", "career_email", "hiring_decision_maker",
    "nalin_tech_fit_hook", "outreach_status"
]

with open("target_companies.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for comp in final_companies:
        writer.writerow(comp)

print("Saved updated 355 companies to target_companies.csv.")
