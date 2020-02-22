# This class defines the database object in the database

# Import modules
from errno import errorcode
import mysql.connector
from secrets import DB_USER
from secrets import DB_PASSWORD
from secrets import DATABASE
from secrets import DB_HOST


class DB_Connection:
    def __init__(self):
        try:
            self.cnx = mysql.connector.connect(user=DB_USER, password=DB_PASSWORD,
                                               host=DB_HOST,
                                               database=DATABASE,
                                               auth_plugin='mysql_native_password')
            self.cursor = self.cnx.cursor(buffered=True)
        except mysql.connector.Error as err:
            print(err)
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def insert(self, query):
        self.cursor.execute(query)

    def query(self, select, table, rmStr, params):
        query = "SELECT %s FROM %s WHERE %s" % (select, table, rmStr)
        self.cursor.execute("SELECT * FROM USER")
        return self.cursor.fetchall()

    def close(self):
        self.cnx.close()
