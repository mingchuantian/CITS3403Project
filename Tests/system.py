import unittest, os, time
from app import app, db
from app.models import User
from selenium import webdriver
from selenium.webdriver.support.ui import Select
basedir = os.path.abspath(os.path.dirname(__file__))

class SystemTest(unittest.TestCase):
    driver = None

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=os.path.join(basedir,'geckodriver'))
        if not self.driver:
            self.skipTest
        else:
            db.init_app(app)
            db.drop_all()
            db.create_all()
            u1 = User(name='Ming', email='mingchuantian@gmail.com', faculty="Science", title="Mr.", phone = "499382201", is_teacher=True, address="311 road") 
            u1.set_password('mingchuan')
            db.session.add(u1)
            u2 = User(name='chenshu', email='chenshu730@gmail.com', faculty="Science", title="Mrs.", phone = "499382201", is_teacher=False, address="311 road") 
            u2.set_password('chenshu')
            db.session.add(u2)
            db.session.commit()
            self.driver.maximize_window()
            #self.driver.get('http://localhost:5000/')

    def tearDown(self):
        if self.driver:
            self.driver.close()
            db.session.remove()



    # Test teacher account login & open 'Add quiz' page
    def test_login(self):

        #Login process
        self.driver.get('http://localhost:5000/login')
        time.sleep(1) 
        email_field = self.driver.find_element_by_id('email')
        password_field = self.driver.find_element_by_id('password') 
        submit = self.driver.find_element_by_id('submit')

        email_field.send_keys('mingchuantian@gmail.com')
        password_field.send_keys('mingchuan')
        submit.click()
        time.sleep(1)

        login_identifier = self.driver.find_element_by_id('Logged in successful').get_attribute('innerHTML')
        self.assertEqual(login_identifier, 'The University of Western Australia')

        #Open quiz page
        make_quiz = self.driver.find_element_by_id('makeQuiz')
        make_quiz.click()
        time.sleep(1)
        quiz_identifier = self.driver.find_element_by_id('quizPage')
        self.assertTrue(quiz_identifier)

    #Test teacher account register
    def test_register(self):
        self.driver.get('http://localhost:5000/')
        time.sleep(1)
        name_field = self.driver.find_element_by_id('name')
        email_field = self.driver.find_element_by_id('email')
        password_field = self.driver.find_element_by_id('password')
        is_teacher = self.driver.find_element_by_id('teacher')
        submit = self.driver.find_element_by_id('submit')

        name_field.send_keys('tian')
        email_field.send_keys('1120509786@qq.com')
        password_field.send_keys('Tianmingchuan123')
        is_teacher.click()
        submit.click()
        time.sleep(4)

        signup_identifier = self.driver.find_element_by_id('notif').get_attribute('innerHTML')
        self.assertEqual(signup_identifier, 'The user is successfully registered')
    
    def test_addQuiz(self):
        #Login process
        self.driver.get('http://localhost:5000/login')
        time.sleep(1) 
        email_field = self.driver.find_element_by_id('email')
        password_field = self.driver.find_element_by_id('password') 
        submit = self.driver.find_element_by_id('submit')

        email_field.send_keys('mingchuantian@gmail.com')
        password_field.send_keys('mingchuan')
        submit.click()
        time.sleep(1)

        login_identifier = self.driver.find_element_by_id('Logged in successful').get_attribute('innerHTML')
        self.assertEqual(login_identifier, 'The University of Western Australia')

        #Open quiz page
        make_quiz = self.driver.find_element_by_id('makeQuiz')
        make_quiz.click()
        time.sleep(1)
        quiz_identifier = self.driver.find_element_by_id('quizPage')
        self.assertTrue(quiz_identifier)

        #add quiz
        title = self.driver.find_element_by_id('title')
        quizID =self.driver.find_element_by_id('quiz_id')
        question_num = Select(self.driver.find_element_by_id('question_num'))
        submit = self.driver.find_element_by_id('submit')
        title.send_keys('This is test quiz')
        quizID.send_keys('111')
        question_num.select_by_value('1')
        submit.click()
        time.sleep(1)

        

    
    def test_answerQuiz(self):
        #Login process
        self.driver.get('http://localhost:5000/login')
        time.sleep(1) 
        email_field = self.driver.find_element_by_id('email')
        password_field = self.driver.find_element_by_id('password') 
        submit = self.driver.find_element_by_id('submit')

        email_field.send_keys('chenshu730@gmail.com')
        password_field.send_keys('chenshu')
        submit.click()
        time.sleep(2)
        login_identifier = self.driver.find_element_by_id('Logged in successful').get_attribute('innerHTML')
        self.assertEqual(login_identifier, 'The University of Western Australia')

        #Open Answer Quiz page
        quizID_field = self.driver.find_element_by_id('QuizID')
        submit = self.driver.find_element_by_id('submit')
        quizID_field.send_keys('111')
        submit.click()
        time.sleep(3)

    
 #   def test_addQuiz(self):
#        self.driver.get('http://localhost:5000/login')





if __name__=='__main__':
  unittest.main(verbosity=2)
    