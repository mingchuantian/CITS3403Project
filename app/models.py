import os
from app import app, db, login_manager
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

#define shell content 
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Question=Question, Answer=Answer, QuizSet=QuizSet)

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
    #add a relationship between User and Quiz
    create_quizsets = db.relationship('QuizSet', backref='author', lazy='dynamic')
    answer_quizzes = db.relationship('Answer', backref='answerer', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return '<User>' + self.name


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
    quizset_id = db.Column(db.Integer, db.ForeignKey('quizsets.id'))
    student_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))


    def __repr__(self):
        return self.Answer 
