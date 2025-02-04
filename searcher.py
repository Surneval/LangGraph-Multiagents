"""
LangGraph Multi-Agent Web Search System using GigaChat
"""

import json
import time
import requests
from bs4 import BeautifulSoup
from googlesearch import search
from gigachat import GigaChat
from langgraph.graph import StateGraph


def load_keys(config_path="keys.conf"):
    with open(config_path, "r", encoding="utf-8") as f:
        keys_json = json.load(f)
        return keys_json["giga"]["key"]

giga_key = load_keys("keys.conf")
giga = GigaChat(
    credentials=giga_key,
    scope="GIGACHAT_API_PERS",
    model="GigaChat",
    verify_ssl_certs=False
)


# corrector agent
def correct_text(state):

    if state["corrected_query"] is None:
        response = giga.chat("Correct: " + state["query"])
        state["corrected_query"] = response.choices[0].message.content.strip()
        print(f"[CorrectorAgent] Corrected Query: {state['corrected_query']}")
    else:
        for url, text in state["scraped_content"].items():
            response = giga.chat("Correct: " + text)
            state["corrected_content"][url] = response.choices[0].message.content.strip()
            print(f"[CorrectorAgent] Corrected Text for {url}")
    return state

# web search agent
def search_google(state):
    print(f"[WebSearchAgent] Searching for: '{state['corrected_query']}'")
    try:
        state["urls"] = list(search(state["corrected_query"], num_results=10))
    except Exception as e:
        print(f"[WebSearchAgent] Google search failed: {e}")
        state["urls"] = []
    print(f"[WebSearchAgent] Found URLs: {state['urls']}")
    return state

# web scraper agent
def scrape_web_pages(state):
    for url in state["urls"]:
        if not url.startswith("http"):
            print(f"[WebScrapperAgent] Skipping invalid URL: {url}")
            continue
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            # Extract text from all <p> tags (limit to 1000 characters)
            text = " ".join([p.text for p in soup.find_all("p")])[:1000]
            state["scraped_content"][url] = text
            print(f"[WebScrapperAgent] Scraped {len(text)} characters from {url}")
        except Exception as e:
            print(f"[WebScrapperAgent] Failed to scrape {url}: {e}")
            state["scraped_content"][url] = "Failed to scrape content."
    return state

# summarizer agent
def summarize_text(state):
    for url, text in state["corrected_content"].items():
        if len(text) < 50 or "scraped content" in text.lower():
            summary = "No useful content available for summarization."
        else:
            response = giga.chat("Summarize: " + text)
            summary = response.choices[0].message.content.strip()
        state["summaries"][url] = summary
        print(f"[SummarizerAgent] Summary for {url}: {summary}")
    return state

# final Report + saving results
def generate_report(state):
    """
    Generates a final report with URLs and their corresponding summaries.
    Saves the results to a file: search_results.txt.
    """
    filename = "search_results.txt"
    
    with open(filename, "w", encoding="utf-8") as file:
        file.write("=== Final Report ===\n")
        for url, summary in state["summaries"].items():
            report_entry = f"\nURL: {url}\nSummary: {summary}\n"
            print(report_entry)
            file.write(report_entry)
    
    print(f"\n Search results saved to {filename}\n")
    return state

graph = StateGraph(dict)

graph.add_node("Corrector", correct_text)
graph.add_node("WebSearch", search_google)
graph.add_node("WebScrapper", scrape_web_pages)
graph.add_node("CorrectorContent", correct_text)
graph.add_node("Summarizer", summarize_text)
graph.add_node("FinalReport", generate_report)

# workflow connections.
graph.add_edge("Corrector", "WebSearch")
graph.add_edge("WebSearch", "WebScrapper")
graph.add_edge("WebScrapper", "CorrectorContent")
graph.add_edge("CorrectorContent", "Summarizer")

# specify a conditional edge to the final report.
graph.add_conditional_edges("Summarizer", lambda state: "FinalReport")

# set the entry point.
graph.set_entry_point("Corrector")

# compile the workflow.
executor = graph.compile()

def main():
    print("Welcome to the LangGraph Web Search System.\n")
    user_query = input("Enter your search query: ")

    state = {
        "query": user_query,
        "corrected_query": None,
        "urls": [],
        "scraped_content": {},
        "corrected_content": {},
        "summaries": {}
    }
    executor.invoke(state)

if __name__ == "__main__":
    main()
