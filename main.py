from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import (DataIngestion, DataIngestionTrainingPipeline)

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>> Stage {STAGE_NAME} Started <<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(">>>>> Stage {STAGE_NAME} Completed <<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e