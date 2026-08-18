import os
from dotenv import load_dotenv
from litellm import completion

load_dotenv()

response = completion(
    model="groq/openai/gpt-oss-120b",
    messages=[
        {
            "role": "user",
            "content": "Explain what an LLM is in simple English."
        }
    ],
    api_key=os.getenv("GROQ_API_KEY")
)

print(response.choices[0].message.content)