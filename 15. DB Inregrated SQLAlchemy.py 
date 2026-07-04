from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from fastapi import FastAPI, Depends

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

# Inject the DB session using Depends — confirms DB is connected
@app.get("/")
def home(db: Session = Depends(get_db)):
    return {
        "message": "DB connected fine"
    }