# PRSentry - AI Code Review Bot
from fastapi import FastAPI, Request

app=FastAPI()

@app.get("/")
def home():
    return {"message":"Bot is alive!"}

@app.post("/webhook")
async def webhook(request: Request):
    data=await request.json()
    print(data)
    return {"status": "recieved"}