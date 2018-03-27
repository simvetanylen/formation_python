from app.database.database import Database


class ArticleReverseIndexDao:

    @staticmethod
    def exists(model):
        return len(Database.read("""
        SELECT * FROM article_reverse_index
        WHERE article_id = ?
        AND word = ?
        """, [model['article_id'], model['word']])) > 0

    @staticmethod
    def create(model):
        return Database.create("""
        INSERT INTO article_reverse_index(article_id, word)
        VALUES (?, ?)
        """, [model['article_id'], model['word']])

    @staticmethod
    def search(word):
        return Database.read("""
        SELECT * FROM article_reverse_index
        WHERE word = ?
        """, [word])