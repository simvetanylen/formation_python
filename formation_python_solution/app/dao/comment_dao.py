from app.database.database import Database


class CommentDao:

    @staticmethod
    def create(model):
        return Database.create("""
        INSERT INTO comment(text, time, writer, article_id)
        VALUES (?, ?, ?, ?)
        """, [model['text'], model['time'], model['writer'], model['article_id']])