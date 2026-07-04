from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    completed = Column(String)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Creates a new todo with title and default completed=False
@app.post("/todos")
def create_todo(title:str, db: Session = Depends(get_db)):
    todo = Todo(title=title, completed="False")  # build the todo object
    db.add(todo)        # stage it
    db.commit()         # save to DB
    db.refresh(todo)    # reload from DB to get the auto-generated id
    return{
        "message":"Todo Created",
        "data":todo
    }

# Fetches all todos from the DB and returns count + data
@app.get("/todos")
def get_todos(db:Session = Depends(get_db)):
    todos = db.query(Todo).all()  # SELECT * FROM todos
    return{
        "Total":len(todos),
        "data":todos
    }

# Fetches a single todo by ID, raises 404 if not found
@app.get("/todos/{todo_id}")
def get_todo(todo_id:int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()  # SELECT WHERE id=todo_id
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

# Finds todo by ID, updates its title, saves and returns updated data
@app.put("/todos/{todo_id}")
def update_todo(todo_id:int, title:str, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo.title = title  # update the field directly on the object
    db.commit()         # save changes
    db.refresh(todo)    # reload updated data from DB
    return{
        "message":"Todo Updated",
        "data": todo
    }

# Finds todo by ID, deletes it from DB
@app.delete("/todos/{todos_id}")
def delete_todo(todo_id:int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo)  # mark for deletion
    db.commit()      # execute deletion
    return {
        "message":"TODO Deleted"
    }