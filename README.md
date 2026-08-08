# PRSentry 🛡️
> AI-powered GitHub Pull Request Review Bot

PRSentry automatically reviews your Pull Requests using AI and posts intelligent feedback instantly!

## ✨ Features
- 🤖 AI powered code review using Llama 3.3
- 🔍 Detects programming language automatically
- ⚠️ Finds common issues (hardcoded passwords, print statements, TODOs)
- 📊 PR complexity scoring
- ⚡ Instant feedback when PR is opened

## 🚀 How to Use
1. Go to your GitHub repo settings
2. Click Webhooks → Add webhook
3. Set Payload URL to: `https://prsentry-2m0a.onrender.com/webhook`
4. Set Content type to: `application/json`
5. Select Pull requests events
6. Click Add webhook
7. Open a PR and watch PRSentry review it! 🎉

## 🛠️ Built With
- Python
- FastAPI
- GitHub Webhooks
- Groq AI (Llama 3.3)
- Render (deployment)

## 📊 Example Review
🛡️ PRSentry AI Review
📋 PR Title: Add login feature
📁 Files Changed: 3
➕ Additions: 45
➖ Deletions: 2
🔤 Languages: Python
📊 Complexity: 🟡 Medium — Review carefully!
⚠️ Issues Found:
⚠️ print() statements found — remove before production!
🤖 AI Review: Overall the code structure is good...

## 👩‍💻 Author
Built by Bhargavi — 2nd year CS Engineering student
