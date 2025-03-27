import pandas as pd
from sqlalchemy import create_engine
import logging

logger = logging.getLogger(__name__)

def clean_data(df):
    df.dropna(inplace=True)
    df = df[df["Exam_Score"].between(0, 100)]
    return df

def upload_to_database(csv_path, connection_string, table_name):
    try:
        logger.info(f"Uploading data to {table_name}...")
        engine = create_engine(connection_string)
        df = pd.read_csv(csv_path)

        df = clean_data(df)

        df.to_sql(table_name, engine, if_exists='replace', index=False)

        logger.info(f"Data uploaded to {table_name} successfully.")

    except Exception as e:
        logger.error(f"Error uploading data: {e}")
