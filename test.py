import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.api_key = os.getenv("GEMINI_API_KEY")

model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-002")

response = model.generate_content("What is AI?")

print(response.text)


#uvicorn main:app --reload