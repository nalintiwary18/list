import json
import urllib.request
import urllib.error
import urllib.parse
from concurrent.futures import ThreadPoolExecutor
import socket
import ssl

socket.setdefaulttimeout(8)

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

def check_url(url):
    if not url or not url.startswith("http"):
        return {"code": "MISSING", "final_url": url, "host_changed": False, "error": "Invalid URL"}
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, context=ctx, timeout=8) as resp:
            final_url = resp.geturl()
            orig_host = urllib.parse.urlparse(url).netloc.lower().replace("www.", "")
            final_host = urllib.parse.urlparse(final_url).netloc.lower().replace("www.", "")
            host_changed = (orig_host != final_host) and (not final_host.endswith(orig_host)) and (not orig_host.endswith(final_host))
            return {
                "code": resp.getcode(),
                "final_url": final_url,
                "host_changed": host_changed,
                "error": ""
            }
    except urllib.error.HTTPError as e:
        final_url = e.geturl() if hasattr(e, "geturl") else url
        orig_host = urllib.parse.urlparse(url).netloc.lower().replace("www.", "")
        final_host = urllib.parse.urlparse(final_url).netloc.lower().replace("www.", "") if final_url else orig_host
        host_changed = (orig_host != final_host) if final_url else False
        return {
            "code": e.code,
            "final_url": final_url,
            "host_changed": host_changed,
            "error": str(e.reason)
        }
    except Exception as e:
        return {
            "code": "ERR",
            "final_url": "",
            "host_changed": False,
            "error": str(e)
        }

def run_live_audit():
    with open("companies_data.json", "r", encoding="utf-8") as f:
        comps = json.load(f)
        
    print(f"Auditing {len(comps)} companies with live HTTP checks...")
    results = []
    
    def process_comp(c):
        cid = c["id"]
        cname = c["company_name"]
        w_res = check_url(c["website"])
        c_res = check_url(c["career_page_url"])
        return {
            "id": cid,
            "company_name": cname,
            "website": c["website"],
            "career_page_url": c["career_page_url"],
            "website_check": w_res,
            "career_url_check": c_res
        }
        
    with ThreadPoolExecutor(max_workers=20) as executor:
        results = list(executor.map(process_comp, comps))
        
    # Sort by ID
    results.sort(key=lambda x: x["id"])
    
    with open("scripts/live_audit_results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    with open("company_link_audit.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
        
    # Summaries
    w_errors = [r for r in results if r["website_check"]["code"] != 200]
    w_redirects = [r for r in results if r["website_check"]["host_changed"]]
    c_errors = [r for r in results if r["career_url_check"]["code"] != 200]
    
    print("\n=== LIVE AUDIT COMPLETE ===")
    print(f"Total checked: {len(results)}")
    print(f"Websites with status != 200: {len(w_errors)}")
    print(f"Websites with host changed: {len(w_redirects)}")
    print(f"Career pages with status != 200: {len(c_errors)}")
    
    print("\n--- Top Website Redirects (Host Changed) ---")
    for r in w_redirects[:20]:
        print(f"  ID {r['id']}: {r['company_name']} -> {r['website']} => {r['website_check']['final_url']}")
        
    print("\n--- Top Website Errors (Not 200) ---")
    for r in w_errors[:20]:
        print(f"  ID {r['id']}: {r['company_name']} -> Code: {r['website_check']['code']} ({r['website_check']['error']}) | URL: {r['website']}")

if __name__ == "__main__":
    run_live_audit()
