from fastapi import FastAPI

# Create a FastAPI application
app = FastAPI()

# GET endpoint: /users
@app.get("/users")
def get_users(name: str = None):
    # Accepts an optional query parameter 'name'
    return {"Name": name}

# GET endpoint: /products
@app.get("/products")
def get_users(limit: int = 10):
    # Accepts an optional query parameter 'limit'
    # Default value is 10
    return {"limit": limit}

# GET endpoint: /items
@app.get("/items")
def get_users(name: str = None, price: int = 0):
    # 'name' is an optional string query parameter (default = None)
    # 'price' is an optional integer query parameter (default = 0)

    # Return the received query parameters as JSON
    return {
        "name": name,
        "price": price
    }