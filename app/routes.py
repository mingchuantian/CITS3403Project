from app import app, db
from flask import render_template, flash, redirect, request, url_for
from app.forms import LoginForm, RegisterForm, QuizEditForm, QuizLoginForm, QuizStartForm, QuizAnswerForm, QuizReviewForm, changeQuestionForm, QuizMarkForm, GradingForm
from flask_login import login_user, login_required, logout_user, current_user
from app.models import User, Question, QuizSet, Answer, Grade


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
        if QuizSet.query.filter_by(quiz_id=form.QuizID.data).first() is None:
            return 'You entered a wrong quizset ID!'
        QuizsetID = QuizSet.query.filter_by(quiz_id=form.QuizID.data).first().id
        if QuizsetID is not None:     
            return redirect(url_for('startQuiz', QuizsetID = QuizsetID, current_question=1)) #render_template('startQuiz.html')
        else:
            return 'the quiz does not exist!'
    return render_template('student.html', loginQuizForm = form)


@app.route('/startQuiz/<QuizsetID>/<current_question>', methods = ['GET', 'POST'])
@login_required
def startQuiz(QuizsetID, current_question):
    if QuizSet.query.filter_by(id=QuizsetID).first() is None:
        return 'You entered a wrong quizset ID!'
    current_question = int(current_question)
    question_num = QuizSet.query.filter_by(id=QuizsetID).first().question_num
    teacher_id = QuizSet.query.filter_by(id=QuizsetID).first().author_id
    teacher_name = User.query.filter_by(id=teacher_id).first().name

    #calculate previous questions number
    prev_num = Prev_Questions_num(QuizsetID)
    form = QuizAnswerForm()

    #calculate current question ID
    #current_question_id = Question.query.filter_by(quizset_id=QuizsetID, id= prev_num+current_question-1).first().id
    if form.validate_on_submit():
        answer = Answer(Answer=form.answer.data, question_id=prev_num+current_question, quizset_id=QuizsetID, student_id=current_user.id)
        db.session.add(answer)
        db.session.commit()
        return redirect(url_for('answerSaved', current_question=current_question, QuizsetID=QuizsetID))

    return render_template('startQuiz.html', prev_num=prev_num, QuizsetID=QuizsetID, current_question=current_question, Question=Question, teacher_name=teacher_name, question_num=question_num, form=form)


def Prev_Questions_num(QuizsetID):
    counts = 0
    for i in range(1, int(QuizsetID)):
        counts = counts + Question.query.filter_by(quizset_id=i).count()
    return counts



@app.route('/answerSaved/<current_question>/<QuizsetID>', methods = ['GET', 'POST'])
@login_required
def answerSaved(current_question, QuizsetID):
    current_question = int(current_question) + 1
    return redirect(url_for('startQuiz', current_question=current_question, QuizsetID=QuizsetID))



@app.route('/finishQuiz')
@login_required
def finishQuiz():
    return render_template('notify.html', content='You have finished your quiz', buttonText='Back to profile page', link=url_for('student'))



@app.route('/teacher', methods = ['GET', 'POST'])
@login_required
def teacher():
    form = QuizReviewForm()

    if form.validate_on_submit() and form.QuizID.data is not None:
        QuizID=form.QuizID.data
        quizset = QuizSet.query.filter_by(quiz_id=QuizID).first()
        if quizset is not None:
            quizsetID = quizset.id
            current_question_id = Prev_Questions_num(quizsetID) + 1
            question_n = 0
            return redirect(url_for('reviewQuiz', quizsetID=quizsetID, current_question_id=current_question_id, question_n=question_n))
        else: 
            return 'the quiz does not exists'

    return render_template('teacher.html',  form=form)







@app.route('/markQuiz', methods = ['GET', 'POST'])
@login_required
def markQuiz():
    form = QuizMarkForm()
    if form.validate_on_submit():
         
        if QuizSet.query.filter_by(quiz_id=form.QuizID.data).first() is None:
            return 'You entered a wrong quizset ID!'
        else:
            quizsetID = QuizSet.query.filter_by(quiz_id=form.QuizID.data).first().id
            answer_num = Answer.query.filter_by(quizset_id=quizsetID).count()
            current_answer = 0
            return redirect(url_for('reviewAnswer', quizsetID=quizsetID, answer_num=answer_num, current_answer=current_answer))
    return render_template('findQuizToMark.html', form=form)




@app.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template('notify.html', content='You have been logged out.')


@app.route('/startEditQuiz', methods = ['GET', 'POST'])
@login_required
def startEditQuiz():
    form = QuizStartForm()
    if form.validate_on_submit():
        num_question=form.question_num.data
        id_quiz = form.quiz_id.data
        quizset = QuizSet(title=form.title.data, quiz_id=id_quiz, question_num=num_question, author_id=current_user.id)
        db.session.add(quizset)
        db.session.commit()
        quizset_id = QuizSet.query.filter_by(quiz_id=id_quiz).first().id
        return redirect(url_for('editQuiz', current_question=1, QuizsetID=quizset_id, num_question=num_question))
    return render_template('startEditQuiz.html', quizStartForm=form)


@app.route('/editQuiz/<QuizsetID>/<num_question>/<current_question>',  methods = ['GET', 'POST'])
@login_required
#there's problem with it
def editQuiz(QuizsetID, num_question, current_question):
    form = QuizEditForm()
    question_num = int(num_question)
    current_question = int(current_question)
    if form.validate_on_submit():
        #quizId = QuizSet.query.filter_by(quiz_id=qid).first().id
        question = Question(Question=form.question.data, quizset_id=QuizsetID)
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('questionSaved', current_question=current_question, QuizsetID=QuizsetID, num_question=question_num))
    return render_template('editQuiz.html', quizEditForm=form, current_question=current_question, question_num=question_num)
    
@app.route('/questionSaved/<current_question>/<QuizsetID>/<num_question>', methods = ['GET', 'POST'])
@login_required
def questionSaved(current_question, QuizsetID, num_question):
    current_question = int(current_question) + 1
    return redirect(url_for('editQuiz', current_question=current_question, QuizsetID=QuizsetID, num_question=num_question))




@app.route('/reviewAnswer/<quizsetID>/<current_answer>/<answer_num>', methods = ['GET', 'POST'])
@login_required
def reviewAnswer(quizsetID,current_answer,answer_num):

    form = GradingForm()
    current_answer = int(current_answer)
    answer_num = int(answer_num)
    if quizsetID is None:
        return 'the quiz does not exists'
    if current_answer is answer_num:
        return 'you have graded all answers'
    else: 
        answer_dict = Answer.query.filter_by(quizset_id=quizsetID).all()
        answer = str(answer_dict[int(current_answer)])
        answer = answer.split(",")
        if form.validate_on_submit():
            grade = Grade(mark=form.mark.data, comment=form.comment.data, answer_id=answer[1], answerer_id=int(answer[0]))
            db.session.add(grade)
            db.session.commit()
            return redirect(url_for('nextAnswer', quizsetID=quizsetID, current_answer=current_answer, answer_num=answer_num))
        return render_template('reviewAnswer.html', answer=answer[2], form=form)


@app.route('/nextAnswer/<quizsetID>/<current_answer>/<answer_num>', methods = ['GET', 'POST'])
@login_required
def nextAnswer(quizsetID, current_answer, answer_num):
    current_answer = int(current_answer) + 1
    return redirect(url_for('reviewAnswer', current_answer=current_answer, quizsetID=quizsetID, answer_num=answer_num))





@app.route('/reviewQuiz/<quizsetID>/<current_question_id>/<question_n>', methods = ['Get', 'POST'])
@login_required
def reviewQuiz(quizsetID,current_question_id, question_n):

    if(current_user.id is not QuizSet.query.filter_by(id=quizsetID).first().author_id):
        return 'you cannot edit the quiz because you are not the author'
    elif(int(question_n) is QuizSet.query.filter_by(id=quizsetID).first().question_num):
        return 'you have done editing all questions in this quizset'
    else:
        current_question_id = int(current_question_id)
        form=changeQuestionForm()
        if form.validate_on_submit():
            changeQuestion = Question.query.filter_by(id=current_question_id).first()
            changeQuestion.Question=form.newQuestion.data
            db.session.commit()
            return redirect(url_for('nextQuestion', current_question_id=current_question_id, quizsetID=quizsetID, question_n=question_n))
        return render_template('reviewQuiz.html',  form=form, Question=Question, current_question_id=current_question_id)

@app.route('/nextQuestion/<current_question_id>/<quizsetID>/<question_n>', methods = ['Get', 'POST'])
@login_required
def nextQuestion(current_question_id, quizsetID, question_n):
    current_question_id = int(current_question_id) + 1
    question_n = int(question_n) + 1
    return redirect(url_for('reviewQuiz', current_question_id=current_question_id, quizsetID=quizsetID, question_n=question_n))


@app.route('/viewGrade',  methods = ['GET', 'POST'])
@login_required
def viewGrade():
    grade_dict = Grade.query.filter_by(answerer_id=current_user.id).all()
    
    #grade = grade_dict[0]
    #grade = grade.split(",")
    return render_template('viewGrade.html', grade_dict=grade_dict, str=str, Answer=Answer)


@app.route('/viewRanking',  methods = ['GET', 'POST'])
@login_required
def viewRanking():
    #get all quizsets ID recorded in this user's answers
    quizsets_taken = []
    answerlist = Answer.query.filter_by(student_id=current_user.id).all()
    for key in answerlist:
        each_answerlist = str(key)
        each_answerlist = each_answerlist.split(',')
        this_quizset = each_answerlist[3]
        quizsets_taken.append(this_quizset)

    #get unique quizsets ID
    unique_quizsets = unique_items(quizsets_taken)

    all_marks = []
    all_students_id = []

    return render_template('viewRanking.html', unique_quizsets=unique_quizsets, QuizSet=QuizSet, User=User, Answer=Answer, Grade=Grade, str=str, all_marks=all_marks, calcualte_total_mark=calcualte_total_mark, calculate_ranking=calculate_ranking, all_students_id=all_students_id, len=len, unique_items=unique_items)

def calcualte_total_mark(all_marks):
    total_mark = 0
    for marks in all_marks:
        ###!!!!!!theres bug when user is not graded
        total_mark = total_mark + marks
    return total_mark 

def calculate_ranking(all_students_id, quizset_id, student_mark):
    all_students_id = unique_items(all_students_id)
    all_students_total_marks = []
    for each_student_id in all_students_id:
        all_marks = []
        #calculate mark for each student
        for answers in Answer.query.filter_by(quizset_id=quizset_id, student_id=each_student_id).all():
            all_marks.append(Grade.query.filter_by(answer_id = str(answers).split(',')[1]).first().mark)
        all_students_total_marks.append(calcualte_total_mark(all_marks))
    all_students_total_marks.sort(reverse=True)
    rank = all_students_total_marks.index(student_mark) + 1

    return rank

def unique_items(all_items):
    unique_items = []
    for key in all_items: 
        if key not in unique_items:
            unique_items.append(key)
    return unique_items

#bug: teacher will unevidably regrade questions. Thus students receive double marks which result in faulty ranking