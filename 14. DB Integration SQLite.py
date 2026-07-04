import sqlite3
from fastapi import FastAPI

app = FastAPI()

# Connect to SQLite database file called test.db
# check_same_thread=False allows FastAPI to use the connection across multiple threads
conn = sqlite3.connect("test.db", check_same_thread=False)

# Create a cursor — used to execute SQL queries
cursor = conn.cursor()

# Create a todos table if it doesn't already exist
# id = auto primary key, title = todo text, completed = done status
cursor.execute("""
CREATE TABLE IF NOT EXISTS todos (
               id INTEGER PRIMARY KEY,
               title TEXT,
               completed TEXT
            )
""")

# Save/commit the table creation to the database
conn.commit()

# Basic GET endpoint just to confirm the app is running and SQLite is connected
@app.get("/")
def home():
    return{
        "message":"SQLite Connected"
    }