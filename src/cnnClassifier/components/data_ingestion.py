# import boto3
import os
from dotenv import load_dotenv
# from botocore.exceptions import ClientError
from azure.storage.blob import BlobServiceClient
from azure.core.exceptions import ResourceNotFoundError
import zipfile
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
import tempfile
from cnnClassifier.entity.config_entity import DataIngestionConfig

load_dotenv()

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config



    def download_from_blob(self, container_name, blob_name, download_path, connection_string):
        try:
            print(f"Downloading '{blob_name}' from container '{container_name}' to '{download_path}'...")

            # Initialize the BlobServiceClient
            blob_service_client = BlobServiceClient.from_connection_string(connection_string)
            blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

            # Download the blob
            with open(download_path, "wb") as f:
                download_stream = blob_client.download_blob()
                f.write(download_stream.readall())

            print("Download complete.")

        except ResourceNotFoundError:
            print(f"Error: Blob '{blob_name}' not found in container '{container_name}'.")
        except Exception as e:
            print(f"Unexpected error: {e}")
            

    def extract_zip_file(self):
        """
        Extracts the zip file into the data directory specified by self.config.unzip_dir.
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(unzip_path)