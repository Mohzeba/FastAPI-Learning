from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

# Create a FastAPI application
app = FastAPI()

# Create a custom exception class
class UserNotFoundException(Exception):

    # Store the user's name when the exception is raised
    def __init__(self, name: str):
        self.name = name

# Register a custom exception handler
# This function runs whenever UserNotFoundException is raised
@app.exception_handler(UserNotFoundException)
def user_not_found_handler(request: Request, exc: UserNotFoundException):

    # Return a custom JSON response with status code 404
    return JSONResponse(
        status_code=404,
        content={
            "status": "error",
            "message": f"User {exc.name} not found"
        }
    )

# GET endpoint: Retrieve a user by name
@app.get("/users/{name}")
def get_user(name: str):

    # If the user is not "Mohzeba",
    # raise the custom exception
    if name != "Mohzeba":
        raise UserNotFoundException(name)

    # Return the user if found
    return {
        "name": name
    }