# Web Research Assistant

A simple AI-powered web research tool built during Week 2 of my LLM Engineering course.

## What it does

The user provides a webpage URL. The application:

1. Fetches the webpage
2. Extracts and cleans the text using BeautifulSoup
3. Sends the text to a Groq-hosted LLM
4. Generates a concise summary and important points
5. Displays the analysis through a Streamlit interface

## Technologies

- Python
- Groq API
- GPT-OSS 120B
- Requests
- BeautifulSoup
- Streamlit

## Project Structure

```text
web_research_assistant/
├── app.py
├── researcher.py
├── scraper.py
├── requirements.txt
└── README.md