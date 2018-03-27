import sqlite3

from app.database.custom_row_factory import custom_row_factory


class MockConnectionFactory:
    __fake_connection = None

    @classmethod
    def get(cls):
        if cls.__fake_connection is None:
            cls.__fake_connection = sqlite3.connect(":memory:")
            cls.__fake_connection.row_factory = custom_row_factory
        return cls.__fake_connection
