from abc import ABCMeta, abstractmethod
from typing import Union
from entity.user import *


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