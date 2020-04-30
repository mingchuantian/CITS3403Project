import os

#set the base directory as where I am
basedir = os.path.abspath(os.path.dirname(__file__))

#create class Config including all configuration
class Config(object):

    #get SECRET_KEY from the os environment
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dont even think about it'

    #set specs for SQLAlchemy
    #locate the database, if db is not found, create a new one
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
