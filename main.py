# PRSentry - AI Code Review Bot
#testing bot comment
# Phase 2 test
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

        repo=g.get_repo(repo_name)
        pr=repo.get_pull(pr_number)
        pr.create_issue_comment("PRSentry is watching this PR!")
    return {"status": "recieved"}
