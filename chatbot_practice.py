import gradio as gr
from researcher import chat_with_history_stream


def chat(message, history):
    response = ""

    for chunk in chat_with_history_stream(message, history):
        response += chunk
        yield response

demo = gr.ChatInterface(
    fn=chat,
    title="AI Chatbot",
    description="A conversational AI with memory and streaming."
)

demo.launch()