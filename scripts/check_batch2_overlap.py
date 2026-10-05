import json

with open("companies_data.json", "r", encoding="utf-8") as f:
    comps = json.load(f)

existing_names = set(c["company_name"].lower() for c in comps)

batch2_candidates = [
    "Promptfoo", "Braintrust", "Openlayer", "Galileo", "Vellum AI",
    "Deepgram", "Chroma", "Qdrant", "Zilliz", "Deepset",
    "Vault Wealth", "Cybrilla", "Finster", "Ignosis", "Skoob",
    "Spintly", "Asets", "ContraVault AI", "Helium", "Capitol AI",
    "Gibran", "Chaotix AI", "DreamTeam", "Nava AI", "Sing One Song",
    "PowerUp Money", "Xccelera AI", "Adopt AI", "ALT Fashion", "Bookee",
    "HireBound", "Infer.so", "Enkrypt AI", "DeepSource", "Arize AI",
    "Coactive AI", "Encord", "Qwak", "Fireworks AI", "Anyscale",
    "Predibase", "Weights & Biases", "Arize Phoenix", "Vespa.ai", "Weaviate",
    "Pinecone", "Cerebrium", "TrueMedia"
]

print(f"Total batch 2 candidates: {len(batch2_candidates)}")
overlap = [c for c in batch2_candidates if c.lower() in existing_names]
print(f"Overlap with existing dataset: {overlap}")
