import os, hashlib
from app import app, db, login_manager
from flask import request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

#define shell content 
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Question=Question, Answer=Answer, QuizSet=QuizSet, Grade=Grade)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(128))
    is_teacher = db.Column(db.Boolean)
    faculty = db.Column(db.String(64))
    title = db.Column(db.String(64))
    phone = db.Column(db.Integer)
    address = db.Column(db.Text)
    avatar_hash = db.Column(db.String(32))

    #add a relationship between User and Quiz
    create_quizsets = db.relationship('QuizSet', backref='author', lazy='dynamic')
    answer_quizzes = db.relationship('Answer', backref='answerer', lazy='dynamic')
    graded = db.relationship('Grade', backref='gradedAnswerer', lazy='dynamic')

    
    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        #if self.email is not None and self.avatar_hash is None:
        self.avatar_hash = self.gravatar_hash()
    
    
    def change_email(self, new_email):
        self.email = new_email
        self.avatar_hash = self.gravatar_hash()

        db.session.add(self)
        #return True
    

    def gravatar_hash(self):
        return hashlib.md5(self.email.lower().encode('utf-8')).hexdigest()

    def gravatar(self, size=100, default='identicon', rating='g'):
        if request.is_secure:
            url = 'https://secure.gravatar.com/avatar'
        else:
            url = 'http://www.gravatar.com/avatar'
        hash = self.avatar_hash or self.gravatar_hash()
        #hash = hashlib.md5(self.email.lower().encode('utf-8')).hexdigest()
        return '{url}/{hash}?s={size}&d={default}&r={rating}'.format(url=url, hash=hash, size=size, default=default, rating=rating)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return '<User>' + str(self.name)


class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    Question = db.Column(db.Text)
    quizset_id = db.Column(db.Integer, db.ForeignKey('quizsets.id'))
    answers = db.relationship('Answer', backref='answerperson', lazy='dynamic')

    def __repr__(self):
        return '<Question>' + str(self.Question)

class QuizSet(db.Model):
    __tablename__ = 'quizsets'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    quiz_id = db.Column(db.String, unique=True)
    question_num = db.Column(db.Integer)
    questions = db.relationship('Question', backref='quizset', lazy='dynamic')
    answers = db.relationship('Answer', backref='answerman', lazy='dynamic')
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))


    def __repr__(self):
        return '<Quizset>' + str(self.id)

class Answer(db.Model):
    __tablename__ = 'answers'
    id = db.Column(db.Integer, primary_key=True)
    Answer = db.Column(db.Text)
    marked = db.Column(db.Boolean)
    quizset_id = db.Column(db.Integer, db.ForeignKey('quizsets.id'))
    student_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))
    #add relationship between Answer and Grade
    graded = db.relationship('Grade', backref='answer', lazy='dynamic')

    def mark(self):
        self.marked = True
        db.session.add(self)

    def is_marked(self):
        return self.marked
    
    def __repr__(self):
        #return str(self.Answer)
        return str(self.student_id) + ',' + str(self.id) + ',' + str(self.Answer) + ',' + str(self.question_id) +  ','+ str(self.quizset_id)

class Grade(db.Model):
    __tablename__='grades'
    id = db.Column(db.Integer, primary_key=True)
    mark = db.Column(db.Integer)
    comment = db.Column(db.String)
    answer_id = db.Column(db.Integer, db.ForeignKey('answers.id'))
    answerer_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return str(self.answer_id) + ',' + str(self.mark) + ',' + str(self.comment)
