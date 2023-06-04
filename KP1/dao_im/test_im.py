from typing import Union
from entity.test import *
from dao_in.test_in import *

class TestDAOim(TestDAOin):
    def get_by_id(self, test_id: int) -> Union[Test, bool]:
        query = f'SELECT test_id, test_title FROM tests WHERE test_id="{test_id}";'
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.cursor.close()
        if result:
            return Test(*result[0])
        return False

    @abstractmethod
    def insert(self, test: Test):
        pass

    @abstractmethod
    def update(self, test: Test):
        pass

    @abstractmethod
    def delete(self, test: Test):
        pass