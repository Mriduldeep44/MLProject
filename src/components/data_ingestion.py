import os
import sys
import src.components.exception import CustomException
from src.components.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join("artifacts","train.csv")
    test_data_path:str=os.path.join("artifacts","test.csv")
    raw_data_path:str=os.path.join("artifacts",'raw.csv')
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig() #ingestion_config is the class variable
    def initiate_data_ingestion(self): #we are using it for reading the data from the database or any other place
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv("")
        except:
            pass