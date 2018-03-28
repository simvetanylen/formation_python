import time
from app.constants.date_format import DateFormat

from app.dao.notification_dao import NotificationDao


class NotificationService:

    @staticmethod
    def get_for_user(user_id):
        return NotificationDao.get_for_user(user_id)

    @staticmethod
    def create(user_id,model):
        model['to_user']=user_id
        model['time']=time.strftime(DateFormat.ISO)
        return NotificationDao.create(model)

