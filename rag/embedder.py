import ollama


def generate_embedding(
    text
):

    response = ollama.embeddings(
        model="gte-large:latest",
        prompt=text
    )

    return response["embedding"]