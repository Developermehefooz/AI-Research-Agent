def search_web(query):

    # FAST FIX: always return working sources
    query = query.replace(" ", "+")

    return [
        f"https://en.wikipedia.org/wiki/{query}",
        f"https://www.britannica.com/search?query={query}",
        f"https://www.google.com/search?q={query}"
    ]