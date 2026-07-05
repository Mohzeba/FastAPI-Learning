# Third party API Integration by python
#import requests

#response = requests.get("https://jsonplaceholder.typicode.com/posts")

#data = response.json()
#print(data[:2])


# Third party API Integration by FastAPI
from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

#Get all data
@app.get("/posts")
def get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    return response.json()

#get single post
@app.get("/posts/{post_id}")
def get_post(post_id: int):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = requests.get(url)
    if response.status_code == 404:
        raise HTTPException(status_code=404, detail="Post not found")
    return response.json()