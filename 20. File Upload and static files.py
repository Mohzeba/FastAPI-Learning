from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.staticfiles import StaticFiles
import os
import shutil

app = FastAPI()

#step 1: ensure uploads folder exists
UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

#step 2: static file setup
app.mount("/uploads", StaticFiles(directory=UPLOAD_DIR), name="files")

#step 3: upload file api
@app.post("/upload/")
def upload_file(file: UploadFile = File(...)):
    filename = file.filename
    file_path = os.path.join(UPLOAD_DIR, filename)

    if not filename:
        raise HTTPException(status_code=400, detail="No file uploaded")
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

        return {
            "message": "File uploaded successfully",
            "filename": filename,
            "file_url":f"https://cautious-carnival-5gr647pvwrpjh4rrw-8000.app.github.dev/uploads/{filename}"
        }

#step 4: Get file URL API

@app.get("/files/{filename}")
def get_file(filename: str):
    file_path = os.path.join(UPLOAD_DIR, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    
    return {
        "file_url":f"https://cautious-carnival-5gr647pvwrpjh4rrw-8000.app.github.dev/uploads/{filename}"
        }

@app.get("/")
def home():
    return{
        "message":"File upload api running"
    }