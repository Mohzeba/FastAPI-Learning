from fastapi import FastAPI
from pydantic import BaseModel

# Create a FastAPI application
app = FastAPI()

# Temporary list to store todos (acts as a fake database)
todos = []

# Define the structure (schema) of a Todo item
class Todo(BaseModel):
    id: int             # Unique ID of the todo
    title: str          # Title of the todo
    completed: bool     # Completion status (True/False)

# POST endpoint: Create a new todo
@app.post("/todos")
def create_todo(todo: Todo):
    
    # Add the new todo to the list
    todos.append(todo)
    return {
        "message": "TODO added",
        "data": todo
    }

# GET endpoint: Retrieve all todos
@app.get("/todos")
def get_todos():
    # Return the complete list of todos
    return todos

# GET endpoint: Retrieve a specific todo by its ID
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):

    # Search for the todo with the given ID
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {"Error": "Todo not found"}

# PUT endpoint: Update an existing todo
@app.put("/tpdps/{todo_id}")   # (Typo: should be "/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):

    # Find the todo by its ID
    for index, todo in enumerate(todos):
        if todo.id == todo_id:

            # Replace the old todo with the updated one
            todos[index] = updated_todo

            # Return the updated todo
            return {
                "message": "Data Updated",
                "data": updated_todo
            }
    return {"error": "Todo not found"}

# DELETE endpoint: Delete a todo by its ID
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):

    # Search for the todo by its ID
    for index, todo in enumerate(todos):
        if todo.id == todo_id:

            # Remove the todo from the list
            todos.pop(index)
            return {"message": "Data Deleted"}
    return {"Error": "Todo not found"}