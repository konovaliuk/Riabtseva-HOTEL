from connector import *
from dao_im import user_im, test_im, score_im

class DAOFactoryMySQL:
    def get_dao_imp(self, cnx: ConnectionMySQL, option: str):
        option = option.lower()
        imp_dao = {
            'user': user_im.UserDAOim,
            'test': test_im.TestDAOim,
            'score': score_im.ScoreDAOim
        }
        if option not in imp_dao:
            return False
        return imp_dao[option](cnx)

class DAOFactory:
    def get_dao(option: str):
        option = option.lower()
        dbms_dao = {
            'mysql': DAOFactoryMySQL
        }
        if option not in dbms_dao:
            return False
        return dbms_dao[option]()



class PoolFactory:
    def get_pool(dbms: str) -> Pool:
        dbms_pools = {
            'mysql': PoolMySQL
        }
        return dbms_pools[dbms]()


class ConnectionFactory:
    def get_connection(option: str, pool: Pool):
        option = option.lower()
        dbms = {
            'mysql': ConnectionMySQL
        }
        if option not in dbms:
            return False
        return dbms[option](pool)
