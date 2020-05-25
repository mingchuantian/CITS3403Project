# forms written by: Mingchuan Tian (22636589)

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, TextField, validators
from wtforms.validators import DataRequired, Length
from wtforms.fields.html5 import EmailField


# teacher login form
class TeacherLoginForm(FlaskForm):
    email = EmailField('Email', [validators.DataRequired(), validators.Email()])
    password = PasswordField("Password", validators = [DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")

# student login form
class StudentLoginForm(FlaskForm):
    email = EmailField('Email', [validators.DataRequired(), validators.Email()])
    password = PasswordField("Password", validators = [DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")

# User registration form
class RegisterForm(FlaskForm):
    name = StringField("Name", validators = [DataRequired()])
    email = EmailField('Email', [validators.DataRequired(), validators.Email()])
    password = PasswordField("Password", validators = [DataRequired()])
    teacher = BooleanField("Register as teacher")
    submit = SubmitField("Sign up")


# Quiz specification form (specify details of a quiz)
class QuizStartForm(FlaskForm):
    title = StringField("Quiz Title", validators = [DataRequired()])
    quiz_id = StringField("Give your quiz an ID", validators = [DataRequired()])
    question_num = SelectField("Number of questions", choices=[('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10')])
    time_limit = StringField("Time Limit (minutes)",  validators = [DataRequired()])
    submit = SubmitField("Continue")

# Quiz edit form (for teachers adding questions to the new quiz)
class QuizEditForm(FlaskForm):
    question = StringField("Question: ", validators = [DataRequired()])
    submit = SubmitField("save question")

# Quiz answer form (for students adding answers to existing quiz)
class QuizAnswerForm(FlaskForm):
    answer = StringField("Answer: ", validators = [DataRequired()])
    submit = SubmitField("save answer")

# Quiz login form (for students retrieving quiz)
class QuizLoginForm(FlaskForm):
    QuizID = StringField("QuizID: ")
    submit = SubmitField("Start Quiz!")

# Quiz review form (for teacher retrieving quiz to be changed/modified)
class QuizReviewForm(FlaskForm):
    QuizID = StringField("QuizID (this Quiz has to be in the database): ")
    submit = SubmitField("Start Editing Quiz!")

# Change quiz form (for teacher changing/modifying questions)
class changeQuestionForm(FlaskForm):
    newQuestion = StringField("Change question to :")
    submit = SubmitField("Save question")

# Quiz mark form (for teachers retrieving the quiz to be marked)
class QuizMarkForm(FlaskForm):
    QuizID = StringField("Quiz ID:")
    submit = SubmitField("Find quiz to be marked!")

# Grading form (for teachers grading the quiz)
class GradingForm(FlaskForm):
    mark = StringField("Mark:")
    comment = TextField("Comment:")
    submit = SubmitField("Save and Proceed to next question")
    
# Edit profile form (for users editing their profile)
class EditProfileForm(FlaskForm):
    name = StringField("Name: ", validators = [DataRequired()])
    title = SelectField("Title: ", choices=[('Mr. ', 'Mr.'),('Mrs. ', 'Mrs. '),('Miss. ', 'Miss '),('Dr. ', 'Dr. '),('Prof. ', 'Prof. ')], validators = [DataRequired()])
    faculty = SelectField("Faculty: ", choices=[('Arts, Business, Law and Education','Arts, Business, Law and Education'),('Health and Medical Sciences','Health and Medical Sciences'),('Engineering and Mathematical Sciences','Engineering and Mathematical Sciences'),('Science','Science')], validators = [DataRequired()])
    phone = StringField("Phone: ", validators=[DataRequired(), Length(min=10, max=10)])
    address = TextField("Address: ", validators=[DataRequired()] )

    submit = SubmitField("Save")

# Change avatar form (form users changing their avatars)
class ChangeAvatarForm(FlaskForm):
    email = EmailField('New Email', [validators.DataRequired(), validators.Email()])
    submit = SubmitField("Save")

# forms written by: Mingchuan Tian (22636589)