from datetime import datetime

from app.dao.article_dao import ArticleDao
from app.dao.article_reverse_index_dao import ArticleReverseIndexDao


class ArticleService:

    @staticmethod
    def create(model):
        now = datetime.now()
        model['time'] = now
        article_id = ArticleDao.create(model)

        words = model['text'].split(' ')

        for word in words:
            ari_model = {
                "article_id": article_id,
                "word": word
            }

            if not ArticleReverseIndexDao.exists(ari_model):
                ArticleReverseIndexDao.create(ari_model)

        return article_id
