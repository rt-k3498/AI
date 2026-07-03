from firecrawl import Firecrawl
from typing import TypedDict, List
import os 

firecrawl_api_key = os.getenv("FIRECRAWL_API_KEY")
app = Firecrawl(api_key=firecrawl_api_key)

class _Web(TypedDict):
    url: str
    title: str
    description: str
    position: int

class _Data(TypedDict):
    web: List[_Web]

class SearchResult(TypedDict):
    success: bool
    data: _Data

def search(query: str, limit: int = 5) -> SearchResult:
    """Tool to search the web using Firecrawl API. It is used for searching the web when you have a query and no specific URL to scrape. It returns the top results from the search. Should be used to find the urls related to a query. should not be used to gain information about a specific url or its content.

    Args:
        query (str): Search query
        limit (int, optional): Number of top results returned. Defaults to 5.

    Returns:
        SearchResult: The search result.
    """
    results = app.search(query, limit=limit)
    return results
