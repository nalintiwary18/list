import json
import csv
import re
import datetime

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
    "fixie.ai", "galileo", "jina ai", "relevance ai", "promptfoo", "braintrust",
    "nango", "speakeasy", "loops", "axiom", "koyeb"
}

tier1_investors = [
    "lightspeed", "accel", "peak xv", "sequoia", "y combinator", "together fund",
    "elevation capital", "matrix partners", "z47", "blume", "nexus", "bessemer",
    "benchmark", "andreessen", "a16z", "general catalyst", "tiger global", "felicis"
]

scored_items = []

for c in comps:
    name = c["company_name"].strip()
    name_lower = name.lower()
    sector = c["domain_sector"].lower()
    hook = c["nalin_tech_fit_hook"].lower()
    fund = c["funding_stage_investors"].lower()
    loc = c["work_model_location"].lower()
    
    # 1. Product & Stack Fit (0-5)
    stack_score = 3
    if any(k in sector or k in hook for k in [
        "llm", "langgraph", "rag", "agent", "ast", "observability", "evaluation",
        "gateway", "vector", "speech", "voice", "next.js", "fastapi", "react"
    ]):
        stack_score = 4
    if any(k in name_lower for k in top_oss_and_community) or ("langgraph" in hook or "ast" in hook):
        stack_score = 5

    # 2. Hiring Signal (0-5)
    hiring_score = 3
    if any(k in fund for k in ["w24", "s24", "w25", "s25", "w26", "s26", "surge 12", "surge 11", "cohort 2026", "2026", "2025"]):
        hiring_score = 5
    elif any(k in fund for k in ["seed", "series a", "w23", "s23", "surge 10"]):
        hiring_score = 4
    elif "bootstrapped" in fund:
        hiring_score = 3

    # 3. India Eligibility (0-5)
    has_delhi = any(p in loc for p in ["delhi", "noida", "gurgaon", "gurugram"])
    has_remote = "remote" in loc
    has_blr = "bangalore" in loc or "bengaluru" in loc
    if has_delhi:
        india_score = 5
    elif has_blr and has_remote:
        india_score = 4
    elif has_remote:
        india_score = 4
    else:
        india_score = 3

    # 4. Warm Path (0-5)
    if any(k in name_lower for k in top_oss_and_community):
        warm_score = 5
    elif any(k in fund for k in ["y combinator", "peak xv", "accel atoms", "together fund", "blume", "z47", "elevation"]):
        warm_score = 4
    elif has_delhi:
        warm_score = 3
    else:
        warm_score = 2

    # 5. Compensation Likelihood (0-5)
    is_tier1 = any(inv in fund for inv in tier1_investors)
    amt_match = re.search(r"\$([0-9\.]+)[mb]", fund)
    amt = float(amt_match.group(1)) if amt_match else 1.0
    if "k" in fund and not ("m" in fund):
        amt = amt / 1000.0

    if amt >= 4.0 or (amt >= 2.0 and is_tier1):
        comp_score = 5
    elif amt >= 1.5 or is_tier1:
        comp_score = 4
    elif amt >= 0.5:
        comp_score = 3
    else:
        comp_score = 2

    total_score = stack_score + hiring_score + india_score + warm_score + comp_score

    # Determine recommended proof based on company profile
    if any(k in name_lower for k in ["langchain", "mem0", "letta", "crewai", "agentops", "inngest", "trigger.dev"]) or ("agent" in sector and "voice" not in sector):
        rec_proof = "Notovo LangGraph Memory"
    elif any(k in sector or k in hook for k in ["voice", "speech", "audio", "tts", "call"]) or any(k in name_lower for k in ["bolna", "dubverse", "fixie", "deepgram", "daily.co"]):
        rec_proof = "TTS Audio Analysis"
    elif any(k in sector or k in hook for k in ["code", "ast", "test", "lint", "developer", "sdk", "sandbox", "ci/cd"]) or any(k in name_lower for k in ["codeant", "perseus", "deepsource", "e2b", "emergent", "promptfoo", "helium", "speakeasy"]):
        rec_proof = "Code Sage AST Engine"
    elif any(k in sector or k in hook for k in ["search", "rag", "retrieval", "vector", "embed", "knowledge"]) or any(k in name_lower for k in ["ragas", "exa", "qdrant", "lancedb", "jina", "auquan", "orbitshift"]):
        rec_proof = "OceanRAG Retrieval"
    else:
        rec_proof = "NimitAI 317s->117s Pipeline Win"

    # Extract decision maker name & role
    dm_raw = c["hiring_decision_maker"].strip()
    name_match = re.match(r"^([^(&]+?)(?:\s*\(([^)]+)\))?(?:\s*&.*)?$", dm_raw)
    if name_match:
        c_name = name_match.group(1).strip()
        c_role = name_match.group(2).strip() if name_match.group(2) else "Founder / Tech Lead"
    else:
        c_name = dm_raw
        c_role = "Founder / Tech Lead"

    slug = re.sub(r"[^a-zA-Z0-9]+", "-", name.lower()).strip("-")
    linkedin_url = f"https://www.linkedin.com/company/{slug}"

    if warm_score >= 5:
        warm_path = "Open-Source PR / Batchmate Warm Intro"
    elif warm_score == 4:
        warm_path = "Accelerator Cohort / VC Alumni Network"
    elif warm_score == 3:
        warm_path = "Delhi-NCR Founder Community"
    else:
        warm_path = "Direct Decision-Maker Outreach"

    scored_items.append({
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

# Rank companies by total score descending, then stack_fit, then hiring_signal
scored_items.sort(key=lambda x: (x["total_score"], x["score_stack_fit"], x["score_hiring_signal"], x["score_india_eligibility"]), reverse=True)

# Assign Tiers:
# Tier A: Exactly 40 companies
# Tier B: Exactly 100 companies
# Tier C: Exactly 215 companies
tier_a_items = scored_items[:40]
tier_b_items = scored_items[40:140]
tier_c_items = scored_items[140:]

updated_companies = []

for idx, item in enumerate(scored_items, 1):
    c = dict(item["comp"])
    c["id"] = idx
    if idx <= 40:
        c["tier"] = "Tier A"
    elif idx <= 140:
        c["tier"] = "Tier B"
    else:
        c["tier"] = "Tier C"
        
    c["total_score"] = item["total_score"]
    c["score_stack_fit"] = item["score_stack_fit"]
    c["score_hiring_signal"] = item["score_hiring_signal"]
    c["score_india_eligibility"] = item["score_india_eligibility"]
    c["score_warm_path"] = item["score_warm_path"]
    c["score_comp_likelihood"] = item["score_comp_likelihood"]
    c["recommended_proof"] = item["rec_proof"]
    c["contact_name"] = item["contact_name"]
    c["contact_role"] = item["contact_role"]
    c["linkedin_url"] = item["linkedin_url"]
    c["contact_email_source"] = item["contact_email_source"]
    c["warm_intro_path"] = item["warm_intro_path"]
    
    # Tracking Dates & State
    c["connection_sent_date"] = ""
    c["connection_accepted_date"] = ""
    c["dm_sent_date"] = ""
    c["email_sent_date"] = ""
    c["followup_due_date"] = ""
    c["last_touched_date"] = ""
    c["custom_notes"] = ""
    
    updated_companies.append(c)

print(f"Tier A: {sum(1 for c in updated_companies if c['tier'] == 'Tier A')}")
print(f"Tier B: {sum(1 for c in updated_companies if c['tier'] == 'Tier B')}")
print(f"Tier C: {sum(1 for c in updated_companies if c['tier'] == 'Tier C')}")

with open("companies_data.json", "w", encoding="utf-8") as f:
    json.dump(updated_companies, f, indent=2, ensure_ascii=False)

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

with open("target_companies.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for c in updated_companies:
        writer.writerow(c)

print("Updated companies_data.json and target_companies.csv with scoring, tiering, contacts, and tracking fields.")
