from datetime import datetime

from app.dao.notification_dao import NotificationDao


class NotificationService:

    @staticmethod
    def create(user_id, model):
        now = datetime.now()
        model['time'] = now
        model['to_user'] = user_id
        return NotificationDao.create(model)
