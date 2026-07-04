from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Temporary in-memory list acting as a fake database
users = []

# Schema defining what a User looks like
class User(BaseModel):
    name: str
    age: int

# POST endpoint: Add a new user to the list
@app.post("/users")
def create_user(user: User):
    users.append(user)
    return {
        "message": "User Created",
        "data": user
    }

# PUT endpoint: Update an existing user by their index in the list
# notify is an optional query parameter (default False)
@app.put("/users/{user_id}")
def update_user(user_id: int, user: User, notify: bool = False):
    
    # Check if user_id is a valid index
    if user_id < len(users):
        users[user_id] = user
        return {
            "message": "User Updated",
            "notify": notify,  # returns whether notification was requested
            "data": user
        }
    return {"error":"User not found"}