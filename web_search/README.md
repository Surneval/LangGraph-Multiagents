# LangGraph Multi-Agent Web Search System using GigaChat

## Overview

This project implements a multi-agent system using LangGraph to perform automated web searching, web scraping, text correction, and summarization with the help of GigaChat. The system follows a structured pipeline where each task is handled by a different agent.

## Workflow
	1.	CorrectorAgent: Corrects the user input for spelling or formatting errors.
	2.	WebSearchAgent: Performs a Google search for the corrected query and retrieves the top 10 URLs.
	3.	WebScrapperAgent: Scrapes text content from the retrieved URLs.
	4.	CorrectorAgent (again): Ensures that the scraped text is clean and properly formatted.
	5.	SummarizerAgent: Summarizes the cleaned web content into short, concise text.
	6.	FinalReportAgent: Saves the results (URLs + summaries) into a text file (search_results.txt).

## 📌 Features
	•	Automated Web Search using Google Search API.
	•	Web Scraping with BeautifulSoup to extract page content.
	•	Text Correction using GigaChat.
	•	Summarization using GigaChat to generate concise summaries.
	•	Workflow Managed by LangGraph ensuring smooth execution.
	•	Saves Final Report to a TXT file (search_results.txt).

## 🛠️ Installation

### 1️⃣ Clone the Repository

git clone git@github.com:Surneval/LangGraph-Multiagents.git
cd LangGraph-Multiagents

### 2️⃣ Install Dependencies

Make sure you have Python 3.9+ installed, then run:

pip install -r requirements.txt

### 3️⃣ Setup API Keys

Create a keys.conf file in the project directory and add your GigaChat API credentials:

{
  "giga": {
    "key": "YOUR_GIGACHAT_KEY"
  }
}

## 🚀 Usage

Run the Script

python searcher.py

Example Input

Enter your search query: What is cybersecurity?

Example Output

## Console Output

[CorrectorAgent] Corrected Query: What is cybersecurity?
[WebSearchAgent] Searching Google...
[WebSearchAgent] Found URLs: ['https://en.wikipedia.org/wiki/Cybersecurity', 'https://www.cisco.com/cybersecurity']
[WebScrapperAgent] Scraping content from: https://en.wikipedia.org/wiki/Cybersecurity
[SummarizerAgent] Summary: Cybersecurity is the practice of protecting systems from cyber threats...
✅ Search results saved to search_results.txt

## Saved Report (search_results.txt)

=== Final Report ===

URL: https://en.wikipedia.org/wiki/Cybersecurity
Summary: Cybersecurity is the practice of protecting systems from cyber threats. It involves encryption, firewalls...

URL: https://www.cisco.com/cybersecurity
Summary: Cybersecurity refers to the protection of digital systems and networks from unauthorized access...

## ⚙️ Architecture

This project uses LangGraph to define a graph-based workflow where each agent is a node and the execution follows a structured pipeline.

Agent Name	Function
CorrectorAgent	Corrects the user input
WebSearchAgent	Searches Google and retrieves URLs
WebScrapperAgent	Scrapes content from webpages
CorrectorAgent	Cleans up scraped text
SummarizerAgent	Summarizes the extracted text
FinalReportAgent	Saves results into a file

## 🛠 Dependencies
	•	LangGraph (Workflow orchestration)
	•	GigaChat (Language model for text correction and summarization)
	•	BeautifulSoup4 (Web scraping)
	•	Requests (HTTP requests for web scraping)
	•	Googlesearch-Python (Google search automation)

## 📜 License

This project is licensed under the MIT License. You are free to modify and distribute it.

## 🙌 Contributing

Feel free to open issues, submit pull requests, or suggest improvements. Contributions are always welcome!

## 📞 Contact

For questions or support, feel free to contact:
	•	GitHub: @Surneval
	•	Email: nadia.trusova@yahoo.com
	•	Telegram: @surneval


