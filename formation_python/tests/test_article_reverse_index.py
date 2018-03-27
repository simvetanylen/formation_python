import json
import unittest

from unittest.mock import patch

from app import app
from app.database.database import Database
from tests.utils import content_type
from tests.utils.mock_connection_factory import MockConnectionFactory


class TestArticleReverseIndex(unittest.TestCase):

    @patch.object(Database, 'get_connection', new=MockConnectionFactory.get)
    def test_search(self):
        Database.execute_schema()
        test_app = app.test_client()

        response = test_app.post('/users', data=json.dumps({
            "firstname": "john"
        }), content_type=content_type.JSON)
        assert response.status_code == 200
        user1_id = int(response.data.decode('utf-8'))

        response = test_app.post('/articles', data=json.dumps({
            "title": "article 1",
            "text": "bla bla des phrases, hop bilbo, du bla bla",
            "writer": user1_id
        }), content_type=content_type.JSON)
        assert response.status_code == 200
        article1_id = int(response.data.decode("utf-8"))

        response = test_app.post('/articles', data=json.dumps({
            "title": "article 2",
            "text": "bla bla des phrases, hop baggins, du bla bla",
            "writer": user1_id
        }), content_type=content_type.JSON)
        assert response.status_code == 200
        article2_id = int(response.data.decode("utf-8"))

        response = test_app.post('/articles', data=json.dumps({
            "title": "article 3",
            "text": "bilbo",
            "writer": user1_id
        }), content_type=content_type.JSON)
        assert response.status_code == 200
        article3_id = int(response.data.decode("utf-8"))

        response = test_app.get('/articles/search/bilbo')
        assert response.status_code == 200
        search_results = json.loads(response.data)

        assert len(search_results) == 2
        assert article1_id in [result['id'] for result in search_results]
        assert not article2_id in [result['id'] for result in search_results]
        assert article3_id in [result['id'] for result in search_results]
