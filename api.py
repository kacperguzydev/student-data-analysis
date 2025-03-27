from fastapi import FastAPI
from sqlalchemy import create_engine
import pandas as pd
from config import DB_URL, TABLE_NAME

app = FastAPI()
engine = create_engine(DB_URL)

@app.get("/students")
def get_students():
    query = f"SELECT * FROM {TABLE_NAME} LIMIT 10;"
    df = pd.read_sql(query, engine)
    return df.to_dict(orient="records")
