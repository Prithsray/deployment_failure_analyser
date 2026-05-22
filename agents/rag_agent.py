from rag.retriever import (
    retrieve_documents
)


def retrieve_similar_failures(
    query
):

    results = retrieve_documents(
        query
    )

    documents = results.get(
        "documents",
        []
    )

    if documents:

        return documents[0]

    return []