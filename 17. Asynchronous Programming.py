import time
import asyncio
from fastapi import FastAPI

app = FastAPI()

# async def = this route can pause and let other requests run while waiting
@app.get("/")
async def home():
    await asyncio.sleep(3)  # pause for 3 seconds WITHOUT blocking the server
    return{
        "message":"Async API"
    }
    
# SYNC version - blocks everything for 3 seconds, no other requests handled
#def task():
#   time.sleep(3)
#   return "Done"

# ASYNC version - pauses for 3 seconds but server stays free for other requests
#async def task():
#   await asyncio.sleep(3)
#   return "Done"