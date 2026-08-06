# PRSentry - AI Code Review Bot
#testing bot comment
# Phase 2 test
#week 6 test 2
from fastapi import FastAPI, Request
from github import Github
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("GITHUB_TOKEN")
g=Github(token)

app=FastAPI()

@app.get("/")
def home():
    return {"message":"Bot is alive!"}

@app.post("/webhook")
async def webhook(request: Request):
    data=await request.json()
   
    if data.get("action") == "opened":
        repo_name=data["repository"]["full_name"]
        pr_number=data["pull_request"]["number"]
        pr_title=data["pull_request"]["title"]
        additions=data["pull_request"]["additions"]
        deletions=data["pull_request"]["deletions"]
        changed_files=data["pull_request"]["changed_files"]

        repo=g.get_repo(repo_name)
        pr=repo.get_pull(pr_number)

        comment = f"""🛡️ PRSentry Review

📋 PR Title: {pr_title}
📁 Files Changed: {changed_files}
➕ Additions: {additions}
➖ Deletions: {deletions}

PRSentry is analyzing your code... AI review coming soon!"""
        pr.create_issue_comment(comment)
    return {"status": "recieved"}
