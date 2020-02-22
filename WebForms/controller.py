from .db import DB_Connection


class Controller:
    def __init__(self):
        self.db = DB_Connection()

    def validate_user(self, username, password):
        rmStr = "username = %s AND password = %s"
        params = (username, password)
        print(rmStr)
        res = self.db.query("ID", "user", rmStr, params)
        return res

    def store_user(self, name, username, password):
        self.db.insert("INSERT INTO user VALUES (%s, %s, %s)" % (name, username, password))


