import unittest
import os
import json
import flask

from api import db,app
from .models import Users

class UserTestCase(unittest.TestCase):
    """This class represents the songs test case"""

    def setUp(self):
        """Stuff to do before every test."""
        self.client = app.test_client()
        self.user = {'email': 'shakira2@gmail.com',
                     'username': 'Shakira',
                     'password': 'Beyonce',
                     }
        self.user1 = {
                     'username': 'Shakira',
                     'password': 'Beyonce',
                     }
        
        # binds the app to the current context
        with app.app_context():
        # Create tables in testdb
            db.create_all()
            

    def tearDown(self):
        """teardown all initialized variables."""
        with app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()

    def test_register(self):
        """Test that user can register."""
        result = self.client.post(
            '/api/register',
            data=self.user)
        self.assertEqual(result.status_code, 201)

    def test_login(self):
        """Test registered user can login."""
        res = self.client.post('/api/register', data=self.user)
        res1 = self.client.post('/api/login', data=self.user1)
        self.assertEqual(res1['message'], "You logged in successfully.")
        self.assertEqual(login_res.status_code, 200)
        self.assertTrue(result['access_token'])