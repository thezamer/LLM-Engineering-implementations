import streamlit as st

from scraper import scrape_webpage
from researcher import ask_llm


st.title("Web Research Assistant")

st.write("Enter a webpage URL and let AI analyze it.")

url = st.text_input(
    "Enter a webpage URL",
    placeholder="https://example.com/article"
)

if st.button("Analyze"):

    if not url:
        st.warning("Please enter a webpage URL.")

    else:
        with st.spinner("Researching webpage..."):

            try:
                text = scrape_webpage(url)

                result = ask_llm(
                    f"""
Analyze the following webpage text.

Give me:
1. A concise summary
2. The most important points

Webpage text:
{text}
"""
                )

                st.subheader("Analysis")
                st.write(result)

            except Exception as e:
                st.error(f"Something went wrong: {e}")