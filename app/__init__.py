import os
from flask import Flask     #flask is module and Flask is a class
from config import Config

#initialize a Flask object, and assign to 'app'
#app now is a Flask object
app = Flask(__name__)

app.config.from_object(Config)

from app import routes      #app is a folder name and there is route.py

