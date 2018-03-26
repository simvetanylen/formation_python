import unittest
from unittest.mock import patch
from flask import json

from app import app
from app.constants import message_types
from app.database.database import Database
from tests.utils import content_type
from tests.utils.mock_connection_factory import MockConnectionFactory


class TestCommentController(unittest.TestCase):

    @patch.object(Database, 'get_connection', new=MockConnectionFactory.get)
    def test_create(self):
        Database.execute_schema()
        test_app = app.test_client()

        response = test_app.post('/users', data=json.dumps({
            "firstname": "user",
        }), content_type=content_type.JSON)
        assert response.status_code == 200
        user1_id = int(response.data.decode('utf-8'))

        response = test_app.post('/articles', data=json.dumps({
            "title": "mon article",
            "text": "blabla",
            "writer": user1_id
        }), content_type=content_type.JSON)
        assert response.status_code == 200
        article1_id = int(response.data.decode('utf-8'))

        response = test_app.post('/articles/' + str(article1_id) + '/comments', data=json.dumps({
            "text": "blabla",
            "writer": user1_id
        }), content_type=content_type.JSON)
        assert response.status_code == 200

    @patch.object(Database, 'get_connection', new=MockConnectionFactory.get)
    def test_comment_notification(self):
        Database.execute_schema()
        test_app = app.test_client()

        response = test_app.post('/users', data=json.dumps({
            "firstname": "user1",
            "lastname": "user1"
        }), content_type=content_type.JSON)
        assert response.status_code == 200
        user1_id = int(response.data.decode('utf-8'))

        response = test_app.post('/users', data=json.dumps({
            "firstname": "user1",
            "lastname": "user1"
        }), content_type=content_type.JSON)
        assert response.status_code == 200
        user2_id = int(response.data.decode('utf-8'))

        response = test_app.post('/articles', data=json.dumps({
            "title": "mon article",
            "text": "blabla",
            "writer": user1_id
        }), content_type=content_type.JSON)
        assert response.status_code == 200
        article1_id = int(response.data.decode('utf-8'))

        response = test_app.post('/articles/' + str(article1_id) + '/comments', data=json.dumps({
            "text": "blabla",
            "writer": user2_id
        }), content_type=content_type.JSON)
        assert response.status_code == 200

        response = test_app.get('/users/' + str(user1_id) + '/inbox')
        assert response.status_code == 200
        messages = json.loads(response.data)
        assert len(messages) == 1
        assert messages[0]['type'] == message_types.NOTIFICATION