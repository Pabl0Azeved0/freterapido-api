import requests
import unittest
from unittest import mock

from app import app as my_web_app


class TestHome(unittest.TestCase):

    def setUp(self) -> None:
        app = my_web_app.test_client()
        self.response = app.get('/')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_content_type(self):
        self.assertIn('text/html', self.response.content_type)

    def test_content(self):
        response_str = self.response.data.decode('utf-8')
        self.assertIn('<p style=', str(response_str))
        self.assertIn('<input type="', str(response_str))
        self.assertIn('<button type=', str(response_str))
        self.assertIn('<h1 style=', str(response_str))

    def test_bootstrap_css(self):
        response_str = self.response.data.decode('utf-8')
        self.assertIn('bootstrap.css', response_str)

    def test_split(self):
        string = 'test string'
        self.assertEqual(string.split(), ['test', 'string'])
        # check if string.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            string.split(2)

    def test_startswith(self):
        self.assertTrue('#test'.startswith('#'))
        self.assertFalse('test'.startswith('#'))

    def test_format(self):
        test = 'test'
        self.assertEqual('name: test', f'name: {test}')


class MyGreatClass:
    def fetch_json(self, url):
        response = requests.get(url)
        return response.json()


# This method will be used by the mock to replace requests.get
def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == 'http://someurl.com/test.json':
        return MockResponse({"key1": "value1"}, 200)
    elif args[0] == 'http://someotherurl.com/anothertest.json':
        return MockResponse({"key2": "value2"}, 200)

    return MockResponse(None, 404)


class MyGreatClassTestCase(unittest.TestCase):

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_fetch(self, mock_get):
        # Assert requests.get calls
        mgc = MyGreatClass()
        json_data = mgc.fetch_json('http://someurl.com/test.json')
        self.assertEqual(json_data, {"key1": "value1"})
        json_data = mgc.fetch_json('http://someotherurl.com/anothertest.json')
        self.assertEqual(json_data, {"key2": "value2"})
        json_data = mgc.fetch_json('http://nonexistenturl.com/cantfindme.json')
        self.assertIsNone(json_data)

        self.assertIn(mock.call('http://someurl.com/test.json'),
                      mock_get.call_args_list)
        self.assertIn(mock.call('http://someotherurl.com/anothertest.json'),
                      mock_get.call_args_list)

        self.assertEqual(len(mock_get.call_args_list), 3)


if __name__ == '__main__':
    unittest.main()
