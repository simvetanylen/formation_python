import re

from app.dao.user_dao import UserDao
from app.exceptions.invalid_model_exception import InvalidModelException


class UserService:

    @staticmethod
    def get_all():
        return UserDao.get_all()

    @staticmethod
    def get(user_id):
        return UserDao.get(user_id)

    @staticmethod
    def create(model):
        if re.match(r'^[A-Za-z ]+$', model['firstname']):
            return UserDao.create(model)
        else:
            raise InvalidModelException()

    @staticmethod
    def update(user_id, model):
        UserDao.update(user_id, model)

    @staticmethod
    def delete(user_id):
        UserDao.delete(user_id)
