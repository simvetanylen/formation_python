import unittest
import json
from unittest.mock import patch

from app import app
from app.dao.article_dao import ArticleDao
from app.database.database import Database
from tests.utils import content_type
from tests.utils.date_format import DATE_FORMAT
from tests.utils.mock_connection_factory import MockConnectionFactory

from datetime import datetime


class TestArticleController(unittest.TestCase):

    @patch.object(Database, 'get_connection', new=MockConnectionFactory.get)
    def test_create(self):
        Database.execute_schema()
        test_app = app.test_client()

        time_before = datetime.now()
        response = test_app.post('/articles', data=json.dumps({
            "title": "Titre",
            "text": "text",
            "writer": "moi"
        }), content_type=content_type.JSON)
        time_after = datetime.now()
        assert response.status_code == 200

        article_id = response.data.decode('utf-8')
        article = ArticleDao.get(article_id)
        time = datetime.strptime(article['time'], DATE_FORMAT)
        assert article['title'] == 'Titre' and article['text'] == 'text' and article['writer'] == 'moi' \
               and time_before < time < time_after
