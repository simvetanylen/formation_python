import os

from app.database.connection_factory import ConnectionFactory


class Database:
    __schema_file = os.path.join(os.path.dirname(__file__), 'schema.sql')

    @classmethod
    def read(cls, request, params):
        connection = cls.get_connection()
        cursor = connection.execute(request, params)
        result = cursor.fetchall()
        return result

    @classmethod
    def create(cls, request, params):
        connection = cls.get_connection()
        cursor = connection.cursor()
        cursor.execute(request, params)
        rowid = cursor.lastrowid
        connection.commit()
        return rowid

    @classmethod
    def update(cls, request, params):
        connection = cls.get_connection()
        connection.execute(request, params)
        connection.commit()

    @classmethod
    def delete(cls, request, params):
        connection = cls.get_connection()
        connection.execute(request, params)
        connection.commit()

    @classmethod
    def get_connection(cls):
        return ConnectionFactory.get()

    @classmethod
    def execute_schema(cls):
        connection = cls.get_connection()
        with open(cls.__schema_file, mode='r') as schema:
            connection.cursor().executescript(schema.read())
        connection.commit()
