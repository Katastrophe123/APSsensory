from dotenv import load_datenv
import pymongo
from sensor.constant.database import DATABASE_NAME
import certifi
ca = certifi.where()
from sensor.constant.env_variable import MONGODB_URL_KEY
import os
import logging

load_dotenv()

class MONGODBClient:
    client = None
    
    def __init__(self,database_name=DATABASE_NAME) -> None:
        try:
            if MONGODBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                logging.info(f"Retrieved MongoDB URL: {mongo_db_url}")
                
                if "localhost" in mongo_db_url:
                    MONGODBClient.client = pymongo.MongoClient(mongo_db_url)
                else:
                    MONGODBClient.client = pymongo.MongoClient(mongo_db_url,
                    tlsCAFile=ca)
            self.client = MONGODBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
        except Exception as e:
            logging.error(f"Error initializing MongoDB client: {e}")
            raise
