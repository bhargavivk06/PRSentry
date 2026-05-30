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




