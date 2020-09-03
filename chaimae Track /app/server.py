from flask_script import Manager
from flask import Flask,request 
import os
import numpy as np
import pandas as pd
import json
from core import app
MODE = os.environ.get("FLASK_ENV")
manager = Manager(app)
@manager.command
def run():
    if MODE == "production":
        serve(app, host="0.0.0.0", port=int(os.getenv("PORT")))
    else:
        app.run(host="localhost", port=int(os.getenv("PORT")))
if __name__ == "__main__":
    manager.run()