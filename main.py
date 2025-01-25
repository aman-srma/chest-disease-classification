from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import (DataIngestion, DataIngestionTrainingPipeline)
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>> Stage {STAGE_NAME} Started <<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>> Stage {STAGE_NAME} Completed <<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e





STAGE_NAME = "Prepare Base Model"

try:
    logger.info(f"*******************")
    logger.info(f">>>>> Stage {STAGE_NAME} Started <<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>> Stage {STAGE_NAME} Completed <<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e