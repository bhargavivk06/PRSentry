# PRSentry - AI Code Review Bot
#changes
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
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

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

def detect_language(files):
    extensions = {
        '.py': 'Python',
        '.js': 'JavaScript',
        '.java': 'Java',
        '.cpp': 'C++',
        '.c': 'C',
        '.ts': 'TypeScript',
        '.html': 'HTML',
        '.css': 'CSS'
    }
    languages = set()
    for file in files:
        ext = os.path.splitext(file.filename)[1]
        if ext in extensions:
            languages.add(extensions[ext])
    return list(languages) if languages else ['Unknown']

def check_issues(code_diff):
    issues = []
    if "password" in code_diff.lower() and "=" in code_diff:
        issues.append("⚠️ Possible hardcoded password detected!")
    if "print(" in code_diff:
        issues.append("⚠️ print() statements found — remove before production!")
    if "TODO" in code_diff:
        issues.append("⚠️ TODO comments found — make sure to address them!")
    if "except:" in code_diff:
        issues.append("⚠️ Bare except clause found — catch specific exceptions!")
    return issues

def get_complexity(additions, deletions, changed_files):
    total_changes = additions + deletions
    if total_changes < 50 and changed_files <= 3:
        return "🟢 Low — Easy to review!"
    elif total_changes < 200 and changed_files <= 8:
        return "🟡 Medium — Review carefully!"
    else:
        return "🔴 High — Consider splitting this PR!"

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
        languages = detect_language(files)
        code_diff = ""
        for file in files:
            code_diff += f"\nFile: {file.filename}\n"
            if file.patch:
                code_diff += file.patch

        issues = check_issues(code_diff)
        complexity = get_complexity(additions, deletions, changed_files)

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
🔤 Languages: {', '.join(languages)}
📊 Complexity: {complexity}

⚠️ Issues Found:
{chr(10).join(issues) if issues else '✅ No issues found!'}

🤖 AI Review:
{ai_review}"""

        pr.create_issue_comment(comment)

    return {"status": "received"}