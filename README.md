## LangGraph Multi-Agent Systems 🚀

Welcome to the Multi-Agent Systems Repository!

This repository is dedicated to developing and experimenting with multi-agent systems using LangGraph, GigaChat, and other advanced AI tools.

Each system consists of multiple autonomous agents, each responsible for a specific task, working together in a structured workflow.

## 📌 Repository Structure

This repository is designed to support multiple multi-agent systems, each in its own directory. Below is the planned structure:

📂 LangGraph-Multiagents/

│── 📂 web_search/        # Web Searcher, Scraper, Corrector, Summarizer Agents

│── 📂 chatbot-agent/            # Conversational AI Agent

│── 📂 translation-agent/        # AI-Powered Multilingual Translator

│── 📂 data-cleaning-agent/      # Automated Data Preprocessing Pipeline

│── README.md                    # This documentation

│── requirements.txt              # Required dependencies

Each folder contains a LangGraph-powered multi-agent system designed for a specific task.

### 🚀 Multi-Agent Systems

Below are the multi-agent systems that will be developed in this repository:

### 1️⃣ Web Search & Summarization System
	•	Agents Involved:
	•	✅ CorrectorAgent – Cleans and corrects user queries.
	•	✅ WebSearchAgent – Performs Google search to find relevant URLs.
	•	✅ WebScraperAgent – Scrapes content from retrieved pages.
	•	✅ SummarizerAgent – Generates short summaries of extracted text.
	•	✅ FinalReportAgent – Saves the final report as a text file.

📂 Directory: web-search-system/
📜 Status: ✅ Completed

### 2️⃣ AI-Powered Chatbot Agent
	•	Agents Involved:
	•	🤖 IntentClassifierAgent – Identifies user intent (e.g., info, booking, support).
	•	📚 KnowledgeRetrievalAgent – Fetches data from a knowledge base.
	•	💬 ConversationalAgent – Engages in interactive conversations.
	•	📝 TextFormatterAgent – Formats chatbot responses for clarity.

📂 Directory: chatbot-agent/
📜 Status: 🚧 In Progress

### 3️⃣ Financial Market Analysis Agent
	•	Agents Involved:
	•	📈 StockDataScraperAgent – Collects real-time stock data.
	•	🤖 PricePredictionAgent – Uses machine learning to forecast prices.
	•	📰 NewsSentimentAgent – Analyzes financial news sentiment.
	•	📊 ReportGeneratorAgent – Produces daily/weekly market reports.

📂 Directory: financial-analysis-agent/
📜 Status: 🛠 Planned

### 4️⃣ Cybersecurity Threat Intelligence Agent
	•	Agents Involved:
	•	🔍 ThreatScraperAgent – Scrapes threat intelligence sources.
	•	🕵️ MalwareAnalysisAgent – Analyzes malware signatures.
	•	🚨 IncidentAlertAgent – Sends alerts for high-risk threats.
	•	📄 CybersecurityReportAgent – Summarizes threat reports.

📂 Directory: cybersecurity-agent/
📜 Status: 🛠 Planned

### 5️⃣ AI-Powered Multilingual Translator
	•	Agents Involved:
	•	🌍 LanguageDetectionAgent – Detects the source language.
	•	🔄 TranslationAgent – Translates text into the target language.
	•	✍️ GrammarCorrectionAgent – Improves fluency and readability.
	•	📄 DocumentTranslationAgent – Handles full document translations.

📂 Directory: translation-agent/
📜 Status: 🛠 Planned

### 6️⃣ Automated Data Cleaning & Preprocessing Agent
	•	Agents Involved:
	•	🔍 MissingValueHandlerAgent – Fills or removes missing values.
	•	🧼 DuplicateRemoverAgent – Detects and removes duplicates.
	•	📊 DataFormatterAgent – Converts data into a clean format.
	•	📑 FeatureSelectionAgent – Selects the most relevant features.

📂 Directory: data-cleaning-agent/
📜 Status: 🛠 Planned

### 🛠️ Installation & Setup

1️⃣ Clone the Repository

git clone git@github.com:Surneval/LangGraph-Multiagents.git
cd LangGraph-Multiagents

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Set Up API Keys

Some agents use GigaChat for text processing. Create a keys.conf file:

{
  "giga": {
    "key": "YOUR_GIGACHAT_KEY"
  }
}

### 🚀 Running a Multi-Agent System

Each system is run independently.


### 📜 License

This repository is licensed under the MIT License.

🙌 Contributing

Contributions are welcome! If you have an idea for a new multi-agent system, feel free to:
	•	Open an issue
	•	Submit a pull request
	•	Suggest improvements in discussions

### 📞 Contact

📧 Email: nadia.trusova@yahoo.com
💬 Telegram: @surneval
🐙 GitHub: @Surneval

🚀 Enjoy building powerful multi-agent AI systems with LangGraph! 🚀
