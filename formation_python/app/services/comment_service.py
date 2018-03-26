from datetime import datetime

from app.dao.comment_dao import CommentDao


class CommentService:

    @staticmethod
    def create(model):
        now = datetime.now()
        model['time'] = now
        return CommentDao.create(model)