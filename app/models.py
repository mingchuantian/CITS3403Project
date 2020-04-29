import os
from app import app, db
from flask_sqlalchemy import SQLAlchemy

#define shell content 
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))
    
    def __repr__(self):
        #make returned query a dictionary that contains both email and password
        return self.name
