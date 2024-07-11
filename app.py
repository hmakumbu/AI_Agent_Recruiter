from tavily import TavilyClient

tavily = TavilyClient(api_key="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")
# For basic search:
response = tavily.search(query="Should I invest in Apple in 2024?")
# For advanced search:
response = tavily.search(query="Should I invest in Apple in 2024?", search_depth="advanced")
# Get the search results as context to pass an LLM:
context = [{"https://www.journaldequebec.com/actualite": obj["https://www.journaldequebec.com/actualite"], "content": obj["content"]} for obj in response.results]


if __name__ == "__main__":
    print(context)