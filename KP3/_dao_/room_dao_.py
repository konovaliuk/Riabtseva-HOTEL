from abc import ABCMeta, abstractmethod, ABC
from typing import Union, List

from sqlalchemy.orm import Session
from sqlalchemy import and_
from _dao_.entity.room import Room
from models.models import Room


class RoomDAOin(metaclass=ABCMeta):
    @abstractmethod
    def get_by_id(self, room_id: int) -> Union[Room, bool]:
        pass

    @abstractmethod
    def get_room(self, room_type: str) -> List[Room]:
        pass

    @abstractmethod
    def get_room_status(self, room_id: int) -> Union[str, None]:
        pass

    @abstractmethod
    def get_available_rooms(self, room_type: str, number_people: int) -> List[int]:
        pass

    @abstractmethod
    def update_status(self, room_id: int, status: str):
        pass


class RoomDAOim(RoomDAOin):
    def __init__(self, session: Session):
        self.session = session

    def get_room(self, room_type: str) -> List[Room]:
        return self.session.query(Room).filter(Room.room_type == room_type).all()

    def get_by_id(self, room_id: int) -> Union[Room, bool]:
        room = self.session.query(Room).filter(Room.room_id == room_id).first()
        return room if room is not None else False

    def get_room_status(self, room_id: int) -> Union[str, None]:
        room = self.get_by_id(room_id)
        if room:
            return room.status
        return None

    def get_available_rooms(self, room_type: str, number_people: int) -> List[int]:
        number_people = int(number_people)
        available_rooms = self.session.query(Room).filter(
            and_(
                Room.room_type == room_type,
                Room.max_capacity >= number_people,
                Room.status == 'available'
            )
        ).all()
        return [int(room.room_id) for room in available_rooms]

    def update_status(self, room_id: int, status: str):
        room = self.get_by_id(room_id)
        if room:
            room.status = status
            self.session.commit()
