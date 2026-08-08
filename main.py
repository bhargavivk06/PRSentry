# PRSentry - AI Code Review Bot
from fastapi import FastAPI, Request
from github import Github
from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()

token = os.getenv("GITHUB_TOKEN")
groq_key = os.getenv("GROQ_API_KEY")

g = Github(token)
groq_client = Groq(api_key=groq_key)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Bot is alive!"}

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    
    if data.get("action") == "opened":
        repo_name = data["repository"]["full_name"]
        pr_number = data["pull_request"]["number"]
        pr_title = data["pull_request"]["title"]
        additions = data["pull_request"]["additions"]
        deletions = data["pull_request"]["deletions"]
        changed_files = data["pull_request"]["changed_files"]

        repo = g.get_repo(repo_name)
        pr = repo.get_pull(pr_number)

        files = pr.get_files()
        code_diff = ""
        for file in files:
            code_diff += f"\nFile: {file.filename}\n"
            if file.patch:
                code_diff += file.patch

        response = groq_client.chat.completions.create(
           model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": f"""You are PRSentry, an AI code reviewer.
Review this Pull Request and give helpful feedback.

PR Title: {pr_title}
Files Changed: {changed_files}
Additions: {additions}
Deletions: {deletions}

Code Changes:
{code_diff}

Give a concise review with:
1. Overall assessment
2. Issues found (if any)
3. Suggestions for improvement
Keep it short and helpful!"""
                }
            ]
        )

        ai_review = response.choices[0].message.content

        comment = f"""🛡️ PRSentry AI Review

📋 PR Title: {pr_title}
📁 Files Changed: {changed_files}
➕ Additions: {additions}
➖ Deletions: {deletions}

🤖 AI Review:
{ai_review}"""

        pr.create_issue_comment(comment)

    return {"status": "received"}