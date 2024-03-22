import pytest
from flask_testing import TestCase
from cars import app 

class MyTest(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_home(self):
        response = self.client.get("/models")
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    pytest.main()
