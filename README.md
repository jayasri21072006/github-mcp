📌 GitHub MCP Server (AI-Powered GitHub Automation)
🚀 Overview

This project is an MCP (Model Context Protocol) Server that connects Claude AI with GitHub APIs, enabling AI to interact with GitHub repositories in real time.

It allows AI agents to:

Fetch GitHub issues
Create new issues
Read PR comments
Post comments on pull requests

This acts as a bridge between AI and GitHub, enabling automation and agent-based workflows.

🧠 Features
📥 GitHub Data Access
List all issues in a repository
Fetch PR comments
✍️ GitHub Actions
Create new issues
Post comments on pull requests
🤖 AI Integration Ready
Works with Claude Desktop via MCP
Enables tool-based AI agent execution
🏗️ Project Structure
github-mcp/
│
├── server.py          # MCP server with GitHub tools
├── .env               # Environment variables (NOT pushed to GitHub)
├── requirements.txt   # Python dependencies (optional)
└── README.md
⚙️ Tech Stack
Python 3.10+
MCP (Model Context Protocol SDK)
GitHub REST API
Requests library
Python-dotenv
📦 Installation
1. Clone the repository
git clone https://github.com/jayasri21072006/github-mcp.git
cd github-mcp
2. Install dependencies
pip install requests python-dotenv mcp
3. Setup environment variables

Create a .env file:

GITHUB_TOKEN=your_github_token
OWNER=your_github_username
REPO=your_repo_name
🚀 Running the MCP Server
python server.py

You should see:

GitHub MCP Server Started Successfully
Waiting for MCP client connection...
🧩 Available MCP Tools
1. List Issues

Fetch all issues from repository

2. Create Issue

Create a new GitHub issue using AI

3. List PR Comments

Fetch comments from a pull request

4. Create PR Comment

Post a comment on a pull request

🔄 Workflow
Claude AI
   ↓
MCP Server (server.py)
   ↓
GitHub API
   ↓
Issues / PR / Comments
🎯 Use Case

This project enables:

AI-powered GitHub automation
Smart issue tracking
PR review assistance
Foundation for AI coding agents
📌 Future Improvements
Auto bug fixing agent
PR code reviewer AI
Test case generation agent
Fully autonomous dev assistant
👨‍💻 Author

Jayasri T


⭐ Status

✔ MCP Server Working
✔ GitHub API Integrated
✔ Claude AI Compatible
✔ Ready for Extension into AI Agent Systems
