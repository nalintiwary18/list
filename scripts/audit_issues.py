import json
import re

def analyze():
    with open("companies_data.json", "r", encoding="utf-8") as f:
        comps = json.load(f)
        
    with open("company_link_audit.json", "r", encoding="utf-8") as f:
        audit_records = json.load(f)["records"]
        
    audit_map = {r["id"]: r for r in audit_records}
    
    flag_names = [
        'scale ai', 'groq', 'perplexity', 'runway', 'glean', 'harness', 'vercel', 
        'supabase', 'midjourney', 'together ai', 'cursor', 'cognition', 
        'dyte', 'cacheflow', 'togai', 'neon', 'highlight.io', 'codeium', 
        'protect ai', 'phidata', 'keywords ai', 'factory.ai', 'memfold', 'invoid', 
        'agri10x', 'blend', 'defer.run', 'vance', 'toplyne', 'customerglu', 'blusmart'
    ]
    
    flagged = []
    redirected = []
    dead_websites = []
    dead_careers = []
    
    for c in comps:
        cid = c["id"]
        cname = c["company_name"]
        a = audit_map.get(cid, {})
        w_check = a.get("website_check", {})
        c_check = a.get("career_url_check", {})
        
        # Check against flagged list
        for f in flag_names:
            if f in cname.lower() or f in c["website"].lower():
                flagged.append((cid, cname, c["website"], f))
                break
                
        # Check website redirects to another host
        if w_check.get("host_changed"):
            redirected.append((cid, cname, c["website"], w_check.get("final_url")))
            
        # Check dead websites
        w_code = w_check.get("code")
        if w_code != 200:
            dead_websites.append((cid, cname, c["website"], w_code, w_check.get("detail")))
            
        # Check dead careers
        c_code = c_check.get("code")
        if c_code != 200:
            dead_careers.append((cid, cname, c["career_page_url"], c_code))

    print(f"=== FLAGGED COMPANIES SPECIFIED BY USER ({len(flagged)}) ===")
    for item in flagged:
        print(f"  ID {item[0]}: {item[1]} | URL: {item[2]} (matched '{item[3]}')")
        
    print(f"\n=== WEBSITE HOST CHANGED / REDIRECTED ({len(redirected)}) ===")
    for item in redirected:
        print(f"  ID {item[0]}: {item[1]} | {item[2]} -> {item[3]}")
        
    print(f"\n=== WEBSITE NON-200 ({len(dead_websites)}) ===")
    for item in dead_websites:
        print(f"  ID {item[0]}: {item[1]} | Code: {item[3]} | URL: {item[2]}")

if __name__ == "__main__":
    analyze()
