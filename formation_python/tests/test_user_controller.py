import sqlite3
import unittest
import json
from unittest.mock import patch

from app import app
from app.database.database import Database


class TestUserController(unittest.TestCase):

    @staticmethod
    def fake_connect():
        connection = sqlite3.connect(":memory:")
        connection.row_factory = Database.dict_factory()
        return connection

    def test(self):
        db_connection_patcher = patch('app.database.database.Database.__get_connection', self.fake_connect)
        db_connection_patcher.start()

        test_app = app.test_client()

        response = test_app.get("/users")

        users = json.loads(response.data)

        assert len(users) == 0

        db_connection_patcher.stop()
