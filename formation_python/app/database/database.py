import sqlite3

import os


class Database:
    __db_file = os.path.join(os.path.dirname(__file__), 'sqlite.db')
    __schema_file = os.path.join(os.path.dirname(__file__), 'schema.sql')
    __schema_created = False

    @classmethod
    def read(cls, request, params):
        connection = cls.__get_connection()
        cursor = connection.execute(request, params)
        result = cursor.fetchall()
        connection.close()
        return result

    @classmethod
    def create(cls, request, params):
        connection = cls.__get_connection()
        cursor = connection.cursor()
        cursor.execute(request, params)
        rowid = cursor.lastrowid
        connection.commit()
        connection.close()
        return rowid

    @classmethod
    def update(cls, request, params):
        connection = cls.__get_connection()
        connection.execute(request, params)
        connection.commit()
        connection.close()

    @classmethod
    def __get_connection(cls):
        connection = sqlite3.connect(Database.__db_file)
        connection.row_factory = cls.__dict_factory
        return connection

    def __dict_factory(cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    @classmethod
    def execute_schema(cls):
        connection = cls.__get_connection()
        with open(cls.__schema_file, mode='r') as schema:
            connection.cursor().executescript(schema.read())
        connection.commit()
        connection.close()
