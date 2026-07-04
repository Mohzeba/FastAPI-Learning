from fastapi import FastAPI
from pydantic import BaseModel

# Create a FastAPI application
app = FastAPI()

# Define the structure (schema) of the user data
class User(BaseModel):
    name: str   # User's name (string)
    age: int    # User's age (integer)

# POST endpoint: /create-user
@app.post("/create-user")
def create_user(user: User):
    # FastAPI automatically validates the incoming JSON
    # and converts it into a User object

    # Return a success message along with the received data
    return {
        "message": "User Created",
        "data": user
    }