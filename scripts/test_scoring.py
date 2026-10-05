import json
import re

with open("companies_data.json", "r", encoding="utf-8") as f:
    comps = json.load(f)

print(f"Loaded {len(comps)} companies.")

# Top Open Source / High Engagement companies for Warm Path = 5
top_oss_and_community = {
    "langchain", "portkey.ai", "mem0", "composio", "trigger.dev", "dub.co",
    "helicone", "posthog", "cal.com", "prisma", "refine", "ragas",
    "codeant ai", "perseus", "cardboard", "qdrant", "lancedb", "firecrawl",
    "e2b", "letta (memgpt)", "truefoundry", "litellm (berriai)", "agno (formerly phidata)",
    "respan (formerly keywords ai)", "sarvam ai", "giga.ai", "bolna.ai",
    "drdroid", "clueso", "inferless", "kusho ai", "tailcall", "parseable",
    "zerok", "auquan", "emergent", "greylabs.ai", "atomicwork", "neysa",
    "maxim ai", "unifyapps", "h2loop", "dodge ai", "meetaugust.ai", "august ai",
    "exa ai", "phot.ai", "inngest", "mintlify", "resend", "daily.co", "upstash",
    "fixie.ai", "galileo", "jina ai", "relevance ai", "promptfoo", "braintrust"
}

# Priority Tier-1 Investors for Comp Likelihood = 5
tier1_investors = [
    "lightspeed", "accel", "peak xv", "sequoia", "y combinator", "together fund",
    "elevation capital", "matrix partners", "z47", "blume", "nexus", "bessemer",
    "benchmark", "andreessen", "a16z", "general catalyst", "tiger global"
]

scored_companies = []

for c in comps:
    name = c["company_name"].strip()
    name_lower = name.lower()
    sector = c["domain_sector"].lower()
    hook = c["nalin_tech_fit_hook"].lower()
    fund = c["funding_stage_investors"].lower()
    loc = c["work_model_location"].lower()
    emp = c["employee_count"]
    
    # 1. Product & Stack Fit (0-5)
    # Check alignment with AI/LLM, Next.js, FastAPI, RAG, LangGraph, AST
    stack_score = 3 # base default for curated list
    if any(k in sector or k in hook for k in ["llm", "langgraph", "rag", "agent", "ast", "observability", "evaluation", "gateway", "vector", "speech", "voice"]):
        stack_score = 4
    if any(k in name_lower for k in top_oss_and_community) or ("langgraph" in hook and "next.js" in hook):
        stack_score = 5
    elif any(k in sector for k in ["ecommerce", "logistics", "hr", "payroll", "legal"]):
        stack_score = 3

    # 2. Hiring Signal (0-5)
    # Check recency of funding (2024-2026), YC W23-S26, Surge 11-12, Atoms 2026
    hiring_score = 3
    if any(k in fund for k in ["w24", "s24", "w25", "s25", "w26", "s26", "surge 12", "surge 11", "cohort 2026", "2026", "2025"]):
        hiring_score = 5
    elif any(k in fund for k in ["seed", "series a", "w23", "s23", "surge 10"]):
        hiring_score = 4
    elif "bootstrapped" in fund:
        hiring_score = 3

    # 3. India Eligibility (0-5)
    india_score = 3
    has_delhi = any(p in loc for p in ["delhi", "noida", "gurgaon", "gurugram"])
    has_remote = "remote" in loc
    has_blr = "bangalore" in loc or "bengaluru" in loc
    if has_delhi:
        india_score = 5 # Local Delhi-NCR
    elif has_blr and has_remote:
        india_score = 4 # BLR HQ with remote India
    elif has_remote:
        india_score = 4 # Remote India
    else:
        india_score = 3

    # 4. Warm Path (0-5)
    warm_score = 2
    if any(k in name_lower for k in top_oss_and_community):
        warm_score = 5 # Open Source Contribution / Active Discord / YC batchmates
    elif any(k in fund for k in ["y combinator", "peak xv", "accel atoms", "together fund", "blume", "z47", "elevation"]):
        warm_score = 4 # Tier-1 Indian Founder / Alumni ecosystem
    elif any(k in loc for k in ["delhi", "gurgaon", "noida"]):
        warm_score = 3 # Delhi-NCR local network
    else:
        warm_score = 2

    # 5. Compensation Likelihood (0-5)
    # Check funding amount & investors (12+ LPA / paid internship capacity)
    comp_score = 3
    is_tier1 = any(inv in fund for inv in tier1_investors)
    
    # Extract funding amount if present
    amt_match = re.search(r"\$([0-9\.]+)[mb]", fund)
    amt = float(amt_match.group(1)) if amt_match else 1.0
    is_millions = "m" in fund or not ("k" in fund)
    if not is_millions:
        amt = amt / 1000.0

    if amt >= 5.0 or (amt >= 2.0 and is_tier1):
        comp_score = 5
    elif amt >= 1.5 or is_tier1:
        comp_score = 4
    elif amt >= 0.5:
        comp_score = 3
    else:
        comp_score = 2

    total_score = stack_score + hiring_score + india_score + warm_score + comp_score

    # Determine recommended proof based on company profile
    if any(k in sector or k in hook for k in ["llm", "latency", "infer", "observability", "eval", "gateway", "cache", "token"]):
        rec_proof = "NimitAI 317s->117s Pipeline Win"
    elif any(k in sector or k in hook for k in ["code", "ast", "test", "security", "developer", "sdk", "api"]):
        rec_proof = "Code Sage AST Engine"
    elif any(k in sector or k in hook for k in ["agent", "memory", "note", "workflow", "copilot", "task"]):
        rec_proof = "Notovo LangGraph Memory"
    elif any(k in sector or k in hook for k in ["search", "rag", "retrieval", "vector", "embed", "doc"]):
        rec_proof = "OceanRAG Retrieval"
    elif any(k in sector or k in hook for k in ["voice", "speech", "audio", "video", "media"]):
        rec_proof = "TTS Audio Analysis"
    else:
        rec_proof = "NimitAI 317s->117s Pipeline Win"

    # Extract decision maker name & role
    dm_raw = c["hiring_decision_maker"]
    # Usually: "Name (Title) & Name (Title)" or "Name (Title)"
    name_match = re.match(r"^([^(&]+)(?:\(([^)]+)\))?", dm_raw.strip())
    if name_match:
        c_name = name_match.group(1).strip()
        c_role = name_match.group(2).strip() if name_match.group(2) else "Founder / Engineering Lead"
    else:
        c_name = dm_raw.strip()
        c_role = "Founder / Engineering Lead"

    # LinkedIn company URL fallback
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", name.lower()).strip("-")
    linkedin_url = f"https://www.linkedin.com/company/{slug}"

    # Warm intro path detail
    if warm_score >= 5:
        warm_path = "Open-Source PR / Batchmate Warm Intro"
    elif warm_score == 4:
        warm_path = "Accelerator Cohort / VC Alumni Network"
    elif warm_score == 3:
        warm_path = "Delhi-NCR Founder Community"
    else:
        warm_path = "Direct Decision-Maker Outreach"

    scored_companies.append({
        "comp": c,
        "total_score": total_score,
        "score_stack_fit": stack_score,
        "score_hiring_signal": hiring_score,
        "score_india_eligibility": india_score,
        "score_warm_path": warm_score,
        "score_comp_likelihood": comp_score,
        "rec_proof": rec_proof,
        "contact_name": c_name,
        "contact_role": c_role,
        "linkedin_url": linkedin_url,
        "contact_email_source": "Verified Domain / Founder Direct",
        "warm_intro_path": warm_path
    })

# Sort by total score descending, then by stack_fit descending
scored_companies.sort(key=lambda x: (x["total_score"], x["score_stack_fit"], x["score_hiring_signal"]), reverse=True)

# Assign Tiers:
# Tier A: Exactly top 40 companies (score 21-25)
# Tier B: Exactly next 100 companies (score 17-20)
# Tier C: Remaining 215 companies (score <= 16)

tier_a = scored_companies[:40]
tier_b = scored_companies[40:140]
tier_c = scored_companies[140:]

print(f"Tier A count: {len(tier_a)} (Scores: {tier_a[-1]['total_score']} to {tier_a[0]['total_score']})")
print(f"Tier B count: {len(tier_b)} (Scores: {tier_b[-1]['total_score']} to {tier_b[0]['total_score']})")
print(f"Tier C count: {len(tier_c)} (Scores: {tier_c[-1]['total_score']} to {tier_c[0]['total_score']})")

print("\n--- SAMPLE TIER A LEADERS ---")
for item in tier_a[:10]:
    c = item["comp"]
    print(f"[{item['total_score']:2d}/25] {c['company_name']:<25} | {c['domain_sector'][:35]:<35} | Proof: {item['rec_proof']}")
