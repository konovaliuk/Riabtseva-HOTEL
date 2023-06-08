from datetime import datetime
from typing import List

from flask import session

from _dao_.factory import *
from _dao_.entity.user import User, Booking
import re
from _dao_.room_dao_ import RoomDAOim

dbms = 'mysql'
my_pool = PoolFactory.get_pool(dbms)
my_pool.connect()
__all__ = ['get_user_by_id', 'get_user_by_email', 'validate_email', 'validate_password', 'validate_user_info', 'create_user', 'validate_login']


def get_user_by_id(id):
    my_cnx = ConnectionFactory.get_connection(dbms, my_pool)
    dao_user = DAOFactory.get_dao(dbms).get_dao_imp(my_cnx, 'user')
    return dao_user.get_by_id(id)


def get_user_by_email(email):
    my_cnx = ConnectionFactory.get_connection(dbms, my_pool)
    dao_user = DAOFactory.get_dao(dbms).get_dao_imp(my_cnx, 'user')

    user = dao_user.get_by_email(email)
    return user


def validate_email(email):
    pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    if len(email) < 5 or len(email) > 255:
        return False
    elif not re.match(pat, email):
        return False
    elif get_user_by_email(email) != False:
        return False
    else:
        return True


def validate_password(password, password_conf):
    if password != password_conf:
        return False
    elif len(password) < 6 or len(password) > 255:
        return False
    elif ' ' in password:
        return False
    else:
        return True


def validate_user_info(first_name, last_name, email, password):
    if validate_email(email):
        return True
    else:
        return False


def create_user(first_name, last_name, email, password):
    if not validate_user_info(first_name, last_name, email, password):
        return False

    new_user = User(first_name, last_name, email, password, booking=[])
    my_cnx = ConnectionFactory.get_connection(dbms, my_pool)
    dao_user = DAOFactory.get_dao(dbms).get_dao_imp(my_cnx, 'user')

    try:
        id = dao_user.insert(new_user)
        new_user._user_id = id
        return new_user
    except:
        print('Error')
        return False


def validate_login(email, password):
    user = get_user_by_email(email)

    if user == False:
        return False
    elif user._password == password:
        return user
    else:
        return False