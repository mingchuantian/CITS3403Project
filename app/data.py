import os
from app import app
from flask_sqlalchemy import SQLAlchemy

#for database setting
basedir = os.path.abspath(os.path.dirname(__file__))
#database configuration
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')
#database use less memory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#initialize database object
db = SQLAlchemy(app)

#define shell content 
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))
    
    def __repr__(self):
        #make returned query a dictionary that contains both email and password
        return self.__dict__