from datetime import datetime

from app.dao.article_dao import ArticleDao
from app.dao.comment_dao import CommentDao
from app.dao.notification_dao import NotificationDao


class CommentService:

    @staticmethod
    def create(article_id, model):
        now = datetime.now()
        model['time'] = now
        model['article_id'] = article_id
        comment_id = CommentDao.create(model)

        article = ArticleDao.get(article_id)
        NotificationDao.create({
            "to_user": article['writer'],
            "text": "Nouveau commentaire sur l'article " + article['title'],
            "time": datetime.now()
        })

        return comment_id
