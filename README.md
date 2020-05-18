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

## Things need to install

pip install flask_sqlalchemy
pip install flask_migrate 
pip install flask_wtf      

## DATABASE MANIPULATION

Enter flask shell:
flask shell

- Drop all tables (in flask shell):
db.drop_all()

- Create all tables (in flask shell):
db.create_all()

## Bug need to fix or some advices

1.  when click the "home" button after log in, will return to the "log in" pagei
(Fixed)
2.  after click the "save" button, the question disappeas and move on to the next question(can not go to previous question or next question)
3.  need to auto mark the quiz (when create the quiz, teacher can select auto mark or not, if "Yes", then need to insert the answer for each question then check the student answer with the correct answer.)
4.  when create the exam, teacher can modify the mark of each question (when mark the exam, if the mark teacher insert is higher than the modify mark, warning)
5.  after click the "log out" button, there is a small button inside of the html page, i am not sure what that is (click it will jump to a error page)
(Fixed)
6.  after login, can not jump to the student or teacher page
7.  after create a new quiz, can not back to the teacher page or view the quiz
8.  when insert a correct email with incorrect password, the html page will warning "the count is not exists", it should be "incorrect password or the count is not exists", then it should have a button to jump back to the login page
9.  the quiz need a timer, when the time is up, then save all question and submit the answer. teacher can see the total time student use to finish the exam. Other hand, when teacher create the exam, it is better if he can modify the length of exam time(2 hours, 10 minutes so on).
10. when mark the answer, it is better if teacher can see the question
11. when mark the exam, if there has two student wait for mark, their answer will mix together. for example, when a and b all wait for mark, the test has 5 questions, then when teacher mark the question, he/she need to mark it as 10 questions, not seperate to two piece (5 and 5 for each). Then back to the student account, student a can see his mark is 10, but there only 5 questions and each questions he get 1 mark, it means a's and b's mark mixed together, then see b's mark, his is correct, 5 marks.
12. if an user try to answer the qustion agian, why he can still do that? On the other hand, although he is able to do that, then he should has a limit to retake the exam and use the highest mark to be his final mark. when teacher try to mark his grade, it is pretty suprised that he need to mark 15 questions, but we only have 5 questions (mark of b is till error after do this). I totally try three times quiz for a(once) and b(twice), each time is 5 qustions.

maybe can try to use something like array to store the answer in database, then each time retake the exam, the answer array for this student will be rewrite, then get the highest mark of his from his mark array?

or create a database for each student to store their answer?

just some surmise, not pretty sure

13. when i finish all qustion then click the first "save" button to save my answer, the answer for other question will disappear.
