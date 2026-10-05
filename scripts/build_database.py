import csv
import json
import os
import sys

from batch1 import BATCH_1
from batch2 import BATCH_2
from batch3 import BATCH_3
from batch4 import BATCH_4
from batch5 import BATCH_5
from batch6 import BATCH_6
from batch7 import BATCH_7

def compile_database():
    all_companies = []
    seen_names = set()
    
    combined = (
        BATCH_1 +
        BATCH_2 +
        BATCH_3 +
        BATCH_4 +
        BATCH_5 +
        BATCH_6 +
        BATCH_7
    )
    
    print(f"Total raw entries across all 7 batches: {len(combined)}")
    
    for comp in combined:
        name = comp["company_name"].strip()
        name_key = name.lower()
        if name_key in seen_names:
            print(f"Warning: Duplicate detected for {name}. Skipping...")
            continue
        seen_names.add(name_key)
        all_companies.append(comp)
        
    # Re-index neatly from 1 to N
    for idx, comp in enumerate(all_companies, 1):
        comp["id"] = idx
        
    print(f"Total unique verified companies: {len(all_companies)}")
    
    if len(all_companies) < 350:
        print(f"ERROR: Expected at least 350 companies, but got {len(all_companies)}")
        sys.exit(1)
        
    csv_file_path = os.path.join(os.path.dirname(__file__), "..", "target_companies.csv")
    json_file_path = os.path.join(os.path.dirname(__file__), "..", "companies_data.json")
    
    fieldnames = [
        "id",
        "company_name",
        "website",
        "domain_sector",
        "employee_count",
        "funding_stage_investors",
        "work_model_location",
        "career_page_url",
        "career_email",
        "hiring_decision_maker",
        "nalin_tech_fit_hook",
        "outreach_status"
    ]
    
    with open(csv_file_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for c in all_companies:
            writer.writerow(c)
            
    with open(json_file_path, mode="w", encoding="utf-8") as f:
        json.dump(all_companies, f, indent=2)
        
    print(f"Successfully updated {csv_file_path} with {len(all_companies)} entries!")
    print(f"Successfully updated {json_file_path} for dashboard viewer!")

if __name__ == "__main__":
    compile_database()
