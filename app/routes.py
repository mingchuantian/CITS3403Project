from app import app, db
from flask import render_template, flash, redirect, request
from app.forms import LoginForm, RegisterForm
from flask_login import login_user, login_required
from app.models import Student, Teacher


@app.route('/', methods = ['GET', 'POST'])
def index():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.teacher.data is True:
            email = Teacher.query.filter_by(email=form.email.data).first()
            if email is None:
                user = Teacher(name=form.name.data, email=form.email.data, password=form.password.data)
                db.session.add(user)
                db.session.commit()
                return 'The teacher account is successfully registered'
            else:
                return 'The user already exists!'
        else:
            email = Student.query.filter_by(email=form.email.data).first()
            if email is None:
                user = Student(name=form.name.data, email=form.email.data, password=form.password.data)
                db.session.add(user)
                db.session.commit()
                return 'The student account is successfully registered'
            else:
                return 'The user already exists!'
    return render_template('index.html', registerForm = form)


@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.teacher.data is True:
            user = Teacher.query.filter_by(email=form.email.data).first()
            if user is not None and user.verify_password(form.password.data):
                login_user(user, form.remember_me.data)
                return 'you are now logged in as teacher'
            else:
                'The teacher does not exist'
        else:
            user = Student.query.filter_by(email=form.email.data).first()
            if user is not None and user.verify_password(form.password.data):
                login_user(user, form.remember_me.data)
                return 'you are now logged in as student'
            else:
                'The student does not exist'
    return render_template('login.html', loginForm = form)


@app.route('/secret')
@login_required
def secret():
    return 'Only authenticated users are allowed!'