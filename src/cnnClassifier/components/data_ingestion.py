import os
import zipfile
import gdown
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config 


    def download_file(self) -> str:
        '''
        Fetch data from the url
        '''

        try:
            dataset_url = self.config.source_URL
            zip_download_dir = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion", exist_ok=True)
            logger.info(f"Downloading dataset from {dataset_url} to {zip_download_dir}")

            file_id = dataset_url.split("/")[-2]
            prefix = "https://drive.google.com/uc?/export=download&id="
            gdown.download(prefix + file_id, zip_download_dir)

            logger.info(f"Downloaded dataset from {dataset_url} into file {zip_download_dir}")

        except Exception as e:
            logger.error(f"Error downloading dataset from {dataset_url} to {zip_download_dir}")
            raise e
        
    def extract_zip_file(self):
        '''
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        '''
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            logger.info(f"Extracting zip file {self.config.local_data_file} to {unzip_path}")
            zip_ref.extractall(unzip_path)
            logger.info(f"Extracted zip file {self.config.local_data_file} to {unzip_path}")
