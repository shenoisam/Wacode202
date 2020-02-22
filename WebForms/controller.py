from .db import DB_Connection
from Geolocation.image_test import Geolocation
import random
import string


class Controller:
    def __init__(self):
        self.db = DB_Connection()
        self.g = Geolocation()

    def validate_user(self, username, password):
        rmStr = "username = %s AND password = %s"
        params = (username, password)
        print(rmStr)
        res = self.db.query("ID", "user", rmStr, params)
        return res

    def Geolocate(self, image):
        print(image)
        return self.g.run_program(image)

    def store_user(self, name, username, password):
        r = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(0,20)])
        print(name, username, password, r)
        self.db.insert("INSERT INTO user (name, username, password, ID)  VALUES (\'%s\', \'%s\', \'%s\',\'%s\')" % (name, username, password,r))


