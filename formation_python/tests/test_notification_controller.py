import unittest
import json
from unittest.mock import patch

from app import app
from app.database.database import Database
from app.dao.user_dao import UserDao
from tests.utils import content_type
from tests.utils.mock_connection_factory import MockConnectionFactory


class TestNotificationController(unittest.TestCase):
    @patch.object(Database, 'get_connection', new=MockConnectionFactory.get)
    def test_create(self):
        Database.execute_schema()
        test_app = app.test_client()

        user_id = UserDao.create({'firstname': 'toto'})
        assert user_id > 0

        response = test_app.post('/users/' + str(user_id) + '/notifications', data=json.dumps({
            "text": "test"
        }), content_type=content_type.JSON)
        assert response.status_code == 200
        notifications_id = json.loads(response.data)
        response = test_app.get('/users/' + str(user_id) + '/notifications')
        assert response.status_code == 200
        notification = json.loads(response.data)
        assert notification[0]['id'] == notifications_id
        assert notification[0]['to_user'] == user_id
        assert notification[0]['text'] == 'test'

