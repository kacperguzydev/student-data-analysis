from sqlalchemy import create_engine, text
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging

logger = logging.getLogger(__name__)

def execute_query(connection_string, sql_query):
    try:
        engine = create_engine(connection_string)
        with engine.connect() as connection:
            result = connection.execute(text(sql_query))
            answer = result.fetchone()
            if answer:
                logger.info(f"Query result: {answer[0]}")
    except Exception as e:
        logger.error(f"Database query failed: {e}")

def visualize_hours_to_score(connection_string, table_name):
    try:
        engine = create_engine(connection_string)
        query = f'SELECT "Sleep_Hours", "Exam_Score" FROM {table_name};'
        df = pd.read_sql(query, engine)

        plt.figure(figsize=(10, 6))
        plt.scatter(df["Sleep_Hours"], df["Exam_Score"], alpha=0.5)
        plt.xlabel("Sleep Hours")
        plt.ylabel("Exam Score")
        plt.title("Sleep Hours vs Exam Scores")
        plt.grid()
        plt.show()

    except Exception as e:
        logger.error(f"Visualization error: {e}")

def visualize_gender_compare(connection_string, table_name):
    try:
        engine = create_engine(connection_string)
        query = f'SELECT "Gender", "Exam_Score" FROM {table_name};'
        df = pd.read_sql(query, engine)

        avg_scores = df.groupby("Gender")["Exam_Score"].mean().reset_index()

        plt.figure(figsize=(10, 6))
        sns.barplot(x="Gender", y="Exam_Score", data=avg_scores, palette="Set2")
        plt.title("Average Exam Scores by Gender")
        plt.xlabel("Gender")
        plt.ylabel("Average Exam Score")
        plt.grid()
        plt.show()

    except Exception as e:
        logger.error(f"Visualization error: {e}")
