import unittest
from unittest.mock import patch

from flask import json

from app import app
from app.database.database import Database
from tests.utils import content_type
from tests.utils.mock_connection_factory import MockConnectionFactory


class TestArticleController(unittest.TestCase):

    @patch.object(Database, 'get_connection', new=MockConnectionFactory.get)
    def test_create(self):
        Database.execute_schema()
        test_app = app.test_client()

        response = test_app.post('/users', data=json.dumps({
            "firstname": "user1",
            "lastname": "user1",
        }), content_type=content_type.JSON)
        assert response.status_code == 200
        user1_id = int(response.data.decode("utf-8"))

        response = test_app.post('/articles', data=json.dumps({
            "title": "mon article",
            "text": "blabla",
            "writer" : user1_id
        }), content_type=content_type.JSON)
        assert response.status_code == 200
