from fastapi import FastAPI, status, HTTPException

# Create a FastAPI application
app = FastAPI()

# POST endpoint: Create a new user
# Returns HTTP status code 201 (Created) on success
@app.post("/create_user", status_code=status.HTTP_201_CREATED)
def create_user():
    return {
        "message": "User Created"
    }

# GET endpoint: Retrieve user information
@app.get("/user")
def get_users():

    # Return a success response with user data
    return {
        "status": "Success",
        "message": "User Fetched",
        "data": {
            "name": "Mohzeba",
            "age": 22
        }
    }

# GET endpoint: Retrieve a specific user by ID
@app.get("/users/{user_id}")
def get_user(user_id: int):

    # If the requested user ID is not 1,
    # raise a 404 (Not Found) error
    if user_id != 1:
        raise HTTPException(
            status_code=404,
            detail="User Not Found"
        )

    # Return user details if ID is 1
    return {
        "id": 1,
        "name": "Mohzeba"
    }