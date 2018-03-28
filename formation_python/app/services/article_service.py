from app.dao.article_dao import ArticleDao

import datetime


class ArticleService:

    @staticmethod
    def create(model):
        model['time'] = datetime.datetime.now()
        return ArticleDao.create(model)
