from abc import ABCMeta, abstractmethod, ABC
from datetime import datetime
from typing import Union, List

from _dao_.entity.user import Booking


class BookingDAOin(metaclass=ABCMeta):

    @abstractmethod
    def get_booking(self, user_id):
        pass

    def insert_booking(self, booking: Booking):
        pass

    def get_user_booking(self, user_id):
        pass

    def delete_user_booking(self, user_id, booking_id):
        pass


class BookingDAOim(BookingDAOin):
    def __init__(self, connection):
        self.cnx = connection.cnx
        self.cursor = self.cnx.cursor()

    def get_booking(self, user_id):

        query = f'SELECT booking.booking_id, room.room_type FROM booking INNER JOIN room ON booking.room_id=room.room_id WHERE booking.user_id={user_id};'

        self.cursor.execute(query)
        booking_data = self.cursor.fetchall()
        all_booking = []
        if booking_data:
            for data in booking_data:
                booking = {
                    'booking_id': data[0],
                    'room_type': data[1]
                }
                all_booking.append(booking)
            # for _ in range(len(booking_id)):
            #     info = [booking_id[_][0], booking_id[_][1]]
            #     all_booking.append(info)
        return all_booking

    def insert_booking(self, booking: Booking):
        if booking.user_id is None:
            print("Invalid user_id. Booking not inserted.")
            return

        query = f'INSERT INTO booking (room_id, user_id, room_type, check_in_date, check_out_date, number_people) VALUES ("{booking.room_id}", "{booking.user_id}", "{booking.room_type}", "{booking.check_in_date}", "{booking.check_out_date}","{booking.number_people}")'
        print(booking.user_id, booking.room_type)
        try:
            self.cursor.execute(query)
            self.cnx.commit()
        except Exception as e:
            print(f"Error adding booking: {str(e)}")

    def get_user_bookings(self, user_id):
        query = f"SELECT room.room_id, booking.booking_id, room.room_type, room.max_capacity, room.room_prise, booking.check_in_date, booking.check_out_date FROM booking INNER JOIN room ON booking.room_id=room.room_id WHERE booking.user_id={user_id};"

        self.cursor.execute(query)
        bookings = self.cursor.fetchall()

        all_bookings = []
        total_coast = 0
        for booking in bookings:
            room_id, booking_id, room_type, max_capacity, room_price, check_in_date, check_out_date = booking
            if isinstance(check_in_date, datetime):
                check_in = check_in_date
            else:
                check_in = datetime.strptime(check_in_date, "%Y-%m-%d")
            if isinstance(check_out_date, datetime):
                check_out = check_out_date
            else:
                check_out = datetime.strptime(check_out_date, "%Y-%m-%d")
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
        query = f"DELETE FROM booking WHERE user_id={user_id} AND booking_id={booking_id};"
        self.cursor.execute(query)
        self.cnx.commit()
        if self.cursor.rowcount > 0:
            return True  # Booking deleted successfully
        else:
            return False  # No booking found for the given user_id and booking_id

