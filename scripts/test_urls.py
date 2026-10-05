import urllib.request
import ssl

urls_to_test = [
    ("Waybill", "https://waybill.com"),
    ("August AI", "https://august.ai"),
    ("Gan.ai", "https://gan.ai"),
    ("Digantara", "https://digantara.com"),
    ("Spry", "https://spryhealth.com"),
    ("Kindling", "https://kindling.ai"),
    ("CogniSaaS", "https://cognisaas.com"),
    ("Tartan", "https://tartanHQ.com"),
    ("Headfone", "https://headfone.co.in")
]

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

for name, u in urls_to_test:
    try:
        req = urllib.request.Request(
            u,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
            }
        )
        res = urllib.request.urlopen(req, context=ctx, timeout=8)
        print(f"SUCCESS: {name:<15} -> {res.status} ({res.url})")
    except Exception as e:
        print(f"FAILED:  {name:<15} -> {str(e)[:60]}")
