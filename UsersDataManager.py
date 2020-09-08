import sqlite3
import os

# Add to os environmental var DB_name, DB_login, DB_server, DB_pass

DB_name = os.getenv("DB_name")
DB_login = os.getenv("DB_login")
DB_server = os.getenv("DB_server")
DB_pass = os.getenv("DB_pass")


class UserDataManager:
    def __init__(self, DB_name=DB_name, DB_login=DB_login, DB_server=DB_server, DB_pass=DB_pass):
        self.DB_pass = DB_pass
        self.DB_login = DB_login
        self.DB_server = DB_server
        self.DB_name = DB_name
        self.connection = self.__connect()
        self.cursor = self.connection.cursor()

    def execute_query(self):
        # TODO
        pass

    def __connect(self):
        """Connect to remote DB server. Raise Error if some troubles."""
        conn = sqlite3.connect(self.DB_name)
        return conn

    def add_new_user(self, user_id, user_name, status="waiting_name"):
        """Register new purple in system"""
        status_equation = {"waiting_name": 0, "waiting_start": 1, "waiting_check": 2}
        status_value = status_equation[status]
        self.cursor.execute(f"INSERT INTO users ({user_id}, {user_name}, {status_value})")
        self.connection.commit()

    def add_check_in(self, user_id, time0, time1, place):
        """Add check in to user id from time0 to time 1"""
        pass
        # TODO

    def add_user_name(self, user_id, name):
        """Connect user id to real purple name"""
        pass
        # TODO
