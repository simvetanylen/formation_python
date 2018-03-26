from app.database.database import Database


class NotificationDao:

    @staticmethod
    def create(model):
        return Database.create("""
        INSERT INTO notification(to_user, text, time)
        VALUES (?, ?, ?);
        """, [model['to_user'], model['text'], model['time']])

    @staticmethod
    def get_for_user(user_id):
        return Database.read("""
        SELECT * FROM notification WHERE to_user = ?
        """, [user_id])
