from fastapi import FastAPI

app = FastAPI()

#Home Route
@app.get("/")
def home():
    return {"message": "Welcome Home"}

@app.get("/about")
def about():
    return{"message": "About"}

@app.get ("/users")
def users():
    return {
        "users": ["Jhon", "Sam", "Summer"]
    }