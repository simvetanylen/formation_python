from datetime import datetime

from app.dao.article_dao import ArticleDao


class ArticleService:

    @staticmethod
    def create(model):
        now = datetime.now()
        model['time'] = now
        return ArticleDao.create(model)