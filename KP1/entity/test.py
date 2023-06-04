class Test:
    def __init__(self, test_id: int, test_title: str):
        self._test_id = test_id
        self._test_title = test_title

    def test_id(self) -> int:
        return self._test_id

    def test_id(self, val: int):
        self._test_id = val

    def test_title(self) -> str:
        return self._test_title

    def test_title(self, val: str):
        self._test_title = val

    def __str__(self) -> str:
        return f"{self.test_id} {self.test_title}"