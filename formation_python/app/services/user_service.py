from app.dao.user_dao import UserDao


class UserService:
    @staticmethod
    def get_all():
        return UserDao.get_all()

    @staticmethod
    def get(user_id):
        return UserDao.get(user_id)

    @staticmethod
    def create(model):
        return UserDao.create(model)

    @staticmethod
    def update(user_id, model):
        return UserDao.update(user_id, model)
