from dotenv import load_dotenv
from pathlib import Path 
import os
env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)
class BaseConfig:
    DEBUG = False
    TESTING = False
    
class DevelopmentConfig(BaseConfig):
    DEBUG = True
    MONGODB_SETTINGS = dict(host=os.environ.get("DEV_DATABASE_URI")) #dict(host="mongodb://localhost:27017/dev_db")

class TestingConfig(BaseConfig):
    TESTING = True
    MONGODB_SETTINGS = dict(host=os.environ.get("TEST_DATABASE_URI")) #dict(host="mongodb://localhost:27017/test_db")

class ProductionConfig(BaseConfig):
    MONGODB_SETTINGS = dict(host=os.environ.get("PROD_DATABASE_URI"))
    DEBUG = False

config_by_name = dict(
    development = DevelopmentConfig,
    test = TestingConfig,
    production = ProductionConfig
)