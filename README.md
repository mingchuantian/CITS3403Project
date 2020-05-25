# CITS3403Project

-  22636589  Mingchuan Tian

-  22762872  Ruida He 

-  22797012 Jiayu Wu

-  22541459  Hanlin Zhang

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

## how to use our project (student quiz management)?

1. create the new count at regist to create both teacher(remember to tick the regist as teacher) and student account

2. log in to teacher home page by clicking "teacher log in", insert email and password

3. create a new quiz by clicking the "create new quiz", insert the name of quiz, quizID, time limit. Remember, we can do both multiple choice and essay questions, just write down your question and click "save"

4. after finished, clicking the "finish" button to back to the teacher home page. If you want to edit the quiz, clicking "edit quiz" and insert the quizID to do that

5. now switch to student account by log out teacher account and log in with student account by clicking "student log in"

6. then you can start the quiz by insert your quizID (teacher will give it to students before the quiz start)

7. after finished the quiz, switch to the teacher account to click the "mark quiz", teacher can give the comments and grade for each answers.

8. after teacher mark the grade, now the students can see their grade and ranking in class by clicking "view grade" and "view ranking" on their student home page.

9. it is also able to change the user profile and their log in email by clicking "edit profile" and "change avatar"

