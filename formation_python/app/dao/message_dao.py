from app.database.database import Database


class MessageDao:

    @staticmethod
    def create(model):
        return Database.create("""
        INSERT INTO message(from_user, to_user, text, time)
        VALUES (?, ?, ?, ?);
        """, [model['from_user'], model['to_user'], model['text'], model['time']])

    @staticmethod
    def get_inbox(user_id):
        return Database.read("""
        SELECT * FROM message WHERE to_user = ?
        """, [user_id])

    @staticmethod
    def get_outbox(user_id):
        return Database.read("""
        SELECT * FROM message WHERE from_user = ?
        """, [user_id])