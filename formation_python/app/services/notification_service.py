from app.dao.notification_dao import NotificationDao


class NotificationService:

    @staticmethod
    def get_all(user_id):
        return NotificationDao.get(user_id)

    @staticmethod
    def create(user_id,model):
        return NotificationDao.create(user_id,model)

