import json
import unittest

from unittest.mock import patch

from datetime import datetime

from app import app
from app.database.database import Database
from tests.utils import content_type, date_format
from tests.utils.mock_connection_factory import MockConnectionFactory


class TestNotificationController(unittest.TestCase):

    @patch.object(Database, 'get_connection', new=MockConnectionFactory.get)
    def test_create(self):
        time_before = datetime.now()

        Database.execute_schema()
        test_app = app.test_client()

        response = test_app.post('/users', data=json.dumps({
            "firstname": "john"
        }), content_type=content_type.JSON)
        assert response.status_code == 200
        user1_id = response.data.decode("utf-8")

        response = test_app.post('/users/' + user1_id + '/notifications', data=json.dumps({
            "text": "hello"
        }), content_type=content_type.JSON)
        assert response.status_code == 200

        response = test_app.get('/users/' + user1_id + '/inbox')
        assert response.status_code == 200

        messages = json.loads(response.data)
        assert len(messages) == 1
        assert messages[0]['type'] == 'NOTIFICATION'
        time = datetime.strptime(messages[0]['time'], date_format.CLASSIC)
        assert time > time_before
        assert time < datetime.now()
