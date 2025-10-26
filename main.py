from cnnClassifier import logger

logger.info("Starting the CNN Classifier application....")

from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
# from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
# from cnnClassifier.pipeline.stage_03_model_trainer import ModelTrainingPipeline
# from cnnClassifier.pipeline.stage_04_evaluation import EvaluationPipeline
from dotenv import load_dotenv

load_dotenv()


STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e