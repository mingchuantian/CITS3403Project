# CITS3403Project

-  22636589  Mingchuan Tian

-  22541459  Hanlin Zhang 

-  22762872  Ruida He 

-  22797012 Jiayu Wu (very insufficient contribution)


## Project description

The system is called CITS3403 Quiz Management System, or QMS for short. 
QMS is an interactive Quiz system that allows teachers to set up quizzes and create questions for their students.
Students have to enter a quiz ID (created by teacher and given by teacher when the quiz starts) to enter the quiz. 
Once students have finished the quiz, teachers can view, grade, and comment on the answers. 
Teachers can also modify/change questions when needed. 
Students will get feedback and ranking once their teacher has finished grading. 


## HOW TO RUN THIS APPLICATION

1. Enter virtual environment:
source /venv/bin/activate

2. Set up running application & enable debug mode:
export FLASK_RUN=run.py
export FLASK_DEBUG=TRUE

3. Run the flask:
flask run

## Things need to install

all in the requirements.txt, use the command below,

pip install -r requirements.txt

## DATABASE MANIPULATION

Enter flask shell:
flask shell

- Drop all tables (in flask shell):
db.drop_all()

- Create all tables (in flask shell):
db.create_all()

## How to use the APP ?

# For teachers:

1. Create an account by clicking "register" and fill up the form. 

2. Log in via "Teacher Login", type in your username & password.

3. Add a quiz by clicking on "New Quiz", then specify your quiz details and questions.

4. Modify questions by clicking on "Edit Quiz". 

5. Check how many students have finished the quiz, click "check quiz progress"

6. Once students have finished the quiz, click "Mark Quiz" to mark and give feedbacks.

* You can also complete your profile and change avatar in your profile page. 

# For students:

1. Create an account by clicking "register" and fill up the form. 

2. Log in via "Student Login", type in your username & password. 

3. Get the quiz id from your teacher. Click "Start quiz" to start your quiz. 

4. Once your teacher has finished grading, you can check your grade and ranking

* You can also complete your profile and change avatar in your profile page. 

## How to contribute to this project? (for developers)

Everyone can contribute to the project. I've made it public after the project due date. 
You can visit and clone the git repository via https://github.com/mingchuantian/CITS3403Project

This APP is written in python, Javascript, HTML, and CSS, using flask web app structure. 
The APP is designed inspired by the MVC structure (Model, View, Controller). 

For now, there is one API that retrieves quiz progress information (How many students have finished the quiz) if you're logged in as teacher.
Getting the API via http://localhost:5000/API (if you're running on localhost)

If there's any further questions regarding project detail, please email me mingchuantian1@gmail.com.