class Score:
    def __init__(self, score: float,  user_id: int, test_id: int):
        self._score = score
        self._test_id = test_id
        self._user_id = user_id

    def score(self) -> float:
        return self._score

    def score(self, val: float):
        self._score = val

    def test_id(self) -> int:
        return self._test_id

    def test_id(self, val: int):
        self._test_id = val

    def user_id(self) -> str:
        return self._user_id

    def user_id(self, val: str):
        self._user_id = val

    def __str__(self) -> str:
        return f"{self.score}, {self.test_id}, {self.user_id}"