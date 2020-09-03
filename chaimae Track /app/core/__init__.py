from flask_mongoengine import MongoEngine
from core.src.configs import config
from flask import Flask
from flask_restplus import Api
import os
db = MongoEngine()
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config.config_by_name[config_name])
    db.init_app(app)
    return app

MODE = os.environ.get("FLASK_ENV")
app = create_app(MODE)
api = Api(app=app,
          title = "tRACLER  SERVICE" ,
          version = "1.0",
          description = """tRACKer.""",
          doc = '/')
          