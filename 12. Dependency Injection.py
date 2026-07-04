from fastapi import FastAPI, Depends, Header, HTTPException

app = FastAPI()

# Checks if the token sent in the request header is valid
def verify_token(token: str = Header(None)):
    # If token is wrong, block the request with 401
    if token != "mysecrettoken":
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )
    # If correct, return authorized user info
    return {
        "user":"Authorized User"
    }

# verify_token runs first before this endpoint executes
# if token is invalid, this never runs
@app.get("/secure-data")
def secure_data(user = Depends(verify_token)):
    return {
        "message": "Secure data accessed",
        "user":user
    }

# Returns the current hardcoded user
def get_current_user():
    return{
        "user":"Mohzeba"
    }

# Both endpoints reuse get_current_user — write once, use everywhere
@app.get("/profile")
def profile(user = Depends(get_current_user)):
    return user

@app.get("/dashboard")
def dashboard(user = Depends(get_current_user)):
    return user