import mysql.connector
from mysql.connector import Error

import os

# Add to os environmental var DB_name, DB_login, DB_server, DB_pass

DB_name = os.getenv("DB_name")
DB_login = os.getenv("DB_login")
DB_server = os.getenv("DB_server")
DB_pass = os.getenv("DB_pass")

class UserDataManager:
    def __init__(self, DB_name = DB_name, DB_login = DB_login, DB_server = DB_server, DB_pass = DB_pass):
        self.DB_pass = DB_pass
        self.DB_login = DB_login
        self.DB_server = DB_server
        self.DB_name = DB_name

    def __connect(self):
