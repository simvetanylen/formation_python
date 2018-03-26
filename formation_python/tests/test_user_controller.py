import unittest
import json
from unittest.mock import patch

from app import app
from app.database.database import Database
from tests.utils.mock_connection_factory import MockConnectionFactory


class TestUserController(unittest.TestCase):

    @patch.object(Database, 'get_connection', new=MockConnectionFactory.get)
    def test(self):
        Database.execute_schema()

        test_app = app.test_client()

        response = test_app.get("/users")

        users = json.loads(response.data)

        assert len(users) == 0
