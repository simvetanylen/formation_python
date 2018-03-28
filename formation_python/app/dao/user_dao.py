from app.database.database import Database
from app.exceptions.item_not_found_exception import ItemNotFoundException


class UserDao:

    @staticmethod
    def get_all():
        return Database.read("SELECT * FROM user;", [])

    @staticmethod
    def get(user_id):
        results = Database.read("SELECT * FROM user WHERE id = ?", [user_id])
        if len(results) > 0:
            return results[0]
        else:
            raise ItemNotFoundException()

    @staticmethod
    def create(model):
        return Database.create("""
        INSERT INTO user(firstname)
        VALUES (?);
        """, [model['firstname']])

#    @staticmethod
#    def update(user_id, model):
#       Database.update("""
#        UPDATE user SET firstname = ?, lastname = ?
#        WHERE id = ?
#        """, [model['firstname'], model['lastname'], user_id])

    @staticmethod
    def update(user_id, model):
        Database.update("""
        UPDATE user SET firstname = ?
        WHERE id = ?
        """, [model['firstname'], user_id])

    @staticmethod
    def delete(user_id):
        Database.delete("""
        DELETE FROM user WHERE id = ?
        """, [user_id])
