import os
import sqlite3

from app.database.custom_row_factory import custom_row_factory


class ConnectionFactory:
    __db_file = os.path.join(os.path.dirname(__file__), 'sqlite.db')

    @classmethod
    def get(cls):
        connection = sqlite3.connect(cls.__db_file)
        connection.row_factory = custom_row_factory
        return connection
