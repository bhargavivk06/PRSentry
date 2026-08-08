## Day 1 - 25 May 2026
- Learned Git, GitHub, JSON
- Created first PR ✅

## Day 2 - 26 May 2026
- Installed FastAPI, Uvicorn
- Built first server
- Got "Bot is alive!" response ✅
- <img width="320" height="77" alt="image" src="https://github.com/user-attachments/assets/5b50d14d-3211-43cd-b8d9-80f875be94f8" />
## Day 3 - 27 May 2026
What I did:

Added webhook route to PRSentry
Understood GET vs POST deeply
Fixed indentation bug myself
Tested webhook using PowerShell
Bot successfully received first fake PR notification ✅

What I learned:

@app.post("/webhook") — creates a route that receives data
async def — means the function waits for data to arrive
await request.json() — reads the JSON data GitHub sends
print(data) — prints it in terminal so we can see it
Indentation in Python is everything — one wrong space breaks everything!

How it feels:

Sent a fake PR notification to my bot
Bot received it and printed it in terminal
That moment = 🤯🔥

## Day 4 - 28 May 2026
What I did:

Installed and configured ngrok
Got public URL for my local server
Connected real GitHub webhook to PRSentry
Opened a real PR and bot received real data ✅
Completed Phase 1! 🎉

What I learned:

ngrok = gives laptop a public address so GitHub can reach it
127.0.0.1 = only visible on my laptop
ngrok URL = visible to entire internet
GitHub webhook settings = where GitHub sends PR notifications
Every time terminals close → bot stops (fixed in Phase 5 with Render)

Big moment:

Saw REAL GitHub PR data printing in my terminal
Bot received action: opened, PR title, changed files, everything!
Phase 1 complete in just 4 days! 🛡️


## Day 5 - 29 May 2026
- Installed PyGithub and python-dotenv
- Created .env file to store token safely
- Created .gitignore to protect secrets
- Bot almost posting comments — 401 auth error
- Tomorrow: fix token and bot posts first comment!

- ## Day 6 - 6 August 2026

**What I did:**
- Generated new GitHub Personal Access Token
- Updated .env file with new token
- Fixed 401 authentication error
- Bot successfully posted first comment on a real PR! ✅

**What I learned:**
- GitHub PAT = bot's password to access GitHub
- .env file = safe place to store secrets
- .gitignore = prevents secrets from going to GitHub
- PyGithub = Python library to talk to GitHub API
- 401 error = authentication failed (token expired/wrong)

**Big moment:**
- Opened a real PR
- Bot automatically commented "PRSentry is watching this PR!"
- Phase 2 Week 5 COMPLETE! 🎉

**Current bot abilities:**
- ✅ Receives GitHub webhooks
- ✅ Authenticates with GitHub
- ✅ Posts comments on PRs automatically!

- ## Day 7 - 8 August 2026

**What I did:**
- Tried Claude API → needs payment ❌
- Switched to Gemini API → hit daily rate limit ❌
- Switched to Groq API → WORKS PERFECTLY! ✅
- Phase 3 Complete! 🎉

**AI APIs I tried:**

Claude API (Anthropic):
- Installed anthropic library
- Got API key from console.anthropic.com
- Error: "Credit balance too low" — needs minimum $5
- Decided to find free alternative

Gemini API (Google):
- Installed google-generativeai library
- Got free API key from aistudio.google.com
- Error: gemini-1.5-flash model not found
- Fixed: switched to gemini-2.0-flash
- Error: Hit daily free tier rate limit
- Decided to find better alternative

Groq API (Final Choice ✅):
- Installed groq library
- Got free API key from groq.com
- Error: llama3-8b-8192 model decommissioned
- Fixed: switched to llama-3.3-70b-versatile
- WORKED PERFECTLY! 🔥

**What I learned:**
- Claude API = best quality but paid
- Gemini API = free but low rate limits
- Groq API = free + fast + high limits = perfect for student projects!
- Rate limiting = APIs have daily/minute request limits
- Model names change over time — always check latest!
- API key = password to access AI services
- Never share API keys publicly!

**Libraries installed today:**
- pip install anthropic ✅
- pip install google-generativeai ✅
- pip install groq ✅

**Big moment:**
Bot posted its first REAL AI code review:
- Overall assessment ✅
- Issues found ✅
- Suggestions for improvement ✅
All automatically on a real GitHub PR! 🤖🎉

**Current bot abilities:**
- ✅ Receives GitHub webhooks
- ✅ Authenticates with GitHub
- ✅ Posts comments on PRs automatically
- ✅ Reads actual code changes
- ✅ AI reviews the code intelligently
- ✅ Posts detailed review as PR comment

**Errors fixed today:**
- Claude API payment error → switched to free Gemini
- Gemini model not found → updated model name
- Gemini rate limit hit → switched to Groq
- Groq model decommissioned → updated to llama-3.3-70b-versatile
- ngrok stopped → restarted it
- uvicorn stopped → restarted it

**Phase 3 COMPLETE! 🎉**




