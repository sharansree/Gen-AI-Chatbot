import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

models = genai.list_models()
print("Available models:")
print("GEMINI_API_KEY =", os.getenv("GEMINI_API_KEY"))

for m in models:
    print(f"- {m.name} : supported methods {m.supported_generation_methods}")
