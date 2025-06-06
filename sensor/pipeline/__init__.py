from sensor.exception import SensorException
from sensor.entity.artifact_entity import DataIngestionArtifact
from sensor.logger import logging
import sys
import os
from  sensor.components.data_ingestion import DataIngestion


class TrainPipeline:
    
    def __init__(self):
        self.training_pipeline_config = TrainingPipeLineConfig()
        
    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            
            self.data_ingestion_config = DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)
            
            logging.info("Starting Data ingestion")
            
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            
            logging.info(f"Data ingestion completed and artifact:(data_ingestion_artifact)")
            return data_ingestion_artifact
        except Exception as e:
            raise SensorException(e,sys)
        
    def run_pipeline(self):
        try:
            data_ingestion_artifact:DataIngestionArtifact = self.start_data_ingestion()
        except Exception as e:
            raise SensorException(e,sys)
        