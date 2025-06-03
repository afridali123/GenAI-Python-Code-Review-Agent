import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

# Azure OpenAI client setup
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version="2024-02-15-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT")

REVIEW_FOLDER = "C:/Users/thenebandaa/OneDrive - West Pharmaceutical Services, Inc/smartdose automation/git/code_reviews_md"
SOURCE_FOLDER = "C:/Users/thenebandaa/OneDrive - West Pharmaceutical Services, Inc/smartdose automation/git/code/src"
OUTPUT_FOLDER = "fixed_code"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def apply_review_fix(original_code: str, review_text: str) -> str:
    prompt = f"""
You are an expert Python developer. Based on the following code review comments, rewrite the code to fix all issues:

--- REVIEW COMMENTS ---
{review_text}

--- ORIGINAL CODE ---
{original_code}

Please return the entire updated Python code.
"""
    response = client.chat.completions.create(
        model=deployment_name,
        messages=[
            {"role": "system", "content": "You are a senior Python engineer who improves code based on reviews."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )
    return response.choices[0].message.content.strip()

def process_all_files():
    for md_file in os.listdir(REVIEW_FOLDER):
        if md_file.endswith(".md"):
            filename = md_file.replace(".md", ".py")
            md_path = os.path.join(REVIEW_FOLDER, md_file)
            py_path = None

            # Recursively find the original .py file
            for root, _, files in os.walk(SOURCE_FOLDER):
                if filename in files:
                    py_path = os.path.join(root, filename)
                    break

            if not py_path or not os.path.exists(py_path):
                print(f"❌ Source file not found for: {filename}")
                continue

            print(f"🔧 Fixing: {filename}")

            with open(py_path, "r", encoding="utf-8") as f:
                original_code = f.read()

            with open(md_path, "r", encoding="utf-8") as f:
                review_comments = f.read()

            try:
                fixed_code = apply_review_fix(original_code, review_comments)
                output_path = os.path.join(OUTPUT_FOLDER, filename)
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(fixed_code)
                print(f"✅ Fixed and saved: {output_path}")
            except Exception as e:
                print(f"❌ Failed to process {filename}: {e}")

if __name__ == "__main__":
    process_all_files()
