import gradio as gr
from scraper import scrape_webpage
from researcher import ask_llm_stream


def create_brochure(company_name, url):
    text = scrape_webpage(url)

    prompt = f"""
You are a professional company research assistant.

Create a concise and professional company brochure for {company_name}.

Use the following webpage content as your source:

{text}

Include:
- Company overview
- What the company does
- Main products or services
- Key information that would be useful to a potential customer

Keep it clear, professional, and easy to read.
"""

    response = ""

    for chunk in ask_llm_stream(prompt):
        response += chunk
        yield response
demo = gr.Interface(
    fn=create_brochure,
    inputs=[
        gr.Textbox(label="Company Name"),
        gr.Textbox(label="Website URL")
    ],
    outputs=gr.Markdown(),
    title="Company Brochure Generator",
    description="Enter a company name and website to generate an AI-powered brochure."
)

demo.launch()