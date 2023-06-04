class Room:
    def __init__(self, room_id: int, room_type: str, max_capacity: int, room_prise: int, status: str):
        self._room_id = room_id
        self._room_type = room_type
        self._max_capacity = max_capacity
        self._room_prise = room_prise
        self._status = status

    def room_id(self) -> int:
        return self.room_id

    def room_id(self, val: int):
        self._room_id = val

    def room_type(self) -> str:
        return self._room_type

    def room_type(self, val: str):
        self._room_type = val

    def max_capacity(self) -> int:
        return self.max_capacity

    def max_capacity(self, val: int):
        self._max_capacity = val

    def room_prise(self) -> int:
        return self.room_prise

    def room_prise(self, val: int):
        self._room_prise = val

    def status(self) -> str:
        return self._status

    def status(self, val: str):
        self._status = val
