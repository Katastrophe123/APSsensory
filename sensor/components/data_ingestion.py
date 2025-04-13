from sensor.exception import SensorException
from sensor.logger import logging
import os 
import sys
from pandas import DataFrame
from sensor.entity.config_entity import DataIngestionConfig
from sensor.entity.artifact_entity import DataIngestionArtifact
from sensor.data_access.sensor_data import SensorData
from sklearn.model_selection import train_test_split

class DataIngestion:
    
    def __init__(self)
