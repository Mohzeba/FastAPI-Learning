# Third party API Integration by python
#import requests

#response = requests.get("https://jsonplaceholder.typicode.com/posts")
#data = response.json()
#print(data[:2])
# ^ commented-out plain-Python version: calling an external API directly with
# requests, no FastAPI involved — just to show the "before" comparison


# Third party API Integration by FastAPI
from fastapi import FastAPI, HTTPException
import requests
# 'requests' = library to call external APIs (this app is calling
# jsonplaceholder.typicode.com, a fake test API, not your own data)

app = FastAPI()

#Get all data
@app.get("/posts")
def get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    # your FastAPI server itself becomes the client here — it reaches out
    # to a third-party API and fetches data on the caller's behalf
    return response.json()
    # forwards the external API's JSON straight back to whoever called YOUR endpoint

#get single post
@app.get("/posts/{post_id}")
def get_post(post_id: int):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    # post_id path parameter gets inserted into the external API's URL
    response = requests.get(url)
    if response.status_code == 404:
        raise HTTPException(status_code=404, detail="Post not found")
        # if the THIRD-PARTY api says "not found", you translate that into
        # your OWN API's proper error response instead of just passing along
        # whatever raw response the third party sent
    return response.json()