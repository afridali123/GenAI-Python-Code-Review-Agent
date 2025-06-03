import os
import time
from openai import AzureOpenAI
from dotenv import load_dotenv
import openai.types  # required for new exception handling

load_dotenv()

# ✅ Use AzureOpenAI client instead of openai.ChatCompletion
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version="2024-02-15-preview",  # Use your Azure API version
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
)

def review_python_code(code: str) -> str:
    max_chars = 6000
    if len(code) > max_chars:
        code = code[:max_chars] + "\n\n# Note: Code truncated due to length."

    for attempt in range(3):
        try:
            response = client.chat.completions.create(
                model="gpt-4o", # 🔁 this must be your deployment name in Azure
                messages=[
                    {"role": "system", "content": "You are a senior Python code reviewer."},
                    {"role": "user", "content": f"Review this code:\n\n{code}"}
                ],
                temperature=0.3
            )
            return response.choices[0].message.content

        except Exception as e:
            if isinstance(e, openai.RateLimitError):
                wait_time = 5 * (attempt + 1)
                print(f"⚠️ Rate limit hit. Retrying in {wait_time}s...")
                time.sleep(wait_time)
            else:
                print(f"❌ Unexpected error: {e}")
                return f"Review failed: {e}"

    return "❌ Failed after 3 attempts."
