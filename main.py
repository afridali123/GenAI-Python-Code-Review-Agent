from azure_repo import clone_or_pull_repo
from reviewer import review_python_code
from utils import get_all_python_files

import os
import json

def get_severity_tag(review: str) -> str:
    review_lower = review.lower()
    if any(word in review_lower for word in ["bug", "error", "exception", "incorrect", "crash"]):
        return "🐞 Issues Found"
    elif any(word in review_lower for word in ["suggest", "improve", "could be better", "recommend"]):
        return "⚠️ Suggestions"
    else:
        return "✅ Clean"

def save_markdown_review(file_path: str, review: str, output_dir: str = "code_reviews_md"):
    os.makedirs(output_dir, exist_ok=True)
    filename = os.path.splitext(os.path.basename(file_path))[0]
    severity = get_severity_tag(review)

    md_path = os.path.join(output_dir, f"{filename}.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(f"# 📄 Code Review: {filename}.py\n")
        f.write(f"**Path**: `{file_path}`\n\n")
        f.write(f"**Severity**: {severity}\n\n")
        f.write("## Review\n")
        f.write(f"```\n{review.strip()}\n```\n")
    print(f"📝 Saved Markdown review → {md_path}")

def save_reviews_json(reviews: dict, output_path: str = "code_review_report.json"):
    json_data = []
    for path, content in reviews.items():
        json_data.append({
            "file": path,
            "severity": get_severity_tag(content),
            "review": content.strip()
        })

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(json_data, f, indent=2)
    print(f"📦 Saved consolidated JSON → {output_path}")

def save_review_report(reviews: dict, output_file: str = "code_review_report.md"):
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# 🧠 AI Code Review Report\n\n")
        for file_path, review in reviews.items():
            filename = os.path.basename(file_path)
            rel_path = os.path.relpath(file_path)
            severity = get_severity_tag(review)
            f.write(f"## 📄 {filename}\n")
            f.write(f"**Path**: `{rel_path}`\n")
            f.write(f"**Severity**: {severity}\n\n")
            f.write("**Review:**\n")
            f.write(f"```\n{review.strip()}\n```\n")
            f.write("\n---\n\n")
    print(f"\n📄 Saved combined report to {output_file}")

def main():
    repo_url = "https://dev.azure.com/westpharmaceutical/SmartDose%20Flex%20Automation/_git/Agent"
    local_path = "C:/Users/thenebandaa/OneDrive - West Pharmaceutical Services, Inc/smartdose automation/git/code"

    clone_or_pull_repo(repo_url, local_path)

    reviews = {}
    py_files = get_all_python_files(local_path)

    for file_path in py_files:
        print(f"\n🔍 Reviewing {file_path}...")
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                code = f.read()
            review = review_python_code(code)
        except Exception as e:
            review = f"❌ Failed to review due to error: {e}"

        reviews[file_path] = review
        save_markdown_review(file_path, review)

    save_review_report(reviews)
    save_reviews_json(reviews)

if __name__ == "__main__":
    main()
