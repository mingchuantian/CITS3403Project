import os

#for database setting
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    #set configurations
    SECRET_KEY = os.environ.get('SECRET_KEY') or "this-is-a-secret-key"
