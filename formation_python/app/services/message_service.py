from datetime import datetime

from app.constants import message_types
from app.dao.message_dao import MessageDao
from app.dao.notification_dao import NotificationDao
from app.dao.user_dao import UserDao


class MessageService:

    @staticmethod
    def create(model):
        now = datetime.now()
        model['time'] = now
        return MessageDao.create(model)

    @staticmethod
    def get_inbox(user_id):
        messages = MessageDao.get_inbox(user_id)
        model_list = []

        for message in messages:
            model_list.append({
                'text': message['text'],
                'time': message['time'],
                'from': UserDao.get(message['from_user']),
                'type': message_types.USER
            })

        notifications = NotificationDao.get_for_user(user_id)

        for notification in notifications:
            model_list.append({
                'text': notification['text'],
                'time': notification['time'],
                'type': message_types.NOTIFICATION
            })

        return model_list

    @staticmethod
    def get_outbox(user_id):
        messages = MessageDao.get_outbox(user_id)
        model_list = []

        for message in messages:
            model_list.append({
                'text': message['text'],
                'time': message['time'],
                'to': UserDao.get(message['to_user'])
            })
        return model_list
