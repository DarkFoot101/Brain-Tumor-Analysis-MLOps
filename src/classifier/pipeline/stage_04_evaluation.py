from classifier.config.configuration import ConfigurationManager
from classifier.components.evaluation import Evaluation
from classifier import logger
from classifier.constants import *
from pathlib import Path


STAGE_NAME = "Evaluation Stage"

class EvaluationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            evaluation_config = config.get_evaluation_config()
            evaluation = Evaluation(config=evaluation_config)
            evaluation.evaluation()
            evaluation.save_score()
        except Exception as e:
            logger.exception(e)
            raise e

if __name__ == "__main__":
    pipeline = EvaluationPipeline()
    pipeline.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")