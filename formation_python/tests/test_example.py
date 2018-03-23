import unittest

from app import app


class TestExample(unittest.TestCase):

    def test(self):
        test_app = app.test_client()
        response = test_app.get("/example")

        assert response.status_code == 200

