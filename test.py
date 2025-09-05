import unittest
from main import app


class AddTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        app.testing = True

    def test_add_success(self):
        response = self.client.post('/addition', data={'a': '2.5', 'b': '3.5'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'result': 6.0})

    def test_add_invalid_input(self):
        response = self.client.post('/addition', data={'a': 'abc', 'b': '1'})
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.get_json())

    def test_add_missing_param(self):
        response = self.client.post('/addition', data={'a': '5'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'result': 5.0})


if __name__ == '__main__':
    unittest.main()
