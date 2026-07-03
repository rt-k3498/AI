from firecrawl import Firecrawl
from typing import TypedDict, List, Literal
import os 

firecrawl_api_key = os.getenv("FIRECRAWL_API_KEY")
app = Firecrawl(api_key=firecrawl_api_key)

type Formats = Literal["markdown"]

class SearchResult(TypedDict):
    success: bool
    output: str

def scrape(query: str, formats:List[Formats] = ["markdown"]) -> SearchResult:
    """Tool to scrape web pages using Firecrawl API. It is used for scraping web pages when you have a specific URL to scrape. It returns the scraped content in the specified formats. It should be used to gain information about a specific url or its content.

    Args:
        query (str): URL of the page to scrape
        formats (List[Formats], optional): List of formats to return. Defaults to ["markdown"].

    Returns:
        SearchResult: The scrape result.
    """
    results = app.scrape(query, formats=formats)
    return results
