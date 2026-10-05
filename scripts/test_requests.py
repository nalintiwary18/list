import requests
print("Requests version:", requests.__version__)

test_urls = [
    "https://slanglabs.in",
    "https://pesto.tech",
    "https://gan.ai",
    "https://digantara.com",
    "https://spryhealth.com",
    "https://shipyaari.com",
    "https://knorish.com",
    "https://waybill.com",
    "https://kindling.ai",
    "https://cognisaas.com",
    "https://headfone.co.in",
    "https://verloop.io",
    "https://ecolibrium.io",
    "https://tartanhq.com"
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

for u in test_urls:
    try:
        r = requests.get(u, headers=headers, timeout=6, allow_redirects=True)
        print(f"OK {r.status_code} : {u} -> {r.url}", flush=True)
    except Exception as e:
        print(f"FAIL : {u} -> {type(e).__name__}: {e}", flush=True)
