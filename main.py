from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "home"}

@app.get("/about")
def about():
    return {"message": "about"}

@app.get("/users")
def users():
    return {
        "users": ["hope", "success", "peace"]
    }

