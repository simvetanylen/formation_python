import json
import unittest
from unittest.mock import patch

from app import app
from app.constants import message_types
from app.database.database import Database
from tests.utils import content_type
from tests.utils.mock_connection_factory import MockConnectionFactory


class TestInboxController(unittest.TestCase):

    @patch.object(Database, 'get_connection', new=MockConnectionFactory.get)
    def test_date_order(self):
        Database.execute_schema()
        test_app = app.test_client()

        response = test_app.post('/users', data=json.dumps({
            "firstname": "john"
        }), content_type=content_type.JSON)
        assert response.status_code == 200
        user1_id = response.data.decode("utf-8")

        response = test_app.post('/users', data=json.dumps({
            "firstname": "jane"
        }), content_type=content_type.JSON)
        assert response.status_code == 200
        user2_id = response.data.decode("utf-8")

        response = test_app.post('/messages', data=json.dumps({
            "from_user": 1,
            "to_user": 2,
            "text": "..."
        }), content_type=content_type.JSON)
        assert response.status_code == 200
        message1_id = response.data.decode("utf-8")

        response = test_app.post('/users/' + user2_id + '/notifications', data=json.dumps({
            "to_user": 2,
            "text": "..."
        }), content_type=content_type.JSON)
        assert response.status_code == 200
        notification1_id = response.data.decode("utf-8")

        response = test_app.post('/messages', data=json.dumps({
            "from_user" : 1,
            "to_user": 2,
            "text" : "..."
        }), content_type=content_type.JSON)
        assert response.status_code == 200
        message2_id = response.data.decode("utf-8")

        response = test_app.get('/users/' + user2_id + '/inbox')
        assert response.status_code == 200
        messages = json.loads(response.data)
        assert len(messages) == 3
        assert messages[0]['id'] == int(message1_id) and messages[0]['type'] == message_types.USER
        assert messages[1]['id'] == int(notification1_id) and messages[1]['type'] == message_types.NOTIFICATION
        assert messages[2]['id'] == int(message2_id) and messages[2]['type'] == message_types.USER