import csv
import os
import re

def verify_dataset():
    csv_path = os.path.join(os.path.dirname(__file__), "..", "target_companies.csv")
    
    if not os.path.exists(csv_path):
        print(f"ERROR: {csv_path} does not exist.")
        return False
        
    with open(csv_path, mode="r", encoding="utf-8") as f:
        reader = list(csv.DictReader(f))
        
    total_count = len(reader)
    print(f"=== SCHEMA AND FORMAT CHECK FOR {total_count} IMPORTED RECORDS ===")
    
    if total_count == 0:
        print("FAILED: No company records found.")
        return False
        
    required_keys = [
        "id", "company_name", "website", "domain_sector",
        "employee_count", "funding_stage_investors", "work_model_location",
        "career_page_url", "career_email", "hiring_decision_maker",
        "nalin_tech_fit_hook", "outreach_status"
    ]
    
    errors = []
    ids = [row.get("id", "").strip() for row in reader]
    names = [row.get("company_name", "").strip().casefold() for row in reader]
    if len(ids) != len(set(ids)):
        errors.append("Duplicate record IDs found")
    if len(names) != len(set(names)):
        errors.append("Duplicate company names found")
    location_stats = {"Delhi-NCR claim": 0, "Remote claim": 0, "Neither claim": 0}
    employee_stats = {}
    
    for row_idx, row in enumerate(reader, 1):
        # 1. Missing keys / empty values
        for k in required_keys:
            if not row.get(k) or str(row.get(k)).strip() == "":
                errors.append(f"Row {row_idx} ({row.get('company_name')}): Missing '{k}'")
                
        # 2. Email format check
        email = row.get("career_email", "").strip()
        if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email):
            errors.append(f"Row {row_idx} ({row.get('company_name')}): Invalid email format '{email}'")
            
        # 3. URL format check
        url = row.get("website", "").strip()
        if not (url.startswith("http://") or url.startswith("https://")):
            errors.append(f"Row {row_idx} ({row.get('company_name')}): Invalid website URL '{url}'")

        career_url = row.get("career_page_url", "").strip()
        if not (career_url.startswith("http://") or career_url.startswith("https://")):
            errors.append(f"Row {row_idx} ({row.get('company_name')}): Invalid career page URL '{career_url}'")
            
        # 4. Location breakdown
        loc = row.get("work_model_location", "")
        has_delhi_claim = any(place in loc.lower() for place in ["delhi", "noida", "gurgaon"])
        has_remote_claim = "remote" in loc.lower()
        if has_delhi_claim:
            location_stats["Delhi-NCR claim"] += 1
        if has_remote_claim:
            location_stats["Remote claim"] += 1
        if not has_delhi_claim and not has_remote_claim:
            location_stats["Neither claim"] += 1
            
        # 5. Headcount breakdown
        emp = row.get("employee_count", "")
        employee_stats[emp] = employee_stats.get(emp, 0) + 1

    if errors:
        print(f"\nAUDIT FAILED WITH {len(errors)} ERRORS:")
        for err in errors[:10]:
            print(" -", err)
        if len(errors) > 10:
            print(f" ... and {len(errors)-10} more.")
        return False

    print(f"\nPASSED: Basic schema, required-field, duplicate, URL-shape, and email-shape checks for {total_count} records.")
    print("LIMITATION: These checks do not verify that a company or contact exists, that a URL belongs to it, or that funding, headcount, location, email, and hiring data are accurate or current.")
    print("\n--- Listed Geographic & Work Model Claims (not independently verified) ---")
    for loc, count in location_stats.items():
        print(f"  • {loc}: {count} companies ({count*100//total_count}%)")
        
    print("\n--- Listed headcount ranges (not independently verified) ---")
    for size, count in sorted(employee_stats.items(), key=lambda x: x[1], reverse=True)[:15]:
        print(f"  • {size} employees: {count} companies")
        
    return True

if __name__ == "__main__":
    success = verify_dataset()
    if not success:
        exit(1)
