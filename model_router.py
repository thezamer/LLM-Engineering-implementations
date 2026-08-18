import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODELS = {
    "fast": "openai/gpt-oss-20b",
    "powerful": "openai/gpt-oss-120b"
}


def ask_model(prompt, model_name="powerful"):
    model = MODELS[model_name]

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content