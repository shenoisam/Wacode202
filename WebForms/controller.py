from .db import DB_Connection


class Controller:
    def __init__(self):
        #self.db = DB_Connection()
        self.db = 'Hi'

    def validate_user(self, username, password):
        rmStr = "username = %s AND password = %s"
        params = (username, password)
        print(rmStr)
        res = "123456789"#self.db.query("ID", "user", rmStr, params)
        return res

    def store_user(self, name, username, password):
        return True
        #self.db.insert("INSERT INTO user VALUES (%s, %s, %s)" % (name, username, password))


