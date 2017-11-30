from app import app
import unittest

class TestFlask(unittest.TestCase):

    def test_index(self):
        tester = app.test_client()
        response = tester.get('/index', content_type='html/text')
        self.assertEqual(response.status_code, 200)