import re
import os
from app import app
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from app.forms import Register, Login       #app.forms is folder, Register and Login are classes
from app import data


bootstrap = Bootstrap(app)


@app.route('/', methods=['GET','POST']) #register the view function as a handler for GET and POST requests. 
def index():
    form = Register()
    if form.validate_on_submit():
        if compareUsername(form.email.data, str(User.query.filter_by(email=form.email.data).first())):
            return 'this user already exists!'
        else:
            #specifying a new row
            user = User(email=form.email.data, password=form.password.data)
            db.session.add(user)
            db.session.commit()
            return 'the user is successfully registered!'
    return render_template('index.html', registerForm=form)


@app.route('/login', methods=['GET','POST'])
def login():
    form = Login()
    if form.validate_on_submit():
        if compareUsername(form.email.data , str(User.query.filter_by(email=form.email.data).first())):
            if comparePassword(form.password.data, str(User.query.filter_by(email=form.email.data).first())):
                return 'you are successfully logged in'
            else:
                return 'your email exists but password is incorrect'
        else:
            return 'your username does not exist'
    return render_template('login.html', loginForm = form)

'''
@app.route('/regist')
def button():
    return render_template('login.html', loginForm = Login())
'''

@app.route('/user/<username>')
def show_user(username):
    return 'User' + username

#This function compares username regardless of whitespace
def compareUsername(inputEmail, dictionary):
    databaseEmail = dictionary['emial']
    return re.sub("\s*", "", inputEmail) == re.sub("\s*", "", databaseEmail)

def comparePassword(inputPassword, dictionary):
    databasePassword = dictionary['password']
    return re.sub("\s*", "", inputPassword) == re.sub("\s*", "", databasePassword)