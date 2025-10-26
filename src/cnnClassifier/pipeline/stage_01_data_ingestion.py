from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier import logger
import os 
from dotenv import load_dotenv

load_dotenv()



STAGE_NAME = "Data Ingestion stage"



class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)

            container_name = os.getenv("STORAGE_ACCOUNT_CONTAINER")
            blob_name = "data.zip"
            # object_key = "data.zip"

            download_path = data_ingestion_config.local_data_file  # already set in config
            connection_string = os.getenv("STORAGE_ACCOUNT_CONNECTION")

            data_ingestion.download_from_blob(container_name, blob_name, download_path, connection_string)

            data_ingestion.extract_zip_file()

        except Exception as e:
            raise e