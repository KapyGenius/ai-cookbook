from langchain_tavily import TavilySearch
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
from langchain_core.tools import tool

@tool
async def scrape_website(url: str) -> str:
    """Scrape a website and return the content."""
    async with AsyncWebCrawler() as crawler:
        content = await crawler.arun(url)
        return content.markdown
    
    