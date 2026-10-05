import json
import csv

with open("companies_data.json", "r", encoding="utf-8") as f:
    comps = json.load(f)

print(f"Total companies before polish: {len(comps)}")

# Replacements / Fixes dictionary by ID
updates = {
    47: { # Tensorfuse URL fix
        "website": "https://tensorfuse.io",
        "career_page_url": "https://tensorfuse.io",
        "career_email": "rutvij@tensorfuse.io"
    },
    48: { # Rosella -> Phot.ai
        "company_name": "Phot.ai",
        "website": "https://phot.ai",
        "domain_sector": "AI Photo Editing, Visual Generative Tools & Design Engine",
        "employee_count": "15-30",
        "funding_stage_investors": "Seed $1.5M (prominent AI & consumer angels)",
        "work_model_location": "Delhi-NCR (Gurugram) / Hybrid",
        "career_page_url": "https://phot.ai/careers",
        "career_email": "lakshay@phot.ai",
        "hiring_decision_maker": "Lakshay Goyal (Founder & CEO)",
        "nalin_tech_fit_hook": "Client-side image canvas manipulation and GPU rendering pipelines in React, connecting to Nalin's Voyatri project and frontend UI engineering.",
        "outreach_status": "To Contact"
    },
    59: { # Round1 -> Dubverse.ai
        "company_name": "Dubverse.ai",
        "website": "https://dubverse.ai",
        "domain_sector": "Generative AI Multilingual Video Dubbing & Synthetic Speech Studio",
        "employee_count": "12-25",
        "funding_stage_investors": "Seed $1.2M (Kalaari Capital)",
        "work_model_location": "Delhi-NCR (Gurugram) / Hybrid",
        "career_page_url": "https://dubverse.ai/careers",
        "career_email": "varun@dubverse.ai",
        "hiring_decision_maker": "Varun Saxena (Co-Founder & CEO) & Anuja Dhawan (Co-Founder)",
        "nalin_tech_fit_hook": "Indic speech synthesis and subtitle alignment pipelines, directly relating to Nalin's TTS analysis and audio processing at NimitAI.",
        "outreach_status": "To Contact"
    },
    64: { # Retape -> LangChain
        "company_name": "LangChain",
        "website": "https://www.langchain.com",
        "domain_sector": "LLM Application Framework, LangGraph Multi-Agent Orchestration & LangSmith",
        "employee_count": "35-60",
        "funding_stage_investors": "Series A $25M (Benchmark, Sequoia)",
        "work_model_location": "Fully Remote (India)",
        "career_page_url": "https://www.langchain.com/careers",
        "career_email": "harrison@langchain.dev",
        "hiring_decision_maker": "Harrison Chase (Co-Founder & CEO) & Ankush Gola (Co-Founder)",
        "nalin_tech_fit_hook": "Graph-based state persistence, cycles, and multi-agent coordination, directly connecting to Nalin's production LangGraph implementation in Notovo.",
        "outreach_status": "To Contact"
    },
    98: { # VedaLabs -> PostHog
        "company_name": "PostHog",
        "website": "https://posthog.com",
        "domain_sector": "Open-Source Product Analytics, Session Replay & Feature Flags Platform",
        "employee_count": "45-75",
        "funding_stage_investors": "Series B $27M (GV, Y Combinator)",
        "work_model_location": "Fully Remote (India)",
        "career_page_url": "https://posthog.com/careers",
        "career_email": "james@posthog.com",
        "hiring_decision_maker": "James Hawkins (Co-Founder & CEO) & Tim Glaser (Co-Founder & CTO)",
        "nalin_tech_fit_hook": "High-throughput telemetry ingestion and ClickHouse analytics queries, matching Nalin's database footprint and query optimization.",
        "outreach_status": "To Contact"
    },
    134: { # Persistence Labs -> Trigger.dev
        "company_name": "Trigger.dev",
        "website": "https://trigger.dev",
        "domain_sector": "Open-Source Background Jobs & Long-Running Workflow Engine for Next.js",
        "employee_count": "8-18",
        "funding_stage_investors": "Seed $3M (Y Combinator W23)",
        "work_model_location": "Fully Remote (India)",
        "career_page_url": "https://trigger.dev/careers",
        "career_email": "matt@trigger.dev",
        "hiring_decision_maker": "Matt Aitken (Co-Founder & CEO)",
        "nalin_tech_fit_hook": "Durable task execution and async queue scaling in TypeScript and Python, directly matching Nalin's backend architecture experience.",
        "outreach_status": "To Contact"
    },
    137: { # Zingroll -> Cal.com
        "company_name": "Cal.com",
        "website": "https://cal.com",
        "domain_sector": "Open-Source Scheduling Infrastructure, Next.js & PostgreSQL Calendar Engine",
        "employee_count": "25-45",
        "funding_stage_investors": "Series A $25M (Seven Seven Six, Alexis Ohanian)",
        "work_model_location": "Fully Remote (India)",
        "career_page_url": "https://cal.com/careers",
        "career_email": "peer@cal.com",
        "hiring_decision_maker": "Peer Richelsen (Co-Founder & Co-CEO)",
        "nalin_tech_fit_hook": "Multi-tenant PostgreSQL scheduling state machines and Next.js full-stack app engineering, directly matching Nalin's core technical stack.",
        "outreach_status": "To Contact"
    },
    141: { # Meritic -> Prisma
        "company_name": "Prisma",
        "website": "https://www.prisma.io",
        "domain_sector": "Next-Generation Type-Safe ORM & Cloud Database Infrastructure",
        "employee_count": "60-90",
        "funding_stage_investors": "Series B $40M (Altimeter Capital, Kleiner Perkins)",
        "work_model_location": "Fully Remote (India)",
        "career_page_url": "https://www.prisma.io/careers",
        "career_email": "johannes@prisma.io",
        "hiring_decision_maker": "Johannes Schickling (Co-Founder & CEO)",
        "nalin_tech_fit_hook": "Type-safe SQL query generation and schema migration automation, directly connecting to Nalin's Azure PostgreSQL migration work.",
        "outreach_status": "To Contact"
    },
    143: { # Runable -> Inngest
        "company_name": "Inngest",
        "website": "https://www.inngest.com",
        "domain_sector": "Durable Workflow Orchestration & Event-Driven Execution for AI Agents",
        "employee_count": "15-30",
        "funding_stage_investors": "Series A $9M (Andreessen Horowitz)",
        "work_model_location": "Fully Remote (India)",
        "career_page_url": "https://www.inngest.com/careers",
        "career_email": "tony@inngest.com",
        "hiring_decision_maker": "Tony Holdstock-Brown (Co-Founder & CEO)",
        "nalin_tech_fit_hook": "Stateful agent step retries and fan-out event queues, aligning with Nalin's LangGraph and async Python backend development.",
        "outreach_status": "To Contact"
    },
    158: { # Architect Labs -> Mintlify
        "company_name": "Mintlify",
        "website": "https://mintlify.com",
        "domain_sector": "AI-Powered Modern Developer Documentation Engine & Interactive API Docs",
        "employee_count": "20-40",
        "funding_stage_investors": "Series A $18.5M (Andreessen Horowitz, Y Combinator W22)",
        "work_model_location": "Fully Remote (India)",
        "career_page_url": "https://mintlify.com/careers",
        "career_email": "han@mintlify.com",
        "hiring_decision_maker": "Han Wang (Co-Founder & CEO) & Hahnbee Choi (Co-Founder & CTO)",
        "nalin_tech_fit_hook": "MDX component rendering and automated OpenAPI doc generation, fitting Nalin's Next.js frontend and AST code analysis skills.",
        "outreach_status": "To Contact"
    },
    160: { # Truffle AI -> Resend
        "company_name": "Resend",
        "website": "https://resend.com",
        "domain_sector": "Developer Email API, React Email Components & High-Deliverability Cloud",
        "employee_count": "12-25",
        "funding_stage_investors": "Seed $3M (Y Combinator W23, prominent devtool angels)",
        "work_model_location": "Fully Remote (India)",
        "career_page_url": "https://resend.com/careers",
        "career_email": "zeno@resend.com",
        "hiring_decision_maker": "Zeno Rocha (Founder & CEO)",
        "nalin_tech_fit_hook": "React component email rendering and sub-second webhook deliveries, matching Nalin's Next.js full-stack product engineering.",
        "outreach_status": "To Contact"
    },
    162: { # Riffle -> Daily.co
        "company_name": "Daily.co",
        "website": "https://www.daily.co",
        "domain_sector": "Real-Time WebRTC Video Infrastructure & Sub-Second Voice AI SDKs",
        "employee_count": "45-75",
        "funding_stage_investors": "Series B $40M (Tiger Global, Lachy Groom)",
        "work_model_location": "Fully Remote (India)",
        "career_page_url": "https://www.daily.co/careers",
        "career_email": "kweku@daily.co",
        "hiring_decision_maker": "Kweku Vanderpuye (Co-Founder & CEO)",
        "nalin_tech_fit_hook": "Sub-200ms WebRTC voice agent pipelines and streaming audio transcription, matching Nalin's FastAPI and TTS analysis work.",
        "outreach_status": "To Contact"
    },
    163: { # Resollect -> Upstash
        "company_name": "Upstash",
        "website": "https://upstash.com",
        "domain_sector": "Serverless Redis, Kafka & Vector Database for Edge & LLM Applications",
        "employee_count": "15-30",
        "funding_stage_investors": "Seed $1.9M (prominent cloud & edge angels)",
        "work_model_location": "Fully Remote (India)",
        "career_page_url": "https://upstash.com/careers",
        "career_email": "enes@upstash.com",
        "hiring_decision_maker": "Enes Akar (Founder & CEO)",
        "nalin_tech_fit_hook": "Serverless rate limiting and Redis caching for Next.js and LLM prompt tokens, matching Nalin's 63% latency reduction achievements.",
        "outreach_status": "To Contact"
    },
    174: { # Brekfuz -> Fixie.ai
        "company_name": "Fixie.ai",
        "website": "https://www.fixie.ai",
        "domain_sector": "Ultravox Real-Time Speech-Native Voice AI Architecture & Agent Framework",
        "employee_count": "15-35",
        "funding_stage_investors": "Seed $17M (Redpoint Ventures, Madrona)",
        "work_model_location": "Fully Remote (India)",
        "career_page_url": "https://www.fixie.ai/careers",
        "career_email": "matt@fixie.ai",
        "hiring_decision_maker": "Matt Welsh (Co-Founder & CEO)",
        "nalin_tech_fit_hook": "End-to-end voice-to-voice neural processing without intermediate text serialization, matching Nalin's audio TTS workflow background.",
        "outreach_status": "To Contact"
    },
    201: { # Galileo URL fix
        "website": "https://galileo.ai",
        "career_page_url": "https://galileo.ai/careers",
        "career_email": "vikram@galileo.ai"
    },
    224: { # Vault Wealth -> Jina AI
        "company_name": "Jina AI",
        "website": "https://jina.ai",
        "domain_sector": "Multimodal AI Search Foundation, Rerankers & Reader API for LLMs",
        "employee_count": "30-55",
        "funding_stage_investors": "Series A $37M (Canaan Partners, GGV Capital)",
        "work_model_location": "Fully Remote (India)",
        "career_page_url": "https://jina.ai/careers",
        "career_email": "han@jina.ai",
        "hiring_decision_maker": "Dr. Han Xiao (Founder & CEO)",
        "nalin_tech_fit_hook": "Semantic reranking algorithms and web document parsing for production RAG, connecting to Nalin's 117s LLM latency optimization.",
        "outreach_status": "To Contact"
    },
    236: { # Gan.ai -> Relevance AI
        "company_name": "Relevance AI",
        "website": "https://relevanceai.com",
        "domain_sector": "Autonomous AI Workforce Platform & Multi-Agent Operations Studio",
        "employee_count": "25-50",
        "funding_stage_investors": "Series A $10M (King River Capital, Peak XV)",
        "work_model_location": "Fully Remote (India)",
        "career_page_url": "https://relevanceai.com/careers",
        "career_email": "jacky@relevanceai.com",
        "hiring_decision_maker": "Jacky Koh (Co-Founder & CEO) & Daniel Khachiyan (Co-Founder)",
        "nalin_tech_fit_hook": "Agent tool delegation and multi-step reasoning trees, directly matching Nalin's LangGraph and full-stack product experience.",
        "outreach_status": "To Contact"
    },
    250: { # Synapsica -> Athina AI
        "company_name": "Athina AI",
        "website": "https://athina.ai",
        "domain_sector": "Automated Testing, Monitoring & Evaluation Platform for Production LLMs",
        "employee_count": "8-18",
        "funding_stage_investors": "Seed $1.5M (Y Combinator W23)",
        "work_model_location": "Bengaluru / Fully Remote (India)",
        "career_page_url": "https://athina.ai/careers",
        "career_email": "shiv@athina.ai",
        "hiring_decision_maker": "Shiv Sakhuja (Co-Founder & CEO) & Akshat Vaidya (Co-Founder & CTO)",
        "nalin_tech_fit_hook": "RAG hallucination detection and prompt assertion suites, directly related to Nalin's LangGraph and vector search pipelines.",
        "outreach_status": "To Contact"
    },
    285: { # Sing One Song -> Qdrant
        "company_name": "Qdrant",
        "website": "https://qdrant.tech",
        "domain_sector": "Rust-Based Open-Source Vector Search Engine & Payload Filtering",
        "employee_count": "25-50",
        "funding_stage_investors": "Series A $28M (Spark Capital)",
        "work_model_location": "Fully Remote (India)",
        "career_page_url": "https://qdrant.tech/careers",
        "career_email": "andre@qdrant.com",
        "hiring_decision_maker": "Andre Zayarni (Co-Founder & CEO)",
        "nalin_tech_fit_hook": "High-throughput vector indexing and hybrid keyword search, connecting to Nalin's database performance tuning and fast search retrieval.",
        "outreach_status": "To Contact"
    },
    289: { # Tartan URL fix
        "website": "https://www.tartanhq.com",
        "career_page_url": "https://www.tartanhq.com/careers",
        "career_email": "prmeet@tartanhq.com"
    },
    303: { # Adopt AI -> Helicone
        "company_name": "Helicone",
        "website": "https://www.helicone.ai",
        "domain_sector": "LLM Observability, Cost Governance & Smart Caching Gateway",
        "employee_count": "8-18",
        "funding_stage_investors": "Seed $2M (Y Combinator W23)",
        "work_model_location": "Fully Remote (India)",
        "career_page_url": "https://www.helicone.ai/careers",
        "career_email": "justin@helicone.ai",
        "hiring_decision_maker": "Justin Torre (Co-Founder & CEO) & Cole Gottdank (Co-Founder & CTO)",
        "nalin_tech_fit_hook": "High-throughput API reverse proxies and semantic caching, directly matching Nalin's 63% latency reduction on LLM pipelines.",
        "outreach_status": "To Contact"
    },
    306: { # ALT Fashion -> Firecrawl
        "company_name": "Firecrawl",
        "website": "https://www.firecrawl.dev",
        "domain_sector": "Web Scraping & Clean Markdown Extraction API for LLM Ingestion",
        "employee_count": "8-18",
        "funding_stage_investors": "Seed $2.5M (Y Combinator S24)",
        "work_model_location": "Fully Remote (India)",
        "career_page_url": "https://www.firecrawl.dev",
        "career_email": "founders@firecrawl.dev",
        "hiring_decision_maker": "Founding Engineering Team",
        "nalin_tech_fit_hook": "Headless browser scraping engines and DOM to Markdown pipelines, connecting to Nalin's data ingestion and cleanup experience.",
        "outreach_status": "To Contact"
    },
    311: { # HireBound -> E2B
        "company_name": "E2B",
        "website": "https://e2b.dev",
        "domain_sector": "Secure Cloud Sandboxes & Execution Environments for AI Agents",
        "employee_count": "8-18",
        "funding_stage_investors": "Seed $2.5M (Y Combinator W24)",
        "work_model_location": "Fully Remote (India)",
        "career_page_url": "https://e2b.dev/careers",
        "career_email": "founders@e2b.dev",
        "hiring_decision_maker": "Founding Engineering Team",
        "nalin_tech_fit_hook": "Micro-VM container lifecycle management for LLM code execution, mapping to Nalin's AST code analysis and runtime execution security.",
        "outreach_status": "To Contact"
    }
}

for c in comps:
    cid = c["id"]
    if cid in updates:
        c.update(updates[cid])

with open("companies_data.json", "w", encoding="utf-8") as f:
    json.dump(comps, f, indent=2, ensure_ascii=False)

# Export to target_companies.csv
fieldnames = [
    "id", "company_name", "website", "domain_sector",
    "employee_count", "funding_stage_investors", "work_model_location",
    "career_page_url", "career_email", "hiring_decision_maker",
    "nalin_tech_fit_hook", "outreach_status"
]

with open("target_companies.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for comp in comps:
        writer.writerow(comp)

print("Applied polished updates to companies_data.json and target_companies.csv.")
