# rag/ingest.py
import json
from rag.chroma_client import collection
from rag.embedder import generate_embedding


def normalize_metadata(item: dict) -> dict:
    cleaned = {}

    for key, value in item.items():
        if isinstance(value, (list, dict)):
            cleaned[key] = json.dumps(value)  # store as string
        elif value is None or isinstance(value, (str, int, float, bool)):
            cleaned[key] = value
        else:
            cleaned[key] = str(value)

    return cleaned


def ingest_failures(json_file):
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    for item in data:
        text = f"""
Error Type:
{item.get('error_type', '')}

Error:
{item.get('error_text', '')}

Root Cause:
{item.get('root_cause', '')}

Fix:
{item.get('fix', '')}

Platform:
{item.get('platform', '')}

Tags:
{', '.join(item.get('tags', [])) if isinstance(item.get('tags', []), list) else item.get('tags', '')}
"""

        embedding = generate_embedding(text)
        metadata = normalize_metadata(item)

        collection.add(
            documents=[text],
            embeddings=[embedding],
            metadatas=[metadata],
            ids=[item["id"]]
        )

        print(f"Ingested {item['id']}")


if __name__ == "__main__":
    ingest_failures("historical_failures/sample_failures.json")