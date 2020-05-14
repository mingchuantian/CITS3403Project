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


