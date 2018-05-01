import unittest
import os
import json
import flask

from api import db,app
from .models import Songs

class SongTestCase(unittest.TestCase):
    """This class represents the songs test case"""

    def setUp(self):
        """Stuff to do before every test."""
        # self.app = config_name="testing"
        self.client = app.test_client()
        self.song = {'title': 'Listen',
                     'artist': 'Beyonce'}
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

    def test_add_song(self):
        """Test that user can add songs."""
        result = self.client.post(
            '/api/songs',
            data=self.song)
        self.assertEqual(result.status_code, 201)

    def test_get_songs(self):
        """Test that user can get all songs."""
        result = self.client.post(
            '/api/songs',
            data=self.song)
        result = self.client.get(
            '/api/songs',
            data=self.song)
        self.assertEqual(result.status_code, 200)

    def test_single_song(self):
        """Test that user can get a single song."""
        result = self.client.post(
            '/api/songs',
            data=self.song)
        result = self.client.get(
            '/api/songs/1',
            data=self.song)
        self.assertEqual(result.status_code, 200)

    def test_delete_song(self):
        """Test that user can delete all songs."""
        result = self.client.post(
            '/api/songs/1',
            data=self.song)
        result = self.client.delete(
            '/api/songs/1')
        self.assertEqual(result.status_code, 200)
    
    def test_edit_song(self):
        """Test that user can edit a song."""
        result = self.client.post(
            '/api/songs',
            data=self.song)
        result = self.client.put(
            '/api/songs/1',
            data={'title': 'love you', 'artist': 'Shakira'})
        self.assertEqual(result.status_code, 201)
