from abc import ABCMeta, abstractmethod
from typing import Union, List
from datetime import datetime

from sqlalchemy.orm import Session
from sqlalchemy import text

from models import Booking, Room


class BookingDAOin(metaclass=ABCMeta):

    @abstractmethod
    def get_booking(self, user_id):
        pass

    def insert_booking(self, booking: Booking):
        pass

    def get_user_bookings(self, user_id):
        pass

    def delete_user_booking(self, user_id, booking_id):
        pass


class BookingDAOim(BookingDAOin):
    def __init__(self, session: Session):
        self.session = session

    def get_booking(self, user_id):
        bookings = self.session.query(Booking.booking_id, Room.room_type).join(Room).filter(Booking.user_id == user_id).all()
        all_booking = []
        for booking in bookings:
            booking_id, room_type = booking
            all_booking.append({
                'booking_id': booking_id,
                'room_type': room_type
            })
        return all_booking

    def insert_booking(self, booking: Booking):
        if booking.user_id is None:
            print("Invalid user_id. Booking not inserted.")
            return
        self.session.add(booking)
        self.session.commit()

    def get_user_bookings(self, user_id):
        bookings = self.session.query(Room.room_id, Booking.booking_id, Room.room_type, Room.max_capacity, Room.room_price,
                                      Booking.check_in_date, Booking.check_out_date).join(Booking).filter(Booking.user_id == user_id).all()

        all_bookings = []
        total_coast = 0
        for booking in bookings:
            room_id, booking_id, room_type, max_capacity, room_price, check_in_date, check_out_date = booking
            check_in = check_in_date if isinstance(check_in_date, datetime) else datetime.strptime(check_in_date, "%Y-%m-%d")
            check_out = check_out_date if isinstance(check_out_date, datetime) else datetime.strptime(check_out_date, "%Y-%m-%d")
            duration = (check_out - check_in).days
            total_price = room_price * duration

            booking_info = {
                'room_id': room_id,
                'booking_id': booking_id,
                'room_type': room_type,
                'max_capacity': max_capacity,
                'room_price': room_price,
                'check_in_date': check_in_date,
                'check_out_date': check_out_date,
                'total_price': total_price
            }
            all_bookings.append(booking_info)
            total_coast += total_price

        return all_bookings, total_coast

    def delete_user_booking(self, user_id, booking_id):
        rows_deleted = self.session.query(Booking).filter(Booking.user_id == user_id, Booking.booking_id == booking_id).delete()
        self.session.commit()
        return rows_deleted > 0

