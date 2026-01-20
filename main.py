from classifier import logger
from classifier.config.configuration import ConfigurationManager
from classifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from classifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline
from classifier.pipeline.stage_03_prepare_callbacks import PrepareCallbacksPipeline
from classifier.pipeline.stage_04_training import ModelTrainingPipeline
from classifier.pipeline.stage_05_evaluation import EvaluationPipeline


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    pipeline = DataIngestionPipeline()
    pipeline.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e 

STAGE_NAME = "Prepare Base Model Stage"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    pipeline = PrepareBaseModelPipeline()
    pipeline.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare Callbacks Stage"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    pipeline = PrepareCallbacksPipeline()
    pipeline.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Training Stage"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    pipeline = ModelTrainingPipeline()
    pipeline.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Evaluation Stage"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    pipeline = EvaluationPipeline()
    pipeline.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e