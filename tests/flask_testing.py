# help from tutorial: https://www.youtube.com/watch?v=WDh_VQ41kYI&ab_channel=MichaelHerman

from app import app
import unittest

class TestFlask(unittest.TestCase):

    # tests to see if status code is 200 for index
    def test_index(self):
        tester = app.test_client()
        response = tester.get('/index', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # tests to see if data actually loads for index page
    def test_index_loads(self):
        tester = app.test_client()
        response = tester.get('/index', content_type='html/text')
        self.assertTrue(b'store number' in response.data)