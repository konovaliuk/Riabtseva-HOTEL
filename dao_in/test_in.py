from abc import ABCMeta, abstractmethod
from typing import Union
from entity.test import *

class TestDAOin(metaclass=ABCMeta):
    @abstractmethod
    def get_by_id(self, test_id: int) -> Union[Test, bool]:
        pass

    @abstractmethod
    def insert(self, test: Test):
        pass

    @abstractmethod
    def update(self, test: Test):
        pass

    @abstractmethod
    def delete(self, test: Test):
        pass