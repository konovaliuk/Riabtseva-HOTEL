from typing import Union
from entity.user import *
from dao_in.user_in import *


class UserDAOim(UserDAOin):
    def __init__(self, connection):
        self.cnx = connection.cnx
        self.cursor = self.cnx.cursor()

    def get_by_id(self, user_id: int) -> Union[User, bool]:
        query = f'SELECT user_id, first_name, last_name, email, password FROM users WHERE user_id="{user_id}";'
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        if result:
            return User(user_id=result[0][0], first_name=result[0][1], last_name=result[0][2], email=result[0][3],
                        password=result[0][4])
        return False

    def get_by_email(self, email: str) -> Union[User, bool]:
        query = f'SELECT user_id, first_name, last_name, email, password FROM users WHERE email="{email}";'
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        if result:
            return User(user_id=result[0][0], first_name=result[0][1], last_name=result[0][2], email=result[0][3],
                        password=result[0][4])
        return False

    def insert(self, user: User):
        try:
            query = 'INSERT INTO users (first_name, last_name, email, password, role_id)\n' + \
                    f'VALUES ("{user._first_name}", "{user._last_name}", "{user._email}", "{user._password}", {2});'
            self.cursor.execute(query)
            self.cnx.commit()
        except:
            print("Error")

    def update(self, user: User):
        try:
            self.cursor.execute("UPDATE users SET first_name=%s, last_name=%s, email=%s, password=%s  WHERE user_id=%s",
                                (user._first_name, user._last_name, user._email, user._password, user._user_id))
            self.cnx.commit()
        except:
            print("Error")

    def delete(self, user: User):
        query = 'DELETE FROM users\n' + \
                f'WHERE user_id="{user.user_id}";'
        self.cursor.execute(query)
        self.cnx.commit()

    def __del__(self):
        self.cursor.close()
