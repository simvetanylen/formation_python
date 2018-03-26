from app.database.database import Database


class UserDao:

    @staticmethod
    def get_all():
        return Database.read("SELECT * FROM user;", [])

    @staticmethod
    def get(user_id):
        return Database.read("SELECT * FROM user WHERE id = ?", user_id)

    @staticmethod
    def create(model):
        return Database.create("""
        INSERT INTO user(firstname, lastname)
        VALUES (?, ?);
        """, [model['firstname'], model['lastname']])

    @staticmethod
    def update(user_id, model):
        Database.update("""
        UPDATE user SET firstname = ?, lastname = ?
        WHERE id = ?
        """, [model['firstname'], model['lastname'], user_id])

    @staticmethod
    def delete(user_id):
        Database.delete("""
        DELETE FROM user WHERE id = ?
        """, [user_id])