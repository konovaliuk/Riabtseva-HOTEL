from abc import ABCMeta, abstractmethod
from entity.score import *

class ScoreDAOin(metaclass=ABCMeta):
    @abstractmethod
    def insert(self, score: Score):
        pass

    @abstractmethod
    def update(self, score: Score):
        pass

    @abstractmethod
    def delete(self, score: Score):
        pass
