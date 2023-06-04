from abc import ABCMeta, abstractmethod, ABC
from typing import Union, List
from _dao_.entity.room import Room


class RoomDAOin(metaclass=ABCMeta):
    @abstractmethod
    def get_by_id(self, room_id: int) -> Union[Room, bool]:
        pass

    @abstractmethod
    def get_room(self, room_type):
        pass

    @abstractmethod
    def get_room_status(self, room_id):
        pass

    @abstractmethod
    def get_available_rooms(self, room_type, number_people):
        pass

    @abstractmethod
    def update_status(self, room_id, status):
        pass


class RoomDAOim(RoomDAOin, ABC):
    def __init__(self, connection):
        self.cnx = connection.cnx
        self.cursor = self.cnx.cursor()

    # @abstractmethod
    def get_by_id(self, room_id: int) -> Union[Room, bool]:
        query = f'SELECT room_id, room_prise, room_type, max_capacity, status FROM room WHERE room_id="{room_id}";'
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        if result:
            return Room(room_id=result[0][0], room_prise=result[0][1], room_type=result[0][0], max_capacity=result[0][3])
        return False

    # form.number_people, form.room_type, form.room_price
    # @abstractmethod
    def get_room(self, room_type: str):
        query = f'SELECT room_id FROM room WHERE room_type={room_type};'
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        #####
        if result:
            # список id з room
            return

        return False

    # @abstractmethod
    def get_room_status(self, room_id: int):
        query = f"SELECT status FROM room WHERE room_id = {room_id};"
        self.cursor.execute(query)
        result = self.cursor.fetchone()

        if result:
            return result[0]  # Return the status value
        else:
            return None

    # @abstractmethod
    def get_available_rooms(self, room_type: str, number_people: int) -> List[int]:
        number_people = int(number_people)
        query = f"SELECT room_id, room_type, max_capacity, room_prise, status  FROM room WHERE room_type = '{room_type}' AND max_capacity >= {number_people} AND status = 'available';"
        vals = (number_people, )
        self.cursor.execute(query)
        print(type(number_people))
        # self.cursor.execute(query, vals)
        result = self.cursor.fetchall()

        print(result)
        if result:
            # available_rooms = [row for row in result]
            return result

        return []

    def update_status(self, room_id: int, status: str):
        query = f"UPDATE room SET status = '{status}' WHERE room_id = {room_id};"
        self.cursor.execute(query)
        self.cnx.commit()






