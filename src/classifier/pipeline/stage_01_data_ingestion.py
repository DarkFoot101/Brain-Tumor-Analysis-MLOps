from classifier.config.configuration import ConfigurationManager
from classifier.components.data_ingestion import DataIngestion
from classifier import logger
import gdown

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_data()
            data_ingestion.extract_zip_file()
            logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
        except Exception as e:
            logger.exception(e)
            raise e

if __name__ == "__main__":
    pipeline = DataIngestionPipeline()
    pipeline.main()