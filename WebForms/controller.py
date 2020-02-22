from .db import DB_Connection


class Controller:
    def __init__(self):
        self.db = DB_Connection()

    def validate_user(self,username, password):
        rmStr = "username = %s AND password = PASSWORD(%s)" % (username,password)
        res = self.db.query("ID", "user", rmStr)
        if len(res) == 1:
            res = None
        return res


