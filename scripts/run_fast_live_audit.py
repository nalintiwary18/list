import json
import requests
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor
import datetime

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
}

def check_single_url(url):
    if not url or not url.startswith("http"):
        return {
            "code": "MISSING",
            "final_url": url or "",
            "detail": "Invalid or missing URL",
            "bucket": "error",
            "host_changed": False
        }
    try:
        r = requests.get(url, headers=HEADERS, timeout=5, allow_redirects=True)
        final_url = r.url
        orig_host = urlparse(url).netloc.lower().replace("www.", "")
        final_host = urlparse(final_url).netloc.lower().replace("www.", "")
        host_changed = (orig_host != final_host) and (not final_host.endswith(orig_host)) and (not orig_host.endswith(final_host))
        
        code = r.status_code
        if code == 200:
            bucket = "ok"
            detail = "HTTP 200 OK verified"
        elif code in [401, 403]:
            # Bot protection (Cloudflare, etc.) but host is alive
            bucket = "blocked"
            detail = f"HTTP {code} (Bot protection/WAF)"
        elif code == 404:
            bucket = "not_found"
            detail = "HTTP 404 Not Found"
        else:
            bucket = "error"
            detail = f"HTTP {code}"
            
        return {
            "code": code,
            "final_url": final_url,
            "detail": detail,
            "bucket": bucket,
            "host_changed": host_changed
        }
    except requests.exceptions.Timeout:
        return {
            "code": "TIMEOUT",
            "final_url": "",
            "detail": "Connection timed out (5s)",
            "bucket": "timeout",
            "host_changed": False
        }
    except requests.exceptions.SSLError:
        return {
            "code": "SSL_ERROR",
            "final_url": "",
            "detail": "SSL handshake failure",
            "bucket": "error",
            "host_changed": False
        }
    except requests.exceptions.ConnectionError:
        return {
            "code": "DNS_FAIL",
            "final_url": "",
            "detail": "DNS resolution or connection failure",
            "bucket": "error",
            "host_changed": False
        }
    except Exception as e:
        return {
            "code": "ERR",
            "final_url": "",
            "detail": str(e)[:60],
            "bucket": "error",
            "host_changed": False
        }

def run():
    with open("companies_data.json", "r", encoding="utf-8") as f:
        comps = json.load(f)
        
    print(f"Starting audit of {len(comps)} companies with 35 worker threads...", flush=True)
    
    def process(c):
        cid = c["id"]
        cname = c["company_name"]
        w_res = check_single_url(c["website"])
        c_res = check_single_url(c["career_page_url"])
        return {
            "id": cid,
            "company_name": cname,
            "website": c["website"],
            "career_page_url": c["career_page_url"],
            "website_check": w_res,
            "career_url_check": c_res
        }
        
    with ThreadPoolExecutor(max_workers=35) as ex:
        results = list(ex.map(process, comps))
        
    results.sort(key=lambda x: x["id"])
    
    today_str = datetime.date.today().isoformat()
    audit_payload = {
        "checked_date": today_str,
        "method": "Live multithreaded HTTP audit & verified URL resolution",
        "records": results
    }
    
    with open("company_link_audit.json", "w", encoding="utf-8") as f:
        json.dump(audit_payload, f, indent=2, ensure_ascii=False)
        
    with open("scripts/live_audit_results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
        
    w_200 = sum(1 for r in results if r["website_check"]["code"] == 200)
    w_blocked = sum(1 for r in results if r["website_check"]["bucket"] == "blocked")
    w_err = sum(1 for r in results if r["website_check"]["code"] not in [200, 401, 403])
    c_200 = sum(1 for r in results if r["career_url_check"]["code"] == 200)
    
    print("\n=== AUDIT SUMMARY ===", flush=True)
    print(f"Total companies checked: {len(results)}", flush=True)
    print(f"Websites HTTP 200 OK: {w_200}", flush=True)
    print(f"Websites Protected/WAF (401/403): {w_blocked}", flush=True)
    print(f"Websites Errors/Timeouts: {w_err}", flush=True)
    print(f"Career URLs HTTP 200 OK: {c_200}", flush=True)
    print("Audit written to company_link_audit.json and live_audit_results.json successfully.", flush=True)

if __name__ == "__main__":
    run()
