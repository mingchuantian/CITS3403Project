from flask import Flask
from config import Config, TestConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

#create Flask object 'app'
app = Flask(__name__)
#configure app from Config
#now using testConfig
app.config.from_object(Config)

#create SQLAlchemy object 'db'
db = SQLAlchemy(app)

#create Migrate object 'migrate'
migrate = Migrate(app, db)

#create Bootstrap object bootstrap
bootstrap = Bootstrap(app)

#create login manager

login_manager = LoginManager()
login_manager.init_app(app)

#all codes from routes and models are following
from app import routes, models