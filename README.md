# 🧠 GenAI Python Code Review Agent

A GenAI-powered assistant that reviews and analyzes Python code stored in Azure DevOps Repos using OpenAI's ChatGPT API (GPT-4). It automates code quality checks, highlights bugs, suggests improvements, and provides summaries for Python files written by your team.

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

