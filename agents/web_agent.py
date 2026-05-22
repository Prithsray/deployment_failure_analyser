from duckduckgo_search import (
    DDGS
)


def search_web_context(
    query
):

    results_data = []

    try:

        with DDGS() as ddgs:

            results = ddgs.text(
                query,
                max_results=3
            )

            for result in results:

                results_data.append(
                    {
                        "title":
                            result.get("title"),

                        "body":
                            result.get("body")
                    }
                )

    except Exception as e:

        print(
            f"Web search failed: {str(e)}"
        )

    return results_data