import os
from dotenv import load_dotenv

load_dotenv() #load env variables

class Settings:
    SECRET_KEY = os.getenv("SECRET_KEY")
    ORIGINS = [os.getenv("ORIGINS")]
    DB_URL = os.getenv("DB_URL")

setting = Settings()