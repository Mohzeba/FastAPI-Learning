from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()

# Database file path — SQLite will create test.db in the current directory
DATABASE_URL = "sqlite:///./test.db"

# Create the database engine — the core connection to the DB
# check_same_thread=False allows FastAPI to use it across multiple threads
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# SessionLocal is a factory — calling SessionLocal() gives you a new DB session
SessionLocal = sessionmaker(bind=engine)

# Base class — all models (tables) will inherit from this
Base = declarative_base()

# Todo model — maps to the "todos" table in the database
class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)  # auto increment ID
    title = Column(String)       # todo text
    completed = Column(String)   # completion status

# Creates all tables in the DB if they don't exist yet
Base.metadata.create_all(bind=engine)

# Dependency function — opens a DB session, yields it, then closes it after use
def get_db():
    db = SessionLocal()
    try:
        yield db      # gives the session to the endpoint
    finally:
        db.close()    # always closes even if an error occurs

#Create API
@app.post("/todos")
def create_todo(title:str,db: Session = Depends(get_db)):
    todo = Todo(title=title,completed="False")
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return{
        "message":"Todo Created",
        "data":todo
    }

#Read All Data
@app.get("/todos")
def get_todos(db:Session = Depends(get_db)):
    todos = db.query(Todo).all()

    return{
        "Total":len(todos),
        "data":todos
    }

#Read data based on ID
@app.get("/todos/{todo_id}")
def get_todo(todo_id:int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

#Update
@app.put("/todos/{todo_id}")
def update_todo(todo_id:int, title:str, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if not todo:
            raise HTTPException(status_code=404, detail="Todo not found")
        
    todo.title = title
    db.commit()
    db.refresh(todo)
    return{
        "message":"Todo Updated",
        "data": todo
    }

#DELETE
@app.delete("/todos/{todos_id}")
def delete_todo(todo_id:int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    db.delete(todo)
    db.commit()

    return {
        "message":"TODO Deleted"
    }
