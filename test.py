import unittest
from app import app, db
from app.models import User, Book
from flask_user import current_user


class BaseTestCase(unittest.TestCase):
    """A base test case."""

    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.add(User(username="admin", password="admin", name="admin"))
        db.session.add(
            Book(title="title", author="author", description="Great read"))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class FlaskTestCase(BaseTestCase):
    # Ensure that Flask was set up correctly
    def test_index(self):
        response = self.client.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_correct_login(self):
        with self.client:
            response = self.client.post(
                '/login',
                data=dict(username="admin", password="admin"),
                follow_redirects=True
            )
            self.assertIn(b'You were logged in', response.data)
            self.assertTrue(current_user.name == "admin")
            self.assertTrue(current_user.is_active())

    def test_incorrect_login(self):
        response = self.client.post(
            '/login',
            data=dict(username="wrong", password="wrong"),
            follow_redirects=True
        )
        self.assertIn(b'Invalid username or password.', response.data)

    # Ensure user can register
    def test_user_registeration(self):
        with self.client:
            response = self.client.post('register/', data=dict(
                username='admin', password='admin'
            ), follow_redirects=True)
            self.assertIn(b'Welcome to Flask!', response.data)
            self.assertTrue(current_user.name == "admin")
            self.assertTrue(current_user.is_active())