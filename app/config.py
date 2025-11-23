import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://user:password@localhost/library_db")
    ADMIN_API_TOKEN = os.getenv("ADMIN_API_TOKEN", "secret-admin-token")
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")