import unittest
import json
from unittest.mock import patch

from app import app
from app.database.database import Database
from tests.utils import content_type
from tests.utils.mock_connection_factory import MockConnectionFactory


class TestUserController(unittest.TestCase):

    @patch.object(Database, 'get_connection', new=MockConnectionFactory.get)
    def test(self):
        Database.execute_schema()
        test_app = app.test_client()

        response = test_app.get('/users')
        assert response.status_code == 200
        users = json.loads(response.data)
        assert len(users) == 0

    @patch.object(Database, 'get_connection', new=MockConnectionFactory.get)
    def test_create(self):
        Database.execute_schema()
        test_app = app.test_client()

        response = test_app.post('/users', data=json.dumps({
            "firstname": "test",
            "lastname": "test"
        }), content_type=content_type.JSON)
        assert response.status_code == 200

        response = test_app.get('/users')
        assert response.status_code == 200
        users = json.loads(response.data)
        assert len(users) == 1

    @patch.object(Database, 'get_connection', new=MockConnectionFactory.get)
    def test_delete(self):
        Database.execute_schema()
        test_app = app.test_client()

        response = test_app.post('/users', data=json.dumps({
            "firstname": "test",
            "lastname": "test"
        }), content_type=content_type.JSON)
        assert response.status_code == 200
        user_id = response.data.decode("utf-8")

        response = test_app.delete('/users/' + user_id)
        assert response.status_code == 200

        response = test_app.get('/users')
        assert response.status_code == 200
        assert len(json.loads(response.data)) == 0
