import os

from dotenv import load_dotenv
from huggingface_hub import InferenceClient


load_dotenv()


client = InferenceClient(
    api_key=os.getenv("HF_TOKEN")
)


def generate_image(prompt):
    image = client.text_to_image(
        prompt=prompt,
        model="black-forest-labs/FLUX.1-dev"
    )

    image.save("generated_image.png")

    print("Image generated successfully!")
    print("Saved as generated_image.png")


if __name__ == "__main__":
    prompt = input("Describe the image you want: ")

    generate_image(prompt)