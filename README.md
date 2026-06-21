

---

```markdown
# 📌 GitHub MCP Server (AI-Powered GitHub Automation)

## 🚀 Overview

This project is an MCP (Model Context Protocol) Server that connects **Claude AI** with **GitHub APIs**, enabling real-time interaction with GitHub repositories.

It acts as a **bridge between AI and GitHub**, allowing AI agents to perform GitHub operations like issues and pull request management.

---

## 🧠 Features

### 📥 GitHub Data Access
- Fetch all issues from repository  
- Read PR comments  

### ✍️ GitHub Actions
- Create new issues  
- Post comments on pull requests  

### 🤖 AI Integration Ready
- Works with Claude Desktop via MCP  
- Enables tool-based AI agent execution  
- Foundation for autonomous GitHub agents  

---

## 🏗️ Project Structure

```

github-mcp/
│
├── server.py          # MCP server with GitHub tools
├── .env               # Environment variables (NOT pushed to GitHub)
├── requirements.txt   # Python dependencies (optional)
└── README.md

````

---

## ⚙️ Tech Stack

- Python 3.10+
- MCP (Model Context Protocol SDK)
- GitHub REST API
- Requests library
- python-dotenv

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/jayasri21072006/github-mcp.git
cd github-mcp
````

---

### 2. Install dependencies

```bash
pip install requests python-dotenv mcp
```

---

### 3. Setup environment variables

Create a `.env` file:

```env
GITHUB_TOKEN=your_github_token
OWNER=your_github_username
REPO=your_repo_name
```

---

## 🚀 Running the MCP Server

```bash
python server.py
```

Expected output:

```
GitHub MCP Server Started Successfully
Waiting for MCP client connection...
```

---

## 🧩 Available MCP Tools

### 1. List Issues

Fetch all issues from the repository.

### 2. Create Issue

Create a new GitHub issue using AI.

### 3. List PR Comments

Fetch all comments from a pull request.

### 4. Create PR Comment

Post a comment on a pull request.

---

## 🔄 Workflow

```
Claude AI
   ↓
MCP Server (server.py)
   ↓
GitHub API
   ↓
Issues / Pull Requests / Comments
```

---

## 🎯 Use Case

This project enables:

* AI-powered GitHub automation
* Smart issue tracking system
* PR review assistance
* Foundation for AI coding agents

---

## 📌 Future Improvements

* Auto bug fixing agent
* AI PR reviewer
* Test case generation agent
* Fully autonomous developer assistant

---

## 👨‍💻 Author

**Jayasri T**

Internship Project – AI + Data Science

---

## ⭐ Status

* ✔ MCP Server Working
* ✔ GitHub API Integrated
* ✔ Claude AI Compatible
* ✔ Ready for AI Agent Expansion

```


