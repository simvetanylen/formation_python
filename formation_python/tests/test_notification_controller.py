import json
import unittest

from unittest.mock import patch

from app import app
from app.database.database import Database
from tests.utils import content_type
from tests.utils.mock_connection_factory import MockConnectionFactory


class TestNotificationController(unittest.TestCase):

    @patch.object(Database, 'get_connection', new=MockConnectionFactory.get)
    def test_create(self):
        Database.execute_schema()
        test_app = app.test_client()

        response = test_app.post('/users', data=json.dumps({
            "firstname": "user1",
            "lastname": "user1",
        }), content_type=content_type.JSON)
        assert response.status_code == 200
        user1_id = response.data.decode("utf-8")

        response = test_app.post('/users/' + user1_id + '/notifications', data=json.dumps({
            "text" : "hello"
        }))
        assert response.status_code == 200

        response = test_app.get('/users/' + user1_id + '/inbox')
        assert response.status_code == 200

        messages = json.loads(response.data)
        assert len(messages) == 1
