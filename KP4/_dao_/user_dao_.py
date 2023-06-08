from abc import ABCMeta, abstractmethod
from typing import Union
# from .entity.user import User
from _dao_.booking_dao_ import BookingDAOim
from models import User
import hashlib


class UserDAOin(metaclass=ABCMeta):
    @abstractmethod
    def get_by_id(self, user_id: int) -> Union[User, bool]:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> Union[User, bool]:
        pass

    @abstractmethod
    def insert(self, user: User):
        pass

    @abstractmethod
    def update(self, user: User):
        pass

    @abstractmethod
    def delete(self, user: User):
        pass


class UserDAOim(UserDAOin):
    def __init__(self, session):
        self.session = session

    @staticmethod
    def hash(password: str):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def insert(self, user: User):
        user.password = self.hash(user.password)
        self.session.add(user)
        self.session.commit()

    def get_by_id(self, user_id: int) -> Union[User, bool]:
        return self.session.query(User).filter(User.user_id == user_id).first()

    def get_by_email(self, email: str) -> Union[User, bool]:
        return self.session.query(User).filter(User.email == email).first()

    def update(self, user: User):
        existing_user = self.get_by_id(user.user_id)
        if existing_user:
            existing_user.first_name = user.first_name
            existing_user.last_name = user.last_name
            existing_user.email = user.email
            existing_user.password = self.hash(user.password)
            existing_user.role_id = user.role_id
            self.session.commit()

    def delete(self, user: User):
        existing_user = self.get_by_id(user.user_id)
        if existing_user:
            self.session.delete(existing_user)
            self.session.commit()

    def __del__(self):
        self.session.close()

    def read_all(self):
        return self.session.query(User).all()


