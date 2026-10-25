# Minimal retrieval baseline using keyword overlap; no external packages needed.
# This demonstrates the RAG stages, not a production embedding search system.
documents = [
    {"source": "python.md", "text": "Python lists are ordered mutable collections."},
    {"source": "sql.md", "text": "SQL joins combine rows from related tables."},
    {"source": "ml.md", "text": "Train test splits estimate generalization on held-out data."},
]

def retrieve(question, docs, top_k=2):
    terms = set(question.lower().split())
    ranked = []
    for doc in docs:
        words = set(doc["text"].lower().replace(".", "").split())
        score = len(terms & words)
        ranked.append((score, doc))
    return [doc for score, doc in sorted(ranked, key=lambda item: item[0], reverse=True)[:top_k] if score > 0]

question = "How do SQL joins combine tables?"
results = retrieve(question, documents)
for item in results:
    print(f"[{item['source']}] {item['text']}")
if not results:
    print("No supporting document found; do not invent an answer.")
