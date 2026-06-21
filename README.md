# 🌍 Global Signal Detector v1

> An AI-powered Streamlit application that analyzes news/articles using a local LLM (Gemma via Ollama) and converts unstructured text into structured intelligence signals.

---

## 🧠 Overview

Global Signal Detector v1 is a local AI system designed to analyze textual information such as news articles, reports, or observations and transform them into structured intelligence insights.

It simulates an early-stage “AI intelligence analyst system” that extracts meaningful signals from raw data.

---

## ⚙️ Tech Stack

- Python 🐍
- Streamlit 🎨
- Ollama (Gemma local LLM) 🧠
- datetime module
- Session State Management (Streamlit)

---

## 🚀 Features

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

---

### 📌 Interactive UI (Streamlit)
- Clean dashboard interface
- Sidebar system status panel
- Analysis input box
- Expandable result view

---

### 📌 Session Memory System
- Stores recent articles
- Stores last 5 full analyses
- Allows quick recall of previous investigations

---

### 📌 New Analysis Workflow
- Clears previous input
- Resets UI state
- Starts fresh investigation

---

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
