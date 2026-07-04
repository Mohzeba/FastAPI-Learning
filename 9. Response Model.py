from fastapi import FastAPI
from pydantic import BaseModel

# Create a FastAPI application
app = FastAPI()

# Model representing all user data
class User(BaseModel):
    name: str          # User's name
    age: int           # User's age
    password: str      # User's password

# Model representing only the data to be sent in the response
class UserResponse(BaseModel):
    name: str          # User's name
    age: int           # User's age

# GET endpoint: /user
# response_model ensures that only the fields in UserResponse
# are included in the API response
@app.get("/user", response_model=UserResponse)
def get_user():

    # This dictionary contains an extra field: password
    return {
        "name": "Mohzeba",
        "age": 22,
        "password": "123456"
    }