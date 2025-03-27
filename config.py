import os
from dotenv import load_dotenv

load_dotenv()

# Kaggle dataset details
KAGGLE_DATASET = "lainguyn123/student-performance-factors"

# PostgreSQL settings
DB_USER = os.getenv("POSTGRES_USER", "postgres")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "1234")
DB_NAME = os.getenv("POSTGRES_DB", "students_data")
DB_HOST = os.getenv("POSTGRES_HOST", "localhost")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")

# Connection string
DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Data storage
TARGET_DIRECTORY = "data"
TABLE_NAME = "students_data"
