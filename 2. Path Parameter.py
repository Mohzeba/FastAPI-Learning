from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id:int):
    return {"user_id": user_id}

@app.get("/users/{user_name}")
def get_user(user_name:str):
    return {"user_name": user_name}
