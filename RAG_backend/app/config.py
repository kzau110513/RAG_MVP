import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret")
    DEBUG = os.getenv("DEBUG", True)
    DATABASE_URL = os.getenv("DATABASE_URL")
    MODEL_NAME = os.getenv("MODEL_NAME")