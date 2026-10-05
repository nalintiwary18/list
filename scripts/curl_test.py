import subprocess

urls = [
    ("Slang Labs", "https://slanglabs.in"),
    ("Waybill", "https://waybill.com"),
    ("Kindling", "https://kindling.ai"),
    ("CogniSaaS", "https://cognisaas.com"),
    ("Shipyaari", "https://shipyaari.com"),
    ("Pesto Tech", "https://pesto.tech"),
    ("Velocity.in", "https://velocity.in"),
    ("Klub", "https://klubworks.com"),
    ("Digantara", "https://digantara.com"),
    ("Headfone", "https://headfone.co.in"),
    ("Gan.ai", "https://gan.ai"),
    ("Verloop.io", "https://verloop.io"),
    ("Ecolibrium", "https://ecolibrium.io"),
    ("Tartan", "https://tartanhq.com"),
    ("Knorish", "https://knorish.com"),
    ("Spry", "https://spryhealth.com")
]

for name, u in urls:
    try:
        cmd = f'curl -I -s -L --max-time 6 -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" "{u}"'
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        out = res.stdout
        lines = [l.strip() for l in out.splitlines() if l.startswith("HTTP/")]
        last_http = lines[-1] if lines else "NO_RESPONSE"
        print(f"{name:<15} | {u:<25} | {last_http}")
    except Exception as e:
        print(f"{name:<15} | {u:<25} | ERR: {e}")
