# 🌍 Global Signal Detector v1

> An AI-powered Streamlit application that analyzes news/articles using a local LLM (Gemma via Ollama) and converts unstructured text into structured intelligence signals.


##  Overview

Global Signal Detector v1 is a local AI system designed to analyze textual information such as news articles, reports, or observations and transform them into structured intelligence insights.
It simulates an early-stage “AI intelligence analyst system” that extracts meaningful signals from raw data.


##  Problem Statement

In the modern digital world, information overload is a major challenge.
Every day:
- Thousands of news articles are published
- Important signals get buried
- Manual analysis is slow and inconsistent

### This system solves:

 Converting raw information → structured intelligence signals  
 Helping users quickly understand impact, risk, and relevance 


##  Features

### 📌 AI-Powered Analysis
Uses a local LLM (Gemma via Ollama) to analyze input text and generate structured intelligence reports.

### 📌 Structured Output Format
Each analysis includes:

- Summary
- Category (Technology, Health, Economy, etc.)
- Impact Scope (Local / National / Global)
- Severity Score (1–10)
- Stakeholders Affected
- Key Insight
- Risks
- Recommended Actions

### 📌 Interactive UI (Streamlit)
- Clean dashboard interface
- Sidebar system status panel
- Analysis input box
- Expandable result view

### 📌 Session Memory System
- Stores recent articles
- Stores last 10 full analyses
- Allows quick recall of previous investigations

### 📌 New Analysis Workflow
- Clears previous input
- Resets UI state
- Starts fresh investigation


## ⚙️ Tech Stack

- Python 
- Streamlit 
- Ollama (Gemma local LLM) 
- datetime module
- Session State Management (Streamlit)


## 🧩 System Architecture

```text
User Input (Article/Text)
        ↓
Streamlit UI Layer
        ↓
Prompt Engineering Layer
        ↓
Ollama (Gemma LLM)
        ↓
Structured Intelligence Output
        ↓
Session Storage (History + Recent Articles)
        ↓
UI Display
```

🛠️ Installation & Setup
## 🛠️ Installation & Setup

### Prerequisites

Make sure you have the following installed:

- Python 3.10+
- Ollama
- Git

---

### 1. Clone the Repository

git clone https://github.com/ishasherj1730-spec/global-signal-detector-v1.git
cd global-signal-detector-v1

2. Install Dependencies
pip install -r requirements.txt

3. Install and Run Ollama

Download Ollama from:

https://ollama.com

Pull the required model:

ollama pull gemma4:e4b

Start the model:

ollama run gemma4:e4b


4. Launch the Application
streamlit run sourcecode.py

5. Open in Browser
Streamlit will automatically open:

http://localhost:8501

You can now paste any article, report, observation, or trend and receive an AI-generated intelligence analysis.

## Current Limitations

- Uses local LLM inference through Ollama (Gemma).
- Analysis speed depends on hardware specifications.
- On CPU-only systems, analysis may take 1–3 minutes for detailed reports.
- Currently requires manual article input.
- Real-time data ingestion is planned for Version 2.


## Vision

Global Signal Detector is the first step toward building larger AI-driven intelligence systems capable of identifying meaningful signals from large-scale information streams.

Version 1 focuses on manual analysis.

Future versions will introduce:
- Automated news collection
- Signal ranking
- Trend detection
- Multi-source intelligence analysis


## 👤 Author

**Isha Sherj**

Computer Applications Student | Aspiring AI Engineer 

Focused on:
- Artificial Intelligence
- Data Science
- Agentic Systems
- Intelligent Product Development

GitHub: https://github.com/ishasherj1730-spec
