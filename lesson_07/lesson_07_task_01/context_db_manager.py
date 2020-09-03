import sqlite3


class DBContextManager:

    def __init__(self, name_db):
        self.name_db = name_db

    def __enter__(self):
        self.conn = sqlite3.connect(self.name_db)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
        if exc_val:
            raise
