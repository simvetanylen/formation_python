import unittest
import json

from app import app


class TestUserController(unittest.TestCase):

    def test(self):
       test_app = app.test_client()

       response = test_app.get("/users")

       users = json.loads(response.data)

       assert len(users) == 6