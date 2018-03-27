from datetime import datetime

import re

from app.dao.article_dao import ArticleDao
from app.dao.article_reverse_index_dao import ArticleReverseIndexDao


class ArticleService:

    @staticmethod
    def create(model):
        now = datetime.now()
        model['time'] = now
        article_id = ArticleDao.create(model)

        words = re.findall(r"[\w']+", model['text'])

        for word in words:
            ari_model = {
                "article_id": article_id,
                "word": word
            }

            if not ArticleReverseIndexDao.exists(ari_model):
                ArticleReverseIndexDao.create(ari_model)

        return article_id

    @staticmethod
    def search(word):
        search_results = ArticleReverseIndexDao.search(word)

        articles = []
        for article_id in [search_result['article_id'] for search_result in search_results]:
            articles.append(ArticleDao.get(article_id))

        return articles

