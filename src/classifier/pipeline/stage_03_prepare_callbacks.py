from classifier.config.configuration import ConfigurationManager
from classifier.components.prepare_callbacks import PrepareCallbacks
from classifier import logger
from classifier.constants import *
from pathlib import Path


STAGE_NAME = "Prepare Callbacks Stage"

class PrepareCallbacksPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
            config = ConfigurationManager()
            prepare_callbacks_config = config.get_prepare_callbacks_config()
            prepare_callbacks = PrepareCallbacks(config=prepare_callbacks_config)
            callback_list = prepare_callbacks.get_callbacks()
        
            logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
        except Exception as e:
            logger.exception(e)
            raise e

if __name__ == "__main__":
    pipeline = PrepareCallbacksPipeline()
    pipeline.main()
