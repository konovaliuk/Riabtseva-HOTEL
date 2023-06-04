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


__all__ = ['room_available', 'get_available_rooms_for', 'get_room_by_id', 'get_rooms_by_type', 'parse_room_data', 'update_status', 'room_add']


def room_available(room_id):
    try:
        my_cnx = ConnectionFactory.get_connection(dbms, my_pool)
        dao_room = DAOFactory.get_dao(dbms).get_dao_imp(my_cnx, 'room')

        # Check if the room status is "available"
        room_status = dao_room.get_room_status(room_id)
        if room_status != 'available':
            print('The room is not available.')
            return False

    except Exception as e:
        print(f"Error checking room availability: {str(e)}")
        return False

    return True


def get_available_rooms_for(room_type: str, number_people: int):
    try:
        my_cnx = ConnectionFactory.get_connection(dbms, my_pool)
        dao_room = DAOFactory.get_dao(dbms).get_dao_imp(my_cnx, 'room')
        dao_booking = DAOFactory.get_dao(dbms).get_dao_imp(my_cnx, 'booking')

        # Access the DAO and retrieve available rooms based on room type and number of people
        available_rooms = dao_room.get_available_rooms(room_type, number_people)

        return available_rooms

    except Exception as e:
        print(f"Error retrieving available rooms: {str(e)}")
        return []


def get_room_by_id(id):
    my_cnx = ConnectionFactory.get_connection(dbms, my_pool)
    dao_room = DAOFactory.get_dao(dbms).get_dao_imp(my_cnx, 'room')
    return dao_room.get_by_id(id)


def get_rooms_by_type(type):
    my_cnx = ConnectionFactory.get_connection(dbms, my_pool)
    dao_room = DAOFactory.get_dao(dbms).get_dao_imp(my_cnx, 'room')
    return dao_room.get_rooms_by_type(type)


def parse_room_data(room_data):

    parsed_room_data = dict()
    parsed_room_data['room_id'] = room_data[0]
    parsed_room_data['room_type'] = room_data[1]
    parsed_room_data['max_capacity'] = room_data[2]
    parsed_room_data['room_price'] = room_data[3]
    parsed_room_data['status'] = room_data[4]

    return parsed_room_data


def update_status(id, status):
    my_cnx = ConnectionFactory.get_connection(dbms, my_pool)
    dao_room = DAOFactory.get_dao(dbms).get_dao_imp(my_cnx, 'room')
    return dao_room.update_status(id, status)


def room_add(room_id, user_id, room_type, check_in_date, check_out_date, number_people):
    try:
        my_cnx = ConnectionFactory.get_connection(dbms, my_pool)
        dao_booking = DAOFactory.get_dao(dbms).get_dao_imp(my_cnx, 'booking')

        booking = Booking(check_in_date, check_out_date, number_people, room_id, user_id, room_type)
        print('Room_add', booking)
        dao_booking.insert_booking(booking)
        print('Chosen room2:', user_id, room_type, check_in_date, check_out_date, number_people)
        return True

    except Exception as e:
        print(f"Error adding booking: {str(e)}")
        return False