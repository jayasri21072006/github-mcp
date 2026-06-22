import os
import requests
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

load_dotenv()

mcp = FastMCP("github-mcp")

TOKEN = os.getenv("GITHUB_TOKEN")
OWNER = os.getenv("OWNER")
REPO = os.getenv("REPO")

if not TOKEN or not OWNER or not REPO:
    raise ValueError("Missing GITHUB_TOKEN, OWNER, or REPO in .env")

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json"
}

@mcp.tool()
def list_issues():
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/issues"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return {"error": response.text}

    issues = response.json()

    result = []
    for issue in issues:
        if "pull_request" in issue:
            continue

        result.append({
            "number": issue["number"],
            "title": issue["title"],
            "state": issue["state"]
        })

    return result


@mcp.tool()
def create_issue(title: str, body: str):
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/issues"

    response = requests.post(
        url,
        headers=headers,
        json={
            "title": title,
            "body": body
        }
    )

    if response.status_code not in [200, 201]:
        return {"error": response.text}

    data = response.json()

    return {
        "number": data.get("number"),
        "title": data.get("title"),
        "url": data.get("html_url")
    }


@mcp.tool()
def list_pr_comments(pr_number: int):
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/issues/{pr_number}/comments"

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return {"error": response.text}

    comments = response.json()

    return [
        {
            "user": c["user"]["login"],
            "body": c["body"]
        }
        for c in comments
    ]


@mcp.tool()
def create_pr_comment(pr_number: int, comment: str):
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/issues/{pr_number}/comments"

    response = requests.post(
        url,
        headers=headers,
        json={"body": comment}
    )

    if response.status_code not in [200, 201]:
        return {"error": response.text}

    data = response.json()

    return {
        "id": data.get("id"),
        "url": data.get("html_url"),
        "body": data.get("body")
    }


if __name__ == "__main__":
    print("[INFO] GitHub MCP Server Started Successfully")
    print("[INFO] Waiting for MCP client connection...")
    mcp.run()