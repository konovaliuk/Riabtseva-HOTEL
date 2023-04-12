class User:
    def __init__(self, first_name: str, last_name: str, email: str, password: str,  user_id=None):
        if user_id is None:
            pass
        else:
            self._user_id = user_id

        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._password = password

    def user_id(self) -> int:
        return self._user_id

    def user_id(self, val: int):
        self._user_id = val

    def first_name(self) -> str:
        return self._first_name

    def first_name(self, val: str):
        self._first_name = val

    def last_name(self) -> str:
        return self._last_name

    def last_name(self, val: str):
        self._last_name = val

    def email(self) -> str:
        return self._email

    def email(self, val: str):
        self._email = val

    def password(self) -> str:
        return self._password

    def password(self, val: str):
        self._password = val

    def __str__(self) -> str:
        if hasattr(self, '_user_id'):
            return f"{self._user_id}, {self._first_name}, {self._last_name}, {self._email}"
        else:
            return f"{self._first_name}, {self._last_name}, {self._email}"

    @property
    def user_id(self):
        return self._user_id