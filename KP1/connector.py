from mysql.connector import pooling
from abc import ABCMeta, abstractmethod


class Pool(metaclass=ABCMeta):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def close(self):
        pass


class Connection(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, pool: Pool):
        pass

    @abstractmethod
    def __del__(self):
        pass


class PoolMySQL(Pool):
    def connect(self):
        try:
            self.connection_pool = pooling.MySQLConnectionPool(user='root', password='rootroot',
                                                               host='localhost', database="pis_hostel",
                                                               pool_name='my_pool', pool_size=3)
        except:
            print("Error in pool")

    def close(self):
        self.connection_pool._remove_connections()


class ConnectionMySQL(Connection):
    def __init__(self, pool: PoolMySQL):
        try:
            self.cnx = pool.connection_pool.get_connection()
        except:
            print("Error in connection")

    def __del__(self):
        self.cnx.close()
