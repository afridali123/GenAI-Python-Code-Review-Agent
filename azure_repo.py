from git import Repo, InvalidGitRepositoryError
import os
from dotenv import load_dotenv
import shutil

load_dotenv()

azure_pat = os.getenv("AZURE_DEVOPS_PAT")

def clone_or_pull_repo(repo_url, local_path):
    # Properly inject PAT into the repo URL
    # Input repo_url: "https://dev.azure.com/org/project/_git/repo"
    repo_url = repo_url.replace("https://", f"https://{azure_pat}@")

    if os.path.exists(local_path):
        try:
            repo = Repo(local_path)
            print("✅ Repo exists, pulling latest...")
            repo.remote().pull()
            return
        except InvalidGitRepositoryError:
            print("❌ Not a valid Git repo, removing and recloning...")
            shutil.rmtree(local_path)

    print("⬇️ Cloning fresh repo...")
    Repo.clone_from(repo_url, local_path)
