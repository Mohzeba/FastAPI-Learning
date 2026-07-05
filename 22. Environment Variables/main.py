from dotenv import load_dotenv
from config import setting
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
#import os
#import dotenv import load_dotenv    
# need: from config import setting   ← this file uses 'setting' but never imports it
# need: from dotenv import load_dotenv  ← same issue, used but not imported

app = FastAPI()

load_dotenv()  
# loads values from your .env file into the environment (used inside config.py)

origins = setting.ORIGINS  
# pulls the allowed frontend URL(s) from your Settings class in config.py

#origins = [os.getenv("ORIGINS")]  
# unused alternate way to get origins directly, ignore
#DB_URL = os.getenv("DB_URL")  
# unused for now, ignore

app.add_middleware(
    CORSMiddleware,
    # lets a frontend on a different port/domain actually call this API
    allow_origins = origins,  
    # only these URLs are allowed to call this backend
    allow_credentials = True,  
    # allows cookies/auth tokens to be sent cross-origin
    allow_methods = ["*"], #GET,PUT,POST,DELETE
    # "*" = allow every HTTP method
    allow_headers=["*"]
    # "*" = allow every request header
)

@app.get("/")
def home():
    return{
        "message":"CORS ENABLE API"
    }
# test route to confirm CORS works from your frontend