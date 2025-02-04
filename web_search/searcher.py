# #!/usr/bin/env python3
# """
# Multiagent Web Searching System using a Lang-Graph Approach with Google Search and GigaChat

# Agents:
#     - Coordinator Agent: Orchestrates the flow.
#     - Corrector Agent: Corrects text (e.g. spelling, symbols, HTML tags) via GigaChat.
#     - Web-Search Agent: Uses Google search to return top 10 URLs.
#     - Web-Scrapper Agent: Scrapes web pages for content.
#     - Summarizer Agent: Summarizes the scraped content via GigaChat.
# """

# import json
# import time
# import torch
# from googlesearch import search
# from gigachat import GigaChat  # Ensure your GigaChat library is installed and available
# import requests
# from bs4 import BeautifulSoup   

# # ----- Load keys and initialize the GigaChat agent -----
# def load_keys(config_path='keys.conf'):
#     with open(config_path, 'r', encoding='utf-8') as f:
#         keys_json = json.load(f)
#         giga_key = keys_json['giga']['key']
#     return giga_key

# def create_gigachat_agent(giga_key):
#     giga = GigaChat(
#         credentials=giga_key,
#         scope="GIGACHAT_API_PERS",
#         model="GigaChat",
#         verify_ssl_certs=False
#     )
#     return giga

# giga_key = load_keys('keys.conf')
# giga = create_gigachat_agent(giga_key)
# device = torch.device("mps") if torch.backends.mps.is_available() else (torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu"))

# # ----- Agent-2: Corrector Agent -----
# # ----- Agent-2: Corrector Agent -----
# class CorrectorAgent:
#     def process(self, input_data):
#         if isinstance(input_data, dict):
#             corrected_dict = {}
#             for url, text in input_data.items():
#                 prompt = "Correct: " + text
#                 response = giga.chat(prompt)
#                 corrected_text = response.choices[0].message.content.strip()  # ✅ Extract text only
#                 corrected_dict[url] = corrected_text
#             return corrected_dict
#         elif isinstance(input_data, str):
#             prompt = "Correct: " + input_data
#             response = giga.chat(prompt)
#             corrected_text = response.choices[0].message.content.strip()  # ✅ Extract text only
#             print(f"[CorrectorAgent] Corrected text: {corrected_text}")
#             return corrected_text
#         else:
#             raise ValueError("Unsupported input type for CorrectorAgent")

# # ----- Agent-3: Web-Search Agent (Google Search) -----
# class WebSearchAgent:
#     def process(self, query):
#         print(f"[WebSearchAgent] Searching Google for query: '{query}'")
#         urls = []
#         try:
#             results = list(search(query, num_results=10)) 
#             urls.extend(results)
#         except Exception as e:
#             print(f"[WebSearchAgent] Error occurred during search: {e}")
        
#         print(f"[WebSearchAgent] Found URLs: {urls}")
#         return urls

# # ----- Agent-4: Web-Scrapper Agent -----
# class WebScrapperAgent:
#     def process(self, urls):
#         scraped_results = {}
#         for url in urls:
#             if not url.startswith("http"):  # Skip invalid URLs
#                 print(f"[WebScrapperAgent] Skipping invalid URL: {url}")
#                 continue

#             print(f"[WebScrapperAgent] Scraping URL: {url}")
#             try:
#                 response = requests.get(url, timeout=5)
#                 response.raise_for_status()  # Ensure request was successful
#                 soup = BeautifulSoup(response.text, "html.parser")
#                 text = " ".join([p.text for p in soup.find_all("p")])  # Extract meaningful text
#                 scraped_results[url] = text[:1000]  # Limit text size for better summarization
#             except Exception as e:
#                 print(f"[WebScrapperAgent] Failed to scrape {url}: {e}")
#                 scraped_results[url] = "Failed to scrape content."
#         print(f"[WebScrapperAgent] Completed scraping. Results collected for {len(scraped_results)} URLs.")
#         return scraped_results

# # ----- Agent-5: Summarizer Agent -----
# class SummarizerAgent:
#     def process(self, corrected_texts):
#         summaries = {}
#         for url, text in corrected_texts.items():
#             prompt = "Summarize: " + text
#             if len(text) < 50 or "scraped content" in text.lower():  # Skip bad summaries
#                 summary = "No useful content available for summarization."
#             else:
#                 response = giga.chat(prompt)
#                 summary = response.choices[0].message.content.strip()
            
#             print(f"[SummarizerAgent] Summary for {url}: {summary}")
#             summaries[url] = summary
#         return summaries

# # ----- Agent-1: Coordinator Agent -----
# class CoordinatorAgent:
#     def __init__(self):
#         self.corrector = CorrectorAgent()
#         self.web_search = WebSearchAgent()
#         self.web_scrapper = WebScrapperAgent()
#         self.summarizer = SummarizerAgent()
    
#     def run(self, user_request):
#         print("[CoordinatorAgent] Received user request.")
#         # Step 1: Correct the user request.
#         corrected_request = self.corrector.process(user_request)
#         # Step 2: Perform a Google search.
#         urls = self.web_search.process(corrected_request)
#         # Step 3: Scrape the resulting URLs.
#         scraped_texts = self.web_scrapper.process(urls)
#         # Step 4: Correct the scraped texts.
#         corrected_scraped_texts = self.corrector.process(scraped_texts)
#         # Step 5: Summarize the corrected scraped texts.
#         summaries = self.summarizer.process(corrected_scraped_texts)
#         # Step 6: Prepare the final report.
#         report_lines = ["\n=== Final Report ==="]
#         for url in urls:
#             summary = summaries.get(url, "No summary available.")
#             report_lines.append(f"\nURL: {url}\nSummary: {summary}\n")
#         report = "\n".join(report_lines)
#         print("[CoordinatorAgent] Final report prepared.")
#         return report

# # ----- Main function -----
# def main():
#     print("Welcome to the Multiagent Web Searching System.\n")
#     user_query = input("Enter your search query: ")
#     coordinator = CoordinatorAgent()
#     final_report = coordinator.run(user_query)
#     print(final_report)

# if __name__ == "__main__":
#     main()




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