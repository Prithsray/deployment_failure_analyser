from rag.chroma_client import (
    collection
)

from rag.embedder import (
    generate_embedding
)


def retrieve_documents(
    query,
    top_k=3
):

    embedding = generate_embedding(
        query
    )

    return collection.query(
        query_embeddings=[embedding],
        n_results=top_k
    )