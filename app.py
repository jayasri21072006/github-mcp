import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("GITHUB_TOKEN")
OWNER = os.getenv("OWNER")
REPO = os.getenv("REPO")

PR_NUMBER = 4  # Your PR number

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json"
}

url = f"https://api.github.com/repos/{OWNER}/{REPO}/issues/{PR_NUMBER}/comments"

data = {
    "body": "This comment was automatically created using the GitHub API."
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 201:
    print("Comment added successfully!")
    print("Comment URL:", response.json()["html_url"])
else:
    print("Error:", response.status_code)
    print(response.text)