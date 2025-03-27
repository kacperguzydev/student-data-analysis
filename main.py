import logging
from data_downloader import download_dataset
from data_uploader import upload_to_database
from data_analysis import execute_query, visualize_hours_to_score, visualize_gender_compare
from config import KAGGLE_DATASET, TARGET_DIRECTORY, DB_URL, TABLE_NAME

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    try:
        logger.info("Starting data pipeline...")

        dataset_path = download_dataset(KAGGLE_DATASET, TARGET_DIRECTORY)
        if not dataset_path:
            logger.error("Dataset download failed. Exiting.")
            return

        upload_to_database(dataset_path, DB_URL, TABLE_NAME)

        execute_query(DB_URL, f'SELECT AVG("Exam_Score") AS avg_score FROM {TABLE_NAME};')

        visualize_hours_to_score(DB_URL, TABLE_NAME)
        visualize_gender_compare(DB_URL, TABLE_NAME)

        logger.info("Pipeline execution completed successfully.")

    except Exception as e:
        logger.exception(f"Unexpected error in pipeline: {e}")

if __name__ == "__main__":
    main()
