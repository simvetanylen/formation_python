from app.database.database import Database


class ArticleDao:

    @staticmethod
    def create(model):
        return Database.create("""
        INSERT INTO article(title, text, time, writer)
        VALUES (?, ?, ?, ?)
        """, [model['title'], model['text'], model['time'], model['writer']])
