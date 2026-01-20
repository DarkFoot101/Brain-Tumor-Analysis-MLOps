import os
import urllib.request as request
import zipfile
from classifier import logger
from classifier.utils.common import get_size
from classifier.entity.config_entity import DataIngestionConfig
from pathlib import Path
import gdown

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data(self) -> Path:
        if not os.path.exists(self.config.local_data_file):

            url = self.config.source_URL

            # if it is a google drive link, download using gdown
            if "drive.google.com" in url:
                gdown.download(url, str(self.config.local_data_file), quiet=False)
                logger.info(f"Downloaded from Google Drive: {self.config.local_data_file}")
            else:
                filename, headers = request.urlretrieve(
                    url, self.config.local_data_file
                )
                logger.info(f"File: {filename} downloaded with info: \n{headers}")

        else:
            logger.info(
                f"File already exists of size: {get_size(Path(self.config.local_data_file))}"
            )

        return self.config.local_data_file

    def extract_zip_file(self) -> None:
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)  
        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(unzip_path)