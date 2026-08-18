from model_router import ask_model

prompt = "Explain artificial intelligence in two sentences."

print("FAST MODEL:")
print(ask_model(prompt, "fast"))

print("\nPOWERFUL MODEL:")
print(ask_model(prompt, "powerful"))