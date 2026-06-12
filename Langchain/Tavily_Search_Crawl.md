# Tavily + LangChain Web Search & Scraping Guide

## Installation

```bash
pip install -U langchain langchain-tavily
```

Set your Tavily API key:

```bash
export TAVILY_API_KEY="your_api_key"
```

or in Python:

```python
import os

os.environ["TAVILY_API_KEY"] = "your_api_key"
```

---

# Example 1: Web Search

```python
from langchain_tavily import TavilySearch

search_tool = TavilySearch(
    max_results=5,
    topic="general",
    search_depth="advanced",
    include_answer=True,
    include_raw_content=True
)

result = search_tool.invoke({
    "query": "Latest LLM architectures in 2025"
})

print(result)
```

---

# Example 2: Extract Content from a Webpage (Scraping)

```python
from langchain_tavily import TavilyExtract

extract_tool = TavilyExtract(
    extract_depth="advanced",
    format="markdown"
)

result = extract_tool.invoke({
    "urls": [
        "https://en.wikipedia.org/wiki/Large_language_model"
    ]
})

print(result["results"][0]["raw_content"])
```

This fetches the webpage and returns cleaned text that can be used for RAG or LLM applications.

---

# Example 3: Crawl an Entire Website

```python
from langchain_tavily import TavilyCrawl

crawl_tool = TavilyCrawl(
    max_depth=2,
    max_breadth=5,
    limit=20
)

result = crawl_tool.invoke({
    "url": "https://docs.langchain.com"
})

for page in result["results"]:
    print("=" * 50)
    print(page["url"])
    print(page["raw_content"][:500])
```

This follows links from the starting page and extracts content from multiple pages.

---

# Example 4: Search → Extract Pipeline

```python
from langchain_tavily import TavilySearch, TavilyExtract

search = TavilySearch(max_results=3)
extract = TavilyExtract(format="markdown")

search_results = search.invoke({
    "query": "LangGraph tutorial"
})

urls = [item["url"] for item in search_results["results"]]

pages = extract.invoke({
    "urls": urls
})

for page in pages["results"]:
    print(page["url"])
    print(page["raw_content"][:1000])
    print()
```

This workflow:

1. Searches the web.
2. Collects the URLs.
3. Downloads and cleans the webpage contents.

---

# Example 5: Using Tavily in a LangChain Agent

```python
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

llm = ChatOpenAI(model="gpt-4.1")

search_tool = TavilySearch(
    max_results=5,
    topic="general"
)

agent = create_agent(
    model=llm,
    tools=[search_tool]
)

response = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": "Who won the latest Nobel Prize in Physics?"
        }
    ]
})

print(response)
```

---

# Typical RAG Pipeline Using Tavily

```text
                User Query
                     │
                     ▼
              TavilySearch
                     │
                     ▼
                  URLs
                     │
                     ▼
              TavilyExtract
                     │
                     ▼
          Clean Markdown/Text
                     │
                     ▼
                 Chunking
                     │
                     ▼
                Embedding
                     │
                     ▼
                 Vector DB
                     │
                     ▼
                     LLM
```

---

# Summary

## Search the Web

```python
from langchain_tavily import TavilySearch

search = TavilySearch(max_results=5)

result = search.invoke({
    "query": "your query"
})
```

---

## Scrape Specific URLs

```python
from langchain_tavily import TavilyExtract

extract = TavilyExtract(format="markdown")

result = extract.invoke({
    "urls": [
        "https://example.com"
    ]
})
```

---

## Crawl an Entire Website

```python
from langchain_tavily import TavilyCrawl

crawl = TavilyCrawl(
    max_depth=2,
    max_breadth=5,
    limit=20
)

result = crawl.invoke({
    "url": "https://example.com"
})
```

---

## Recommended Workflow for Agentic Applications

```
User Question
      │
      ▼
 TavilySearch
      │
      ▼
 Relevant URLs
      │
      ▼
 TavilyExtract
      │
      ▼
 Clean Text
      │
      ▼
 LLM / RAG / Agent
```

This is the recommended architecture for building web-aware AI agents using LangChain and Tavily.
