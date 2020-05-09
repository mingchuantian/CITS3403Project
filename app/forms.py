from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, TextField, validators
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):

    email = StringField("Email", validators = [DataRequired()])
    password = PasswordField("Password", validators = [DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")

class RegisterForm(FlaskForm):
    name = StringField("Name", validators = [DataRequired()])
    email = StringField("Email", validators = [DataRequired()])
    password = PasswordField("Password", validators = [DataRequired()])
    teacher = BooleanField("Register as teacher")
    submit = SubmitField("Sign up")

'''
class QuizEditForm(FlaskForm):
    title = StringField("Quiz Title", validators = [DataRequired()])
    Q1 = StringField("Question 1: ")
    Q1Answer1 = StringField("Q1 Answer1: ")
    Q1Answer2 = StringField("Q1 Answer2: ")
    Q1Answer3 = StringField("Q1 Answer3: ")
    Q1Answer4 = StringField("Q1 Answer4: ")
    Q2 = StringField("Question 2: ")
    Q2Answer1 = StringField("Q2 Answer1: ")
    Q2Answer2 = StringField("Q2 Answer2: ")
    Q2Answer3 = StringField("Q2 Answer3: ")
    Q2Answer4 = StringField("Q2 Answer4: ")
    #validator does not work
    quiz_id = StringField("Quiz ID (must be 5 digits): ", [validators.Length(min=5, max=5)])
    submit = SubmitField("Submit")
'''

#For starting a new quiz
class QuizStartForm(FlaskForm):
    title = StringField("Quiz Title", validators = [DataRequired()])
    quiz_id = StringField("Give your quiz an ID", validators = [DataRequired()])
    #need to restrict the number of questions
    #question_num = StringField("Number of questions", validators = [DataRequired()])
    question_num = SelectField("Number of questions", choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5')])
    submit = SubmitField("Continue")

#For teachers adding questions to the new quiz
class QuizEditForm(FlaskForm):
    question = StringField("Question: ", validators = [DataRequired()])
    submit = SubmitField("save question")

#For students adding answers to existing quiz
class QuizAnswerForm(FlaskForm):
    answer = StringField("Answer: ", validators = [DataRequired()])
    submit = SubmitField("save answer")

#For students retrieving quiz
class QuizLoginForm(FlaskForm):
    QuizID = StringField("QuizID: ")
    submit = SubmitField("Start Quiz!")

#For teacher retrieving quiz to be changed/modified
class QuizReviewForm(FlaskForm):
    QuizID = StringField("QuizID (this Quiz has to be in the database): ")
    submit = SubmitField("Start Editing Quiz!")

#For teacher changing/modifying questions
class changeQuestionForm(FlaskForm):
    newQuestion = StringField("Change question to :")
    submit = SubmitField("Save question")

class QuizMarkForm(FlaskForm):
    QuizID = StringField("Quiz ID:")
    submit = SubmitField("Find quiz to be marked!")

class GradingForm(FlaskForm):
    mark = StringField("Mark:")
    comment = TextField("Comment:")
    submit = SubmitField("Save and Proceed to next question")
    


