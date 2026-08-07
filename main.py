# PRSentry - AI Code Review Bot
#testing bot comment
# Phase 2 test
#week 6 test 2
#ai tst
from fastapi import FastAPI, Request
from github import Github
from dotenv import load_dotenv
import os
import anthropic

load_dotenv()

token = os.getenv("GITHUB_TOKEN")
claude_key=os.getenv("ANTHROPIC_API_KEY")
g=Github(token)
claude=anthropic.Anthropic(api_key=claude_key)

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
        diff_url=data["pull_request"]["diff_url"]

        repo=g.get_repo(repo_name)
        pr=repo.get_pull(pr_number)

        files=pr.get_files()
        code_diff=""
        for file in files:
            code_diff+=f"\nFile: {file.filename}\n"
            if file.patch:
                code_diff+=file.patch

        message=claude.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1000,
            messages=[
                {
                    "role":"user",
                    "content":f"""You are PRSentry,an AI code reviewer.
Review this pull Request and give helpful feedback.

PR Title:{pr_title}
Files Changed:{changed_files}
Additions:{additions}
Deletions:{deletions}

Code Changes:
{code_diff}

Give a concise  review with:
1.overall assessment
2.issues found(if any)
3.suggestions for improvement
keep it short and helpful!"""
                }
            ]
        )

        ai_review=message.content[0].text

        comment = f"""🛡️ PRSentry Review

📋 PR Title: {pr_title}
📁 Files Changed: {changed_files}
➕ Additions: {additions}
➖ Deletions: {deletions}

🤖 AI Review:
{ai_review}"""
        pr.create_issue_comment(comment)
    return {"status": "recieved"}
