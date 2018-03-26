from app.database.database import Database


class CommentDao:

    @staticmethod
    def create(model):
        return Database.create("""
        INSERT INTO comment(text, time, writer)
        VALUES (?, ?, ?)
        """, [model['text'], model['time'], model['writer']])