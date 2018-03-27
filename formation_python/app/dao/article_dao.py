from app.database.database import Database
from app.exceptions.item_not_found_exception import ItemNotFoundException


class ArticleDao:

    @staticmethod
    def get(article_id):
        results = Database.read("""
        SELECT * FROM article
        WHERE id = ?
        """, [article_id])

        if len(results) > 0:
            return results[0]
        else:
            raise ItemNotFoundException()

    @staticmethod
    def create(model):
        return Database.create("""
        INSERT INTO article(title, text, time, writer)
        VALUES (?, ?, ?, ?)
        """, [model['title'], model['text'], model['time'], model['writer']])
