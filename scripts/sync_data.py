import json
import csv
import os
import subprocess

def sync_all():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    json_path = os.path.join(base_dir, "companies_data.json")
    csv_path = os.path.join(base_dir, "target_companies.csv")

    if not os.path.exists(json_path):
        print(f"Error: {json_path} does not exist.")
        return False

    with open(json_path, "r", encoding="utf-8") as f:
        companies = json.load(f)

    # Standard columns
    fieldnames = [
        "id", "company_name", "tier", "total_score", "score_stack_fit",
        "score_hiring_signal", "score_india_eligibility", "score_warm_path",
        "score_comp_likelihood", "website", "domain_sector", "employee_count",
        "funding_stage_investors", "work_model_location", "career_page_url",
        "career_email", "contact_name", "contact_role", "hiring_decision_maker",
        "linkedin_url", "contact_email_source", "warm_intro_path",
        "recommended_proof", "nalin_tech_fit_hook", "outreach_status",
        "connection_sent_date", "connection_accepted_date", "dm_sent_date",
        "email_sent_date", "followup_due_date", "last_touched_date", "custom_notes"
    ]

    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for c in companies:
            row = {k: c.get(k, "") for k in fieldnames}
            writer.writerow(row)

    print(f"Synchronized {len(companies)} records to {csv_path}")

    # Regenerate viewer
    gen_script = os.path.join(base_dir, "scripts", "generate_viewer.py")
    subprocess.run(["python", gen_script], check=True)
    
    # Run verification
    verify_script = os.path.join(base_dir, "scripts", "verify_and_export.py")
    subprocess.run(["python", verify_script], check=True)
    return True

if __name__ == "__main__":
    sync_all()
