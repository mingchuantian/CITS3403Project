import os

#for database setting
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    
    #set configurations
    SECRET_KEY = os.environ.get('SECRET_KEY') or "this-is-a-secret-key"
    #database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False    
