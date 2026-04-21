# 🧠 GenAI Python Code Review Agent

A GenAI-powered assistant that reviews and analyzes Python code stored in Azure DevOps Repos using OpenAI's ChatGPT API (GPT-4). It automates code quality checks, highlights bugs, suggests improvements, and provides summaries for Python files written by your team.

GenAI-powered Python Code Review Agent that analyzes repositories, detects issues, and generates structured review reports using LLMs (GPT/Claude).

---

## 📌 Features

- Connects to Azure DevOps Repos using Personal Access Token (PAT)
- Automatically retrieves all `.py` files in the repository
- Sends code to OpenAI GPT-4 for review and analysis
- Returns:
  - Code summary
  - Bug detection
  - Suggestions for improvements
  - Best practice adherence
- Command-line based execution
- Modular and extensible

---

## 🔧 Prerequisites

- Python 3.8+
- OpenAI API key with GPT-4 access
- Azure DevOps account with access to your repo
- Azure DevOps Personal Access Token (PAT)

---

## 📁 Project Structure
genai-code-review-agent/
│
├── main.py # Entry point: fetch code and get reviews
├── azure_fetch.py # Functions to connect to Azure DevOps and fetch code
├── code_reviewer.py # Code review logic using OpenAI GPT-4
├── .env # Environment variables (not checked into GitHub)
├── .gitignore # Ignore environment and secret files
├── requirements.txt # Dependencies
└── README.md # You're here!


## ⚙️ Setup

1. **Clone the Repository**

```bash
git clone https://github.com/your-username/genai-code-review-agent.git
cd genai-code-review-agent

## Install Dependencies
pip install -r requirements.txt

## Create a .env file with the following:
OPENAI_API_KEY=your-openai-api-key
AZURE_PAT=your-azure-devops-pat
AZURE_ORG=your-org-name
AZURE_PROJECT=your-project-name
AZURE_REPO=your-repo-name

## Run the Agent

python main.py

## Output Example 
Reviewing /src/utils/helper.py...

--- Review for /src/utils/helper.py ---

1. Summary:
   This file defines utility functions for handling file operations and data formatting.

2. Issues:
   - Uses a hardcoded path which should be parameterized.
   - Lacks exception handling for file operations.

3. Suggestions:
   - Add docstrings for functions.
   - Use pathlib for file paths.

4. Best Practices:
   - Functions are small and focused.
   - Uses list comprehensions effectively.

## 🧩 Extending the Agent
✅ Add Git PR integration (comment reviews automatically)

✅ Store reviews in Markdown or PDF

✅ Add a simple Streamlit or Flask UI

✅ Review only files changed in a given commit


