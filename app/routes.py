from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm, RegisterForm


@app.route('/', methods = ['GET', 'POST'])
def index():
    form = RegisterForm()
    return render_template('index.html', registerForm = form)

'''
@app.route('/login')
def login():
    return null
'''