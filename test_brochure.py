from gradio_practice import create_brochure


for result in create_brochure(
    "Example",
    "https://example.com"
):
    print(result)