import os
import kagglehub
import logging

logger = logging.getLogger(__name__)

def download_dataset(dataset_name, target_directory):
    try:
        logger.info(f"Downloading dataset: {dataset_name}")
        path = kagglehub.dataset_download(dataset_name)
        csv_file = os.path.join(path, 'StudentPerformanceFactors.csv')

        if not os.path.exists(csv_file):
            logger.error("Dataset file not found.")
            return None

        logger.info("Dataset downloaded successfully.")
        return csv_file

    except Exception as e:
        logger.error(f"Error downloading dataset: {e}")
        return None
