from app import app, db
from flask import render_template, flash, redirect, request, url_for
from app.forms import LoginForm, RegisterForm, QuizEditForm, QuizLoginForm, QuizStartForm, QuizAnswerForm
from flask_login import login_user, login_required, logout_user, current_user
from app.models import User, Question, QuizSet, Answer


@app.route('/', methods = ['GET', 'POST'])
def index():
    form = RegisterForm()
    if form.validate_on_submit():
        email = User.query.filter_by(email=form.email.data).first()
        if email is None:
            user = User(name=form.name.data, email=form.email.data, password=form.password.data, is_teacher=form.teacher.data)
            db.session.add(user)
            db.session.commit()
            return 'The user is successfully registered'
        else:
            return 'The user already exists!'

    return render_template('index.html', registerForm = form)


@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            if user.is_teacher == True:
                next = request.args.get('next')
                if next is None or not next.startswith('/'):
                    next = url_for('teacher')
                return redirect(next)
            else:
                next = request.args.get('next')
                if next is None or not next.startswith('/'):
                    next = url_for('student')
                return redirect(next)
        else:
            return 'The account does not exist'

    return render_template('login.html', loginForm = form)


@app.route('/student', methods = ['GET', 'POST'])
@login_required
def student():
    form = QuizLoginForm()
    if form.validate_on_submit():
        getQuiz = Quiz.query.filter_by(quiz_id=form.QuizID.data)
        if getQuiz is not None:
            return render_template('startQuiz.html')
        else:
            return 'the quiz does not exist!'
    return render_template('student.html', loginQuizForm = form)

@app.route('/teacher')
@login_required
def teacher():
    return render_template('teacher.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template('notify.html', content='You have been logged out.')
'''
#cannot determine whether teacher or student
@app.route('/editQuiz', methods = ['GET', 'POST'])
@login_required
def editQuiz():
    form = QuizEditForm()
    if form.validate_on_submit():
        quiz = Quiz(
        author=current_user,
        title=form.title.data, Q1=form.Q1.data, 
        Q1Answer1=form.Q1Answer1.data, Q1Answer2=form.Q1Answer2.data,
        Q1Answer3=form.Q1Answer3.data, Q1Answer4=form.Q1Answer4.data,
        Q2=form.Q2.data, Q2Answer1=form.Q2Answer1.data,
        Q2Answer2=form.Q2Answer2.data, Q2Answer3=form.Q2Answer3.data,
        Q2Answer4=form.Q2Answer4.data, quiz_id=form.quiz_id.data)
        db.session.add(quiz)
        db.session.commit()
        return 'Your quiz has been successfully submitted'
    return render_template('editQuiz.html',quizEditForm=form)
'''
@app.route('/startEditQuiz', methods = ['GET', 'POST'])
@login_required
def startEditQuiz():
    form = QuizStartForm()
    if form.validate_on_submit():
        num_question=form.question_num.data
        id_quiz = form.quiz_id.data
        quizset = QuizSet(title=form.title.data, quiz_id=id_quiz, question_num=num_question)
        db.session.add(quizset)
        db.session.commit()
        return redirect(url_for('editQuiz', qid=id_quiz))
    return render_template('startEditQuiz.html', quizStartForm=form)


@app.route('/editQuiz', methods = ['GET', 'POST'])
@login_required
#there's problem with it
def editQuiz(qid=qid):
    form = QuizEditForm()
    if form.validate_on_submit():
        quizId = QuizSet.query.filter_by(quiz_id=qid).first()
        question = Question(Question=form.question.data, quizset_id=quizId)
        db.session.add(question)
        db.session.commit()
        return 'you have finished editing'
    return render_template('editQuiz.html', quizEditForm=form)
    
    
