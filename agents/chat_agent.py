from config.settings import (
    invoke_with_fallback
)


def start_chat(
    analysis_context
):

    print(
        "\nChat mode started."
    )

    print(
        "Type 'exit' to quit.\n"
    )

    while True:

        user_query = input(
            "\nYou: "
        )

        if (
            user_query.lower()
            == "exit"
        ):
            break

        prompt = f"""
You are an AI DevOps assistant.

Deployment Analysis Context:
{analysis_context}

User Follow-up Question:
{user_query}

Answer clearly and concisely.
"""

        response = invoke_with_fallback(
            prompt
        )

        print(
            f"\nAI: {response['response']}"
        )