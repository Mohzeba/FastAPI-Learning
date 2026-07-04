from fastapi import FastAPI
from pydantic import BaseModel

# Create a FastAPI application
app = FastAPI()

# Define the structure (schema) of the user data
class User(BaseModel):
    name: str    # User's name (string)
    age: int     # User's age (integer)
    email: str   # User's email (string)

# POST endpoint: /create_user
@app.post("/create_user")
def create_user(user: User):
    # FastAPI receives the JSON request body
    # Validates it using the User model
    # Converts the JSON into a User object

    # Return a success message and the received user data
    return {
        "message": "User Created",
        "data": user
    }