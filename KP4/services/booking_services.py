from datetime import datetime
from typing import List

from flask import session

from _dao_.factory import *
from _dao_.entity.user import User, Booking
import re
from _dao_.room_dao_ import RoomDAOim
# from services.room_services import room_available
import transaction

from services.room_services import room_available

dbms = 'mysql'
my_pool = PoolFactory.get_pool(dbms)
my_pool.connect()

__all__ = ['get_all_booking', 'validate_booking_info', 'create_booking', 'user_bookings', 'delete_booking']


def get_all_booking():
    my_cnx = ConnectionFactory.get_connection(dbms, my_pool)
    dao_booking = DAOFactory.get_dao(dbms).get_dao_imp(my_cnx, 'booking')
    return dao_booking.get_all()


def validate_booking_info(room_type, check_in_date, check_out_date, number_people):
    # Check if room_type is 'normal' or 'luxe'
    if room_type not in ['normal', 'luxe']:
        print("Error: Invalid room_type. It should be either 'normal' or 'luxe'.")
        return False

    # Check if check_in_date and check_out_date are in the format YYYY-MM-DD
    try:
        datetime.datetime.strptime(check_in_date, '%Y-%m-%d')
        datetime.datetime.strptime(check_out_date, '%Y-%m-%d')
    except ValueError:
        print("Error: Invalid date format. Dates should be in the format YYYY-MM-DD.")
        return False

    # Check if the number of people is less than 5
    if number_people >= 5:
        print("Error: The number of people should be less than 5.")
        return False

    # All validations passed
    return True


def create_booking(number_people, check_in_date, check_out_date, room_type, user_id, room_id):
    if not validate_booking_info(room_type, check_in_date, check_out_date, number_people):
        return False

    if not room_available(room_id):
        print("Error: The specified room is not available.")
        return False

    my_cnx = ConnectionFactory.get_connection(dbms, my_pool)
    dao_booking = DAOFactory.get_dao(dbms).get_dao_imp(my_cnx, 'booking')

    try:
        my_cnx.begin()  # Початок транзакції

        new_booking = Booking(check_in_date, check_out_date, number_people, room_id, user_id)
        dao_booking.insert(new_booking)
        print('Create:', user_id)

        my_cnx.commit()  # Підтвердження транзакції
        return new_booking

    except Exception as e:
        print(f"Error creating booking: {str(e)}")
        my_cnx.rollback()  # Скасування транзакції у разі помилки
        return False


def user_bookings(user_id: int) -> List[dict]:
    my_cnx = ConnectionFactory.get_connection(dbms, my_pool)
    dao_booking = DAOFactory.get_dao(dbms).get_dao_imp(my_cnx, 'booking')
    return dao_booking.get_user_bookings(user_id)


def delete_booking(user_id: int, booking_id: int):
    my_cnx = ConnectionFactory.get_connection(dbms, my_pool)
    dao_booking = DAOFactory.get_dao(dbms).get_dao_imp(my_cnx, 'booking')
    return dao_booking.delete_user_booking(user_id, booking_id)
