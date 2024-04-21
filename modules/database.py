from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import configparser
import os

ini = os.path.join(os.path.dirname(os.path.dirname(__file__)),"data",".config")
config = configparser.ConfigParser()
config.read(ini)
config_values= {}

for section in config.sections():
  config_values[section]={}
  for option in config.options(section):
    config_values[section][option]= config.get(section,option) 
    
DATABASE_URL = config_values['database']['database_url']
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base = declarative_base()