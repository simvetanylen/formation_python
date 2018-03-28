from datetime import datetime
from app.dao.message_dao import MessageDao


class MessageService:
    @staticmethod
    def get_all_inbox(user_id):
        return MessageDao.get_inbox(user_id)

    @staticmethod
    def get_all_outbox(user_id):
        return MessageDao.get_outbox(user_id)

    @staticmethod
    def create(model):
        model['time'] = datetime.now()
        return MessageDao.create(model)
