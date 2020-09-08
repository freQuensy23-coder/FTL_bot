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
        """Connect to  DB . Raise Error if some troubles."""
        conn = sqlite3.connect(self.DB_name)
        return conn

    def add_new_user(self, id, user_id, user_name = "UNASSIGNED", status="waiting_name"):
        """Register new purple in system"""
        status_equation = {"waiting_name": 0, "waiting_start": 1, "waiting_check": 2}
        status_value = status_equation[status]
        self.cursor.execute(f"INSERT INTO users ({id}, {user_id}, '{user_name}', {status_value})")
        self.connection.commit()

    def add_check_in(self, id, user_id, time0, time1, place, status = True):
        """Add check in to user id from time0 to time 1"""
        status_equation = {True: 1, False: 0}
        status_value = status_equation[status]
        self.cursor.execute(f"INSERT INTO checks ({id}, {user_id}, '{place}', '{time0}','{time1}', {status_value})")
        self.connection.commit()

    def add_user_name(self, user_id, name):
        """Connect user id to real purple name"""
        self.cursor.execute(f"""UPDATE users
                            SET name = '{name}'
                            WHERE user_id = {user_id}
                            """)

    def change_name(self, user_id, new_name):
        """Change user_id's name"""
        self.cursor.execute(f"""UPDATE users
                            SET name = '{new_name}'
                            WHERE user_id = {user_id}
                            """)