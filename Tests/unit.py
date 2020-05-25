import unittest
from app import app, db
from app.models import User, Question, QuizSet, Answer, Grade


# Unit test does testing on models (database)
# checks functions (eg. set_password() for User)
# and see if all attributes have intended values
# (It should be 100% coverage on all models & attributes)

class UserModelTest(unittest.TestCase):

    # setUp will run before running any testing functions
    # it creates a virtual environment & make sure databse is empty
    def setUp(self):
        self.app = app.test_client()
        db.drop_all()
        db.create_all()
        u = User(name='Ming', email='mingchuantian@gmail.com',  faculty="Science", title="Mr.", phone = "499382201", address="311 road")
        u.avatar_hash = u.gravatar_hash()
        db.session.add(u)
        db.session.commit()

    def tearDown(self):
        db.session.remove()

    def test_set_pw(self):  
        u = User.query.get(1)
        u.set_password('pw')
        self.assertFalse(u.verify_password('passw0rd'))
        self.assertTrue(u.verify_password('pw'))

    def test_repr_(self):
        u = User.query.get(1)
        self.assertTrue(str(u) == ('<User>'+u.name))

    def test_values(self):
        u = User.query.get(1)
        self.assertTrue(u.name == 'Ming')
        self.assertTrue(u.faculty == 'Science')
        self.assertTrue(u.title == 'Mr.')
        self.assertTrue(u.phone == 499382201)
        self.assertTrue(u.address == '311 road')
    

    def test_change_email(self):
        u = User.query.get(1)
        new_email = '1120509786@qq.com'
        u.change_email(new_email)
        self.assertTrue(u.email == new_email)


class QuestionModelTest(unittest.TestCase):

    def setUp(self):
        #creates an virtual environment
        self.app = app.test_client()
        #make sure database is empty
        db.drop_all()
        db.create_all()
        q = Question(Question='Who are you', quizset_id=1)
        db.session.add(q)
        db.session.commit()

    def tearDown(self):
        db.session.remove()

    def test_repr_(self):
        q = Question.query.get(1)
        self.assertTrue(str(q) == (q.Question))

    def test_values(self):
        q = Question.query.get(1)
        self.assertTrue(q.Question == 'Who are you')
        self.assertTrue(q.quizset_id == 1)



class QuizSetModelTest(unittest.TestCase):

    def setUp(self):
        #creates an virtual environment
        self.app = app.test_client()
        #make sure database is empty
        db.drop_all()
        db.create_all()
        qs = QuizSet(title='quizset 1', quiz_id= '000', question_num=1)
        db.session.add(qs)
        db.session.commit()

    def tearDown(self):
        db.session.remove()

    def test_repr_(self):
        qs = QuizSet.query.get(1)
        self.assertTrue(str(qs) == (str(qs.id)))
    

    def test_values(self):
        qs = QuizSet.query.get(1)
        self.assertTrue(qs.title == 'quizset 1')
        self.assertTrue(qs.quiz_id == '000')
        self.assertTrue(qs.question_num == 1)

class AnswerModelTest(unittest.TestCase):

    def setUp(self):
        #creates an virtual environment
        self.app = app.test_client()
        #make sure database is empty
        db.drop_all()
        db.create_all()
        a = Answer(Answer='This is my answer', marked = False)
        db.session.add(a)
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()

    def test_repr_(self):
        a = Answer.query.get(1)
        self.assertTrue(str(a) == str(a.student_id) + ',' + str(a.id) + ',' + str(a.Answer) +  ',' + str(a.quizset_id))
    
    def test_values(self):
        a = Answer.query.get(1)
        self.assertTrue(a.Answer == 'This is my answer')

    def test_marked(self):
        a =Answer.query.get(1)
        self.assertTrue(a.marked == False)
        a.mark()
        self.assertTrue(a.marked == True)

class GradeModelTest(unittest.TestCase):

    def setUp(self):
        #creates an virtual environment
        self.app = app.test_client()
        #make sure database is empty
        db.drop_all()
        db.create_all()
        g = Grade(mark=100, comment = 'You did great')
        db.session.add(g)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
    
    def test_repr_(self):
        g = Grade.query.get(1)
        self.assertTrue(str(g) == str(g.answer_id) + ',' + str(g.mark) + ',' + str(g.comment))
   
    def test_values(self):
        g = Grade.query.get(1)
        self.assertTrue(g.mark == 100)
        self.assertTrue(g.comment == 'You did great')


if __name__=='__main__':
  unittest.main(verbosity=2)