class User:
    def __init__(self, first_name: str, last_name: str, email: str, password: str, booking: list, user_id=None):
        if user_id is None:
            pass
        else:
            self._user_id = user_id

        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._password = password
        self._booking = booking

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


class Booking:

    def __init__(self, check_in_date: str, check_out_date: str, number_people: int, room_id: int, user_id: int, room_type: str, booking_id=None):

        self._check_in_date = check_in_date
        self._check_out_date = check_out_date
        self._number_people = number_people
        self._room_id = room_id
        self._booking_id = booking_id
        self._user_id = user_id
        self._room_type = room_type

    @property
    def booking_id(self) -> int:
        return self._booking_id

    @booking_id.setter
    def booking_id(self, val: int):
        self._booking_id = val

    @property
    def room_id(self) -> int:
        return self._room_id

    @room_id.setter
    def room_id(self, val: int):
        self._room_id = val

    @property
    def check_in_date(self) -> str:
        return self._check_in_date

    @check_in_date.setter
    def check_in_date(self, val: str):
        self._check_in_date = val

    @property
    def check_out_date(self) -> str:
        return self._check_out_date

    @check_out_date.setter
    def check_out_date(self, val: str):
        self._check_out_date = val

    @property
    def user_id(self) -> int:
        return self._user_id

    @user_id.setter
    def user_id(self, val: int):
        self._user_id = val

    @property
    def number_people(self) -> int:
        return self._number_people

    @number_people.setter
    def number_people(self, val: int):
        self._number_people = val

    @property
    def room_type(self) -> str:
        return self._room_type

    @room_type.setter
    def room_type(self, val: str):
        self._room_type = val
