from unicodedata import name
from flask import url_for
from flask_testing import TestCase
from Project import app, db
from Project.models import Students, Classes, Enrollment

class TestBase(TestCase):
    def create_app(self): # Sets test configuration
        app.config.update(
            SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db',
            SECRET_KEY = "test secret key",
            DEBUG = True,
            WTF_CSRF_ENABLED = False
        )

        return app
    
    def setUp(self): # Run before each test
        db.create_all()
        sample_stud = Students(first_name = "John", surname = "Doe", house_num = 72, postcode = "SW1A 1AA")
        sample_class = Classes(c_name = "Sample Class", c_desc = "A sample class")
        sample_enroll = Enrollment(fk_student = 1, fk_class = 1)

        db.session.add(sample_stud)
        db.session.add(sample_class)
        db.session.add(sample_enroll)
        db.session.commit()
    
    def tearDown(self): # Run after each test
        db.session.remove()
        db.drop_all()

class TestHome(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assert200(response)
        self.assertIn(b'Sample Class', response.data)

class TestEnroll(TestBase):
    def test_Enroll_get(self):
        response = self.client.get(url_for('enrollment_page'))
        self.assert200(response)
        self.assertIn(b'1', response.data)

class TestAddStud(TestBase):
    def test_create_get(self):
        response = self.client.get(url_for('create_stud'))
        self.assert200(response)
        self.assertIn(b'Student First Name', response.data)

    def test_create_post(self):
        response = self.client.post(
            url_for('create_stud'),
            data = dict(first_name = "Jon", surname = "Do", house_num = 71, postcode = "SW1A 1AB"),
            follow_redirects = True
        )
        self.assert200(response)
        self.assertIn(b'Jon', response.data)

class TestUpdateStud(TestBase):
    def test_create_get(self):
        response = self.client.get(url_for('update_stud', pk=1))
        self.assert200(response)
        self.assertIn(b'Student First Name', response.data)

    def test_create_post(self):
        response = self.client.post(
            url_for('update_stud', pk=1),
            data = dict(first_name = "Jane", surname = "Doe", house_num = 73, postcode = "SW1A 1AC"),
            follow_redirects = True
        )
        self.assert200(response)
        self.assertIn(b'Jane', response.data)

class TestAddClass(TestBase):
    def test_create_get(self):
        response = self.client.get(url_for('create_class'))
        self.assert200(response)
        self.assertIn(b'Class Name', response.data)
    
    def test_create_post(self):
        response = self.client.post(
            url_for('create_class'),
            data = dict(c_name = "Sample Class 2", c_desc = "A Second sample class"),
            follow_redirects = True
        )
        self.assert200(response)
        self.assertIn(b'Sample Class 2', response.data)

class TestUpdateClass(TestBase):
    def test_create_get(self):
        response = self.client.get(url_for('update_class_', pk=1))
        self.assert200(response)
        self.assertIn(b'Class Name', response.data)

    def test_create_post(self):
        response = self.client.post(
            url_for('update_class_', pk=1),
            data = dict(c_name = "Sample Class 3", c_desc = "A Second Third class"),
            follow_redirects = True
        )
        self.assert200(response)
        self.assertIn(b'Sample Class 3', response.data)

class TestAddEnroll(TestBase):
    def test_create_get(self):
        response = self.client.get(url_for('create_enroll'))
        self.assert200(response)
        self.assertIn(b'Student Name', response.data)

    def test_create_post(self):
        response = self.client.post(
            url_for('create_enroll'),
            data = dict(fk_student = 2, fk_class = 2),
            follow_redirects = True
        )
        self.assert200(response)
        self.assertIn(b'2', response.data)   

    def test_enrollment(self):
        assert(str(Enrollment.query.get(1)) == "1, is enrolled in 1")
    
class TestUpdateEnroll(TestBase):    
    def test_create_get(self):
        response = self.client.get(url_for('update_enroll', pk=1))
        self.assert200(response)
        self.assertIn(b'Student Name', response.data)

    def test_create_post(self):
        response = self.client.post(
            url_for('update_class_', pk=1),
            data = dict(fk_student = 3, fk_class = 3),
            follow_redirects = True
        )
        self.assert200(response)
        self.assertIn(b'3', response.data)

class TestDeleteStud(TestBase):
    def test_create_get(self):
        response = self.client.get(url_for('del_stud', pk=1), follow_redirects = True )
        self.assert200(response)
        self.assertNotIn(b'Student First Name', response.data)


class TestDeleteClass(TestBase):
    def test_create_get(self):
        response = self.client.get(url_for('del_class', pk=1),follow_redirects = True)
        self.assert200(response)
        self.assertNotIn(b'Class Name', response.data)


class TestDeleteEnroll(TestBase):
    def test_create_get(self):
        response = self.client.get(url_for('del_enroll', pk=1), follow_redirects = True)
        self.assert200(response)
        self.assertNotIn(b'Student Name', response.data)

class TestValClass(TestBase):
    def test_create_post(self):
        response = self.client.post(
            url_for('create_class'),
            data = dict(c_name = "Sample Class", c_desc = "A sample class"),
            follow_redirects = True
        )
        self.assert200(response)
        self.assertIn(b'Class already exists', response.data)