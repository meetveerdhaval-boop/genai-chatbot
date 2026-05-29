import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
print("API KEY:", os.getenv("OPENAI_API_KEY"))
if not api_key:
    raise ValueError("API key not found. Check your .env file")

client = OpenAI(api_key=api_key)

def get_response(messages, model="gpt-4o-mini"):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"
    