import sudoku.config as config


class Value:

    def __init__(self, num: int) -> None:
        assert num is None or (isinstance(num, int) and 1 <= num <= config.SIZE)
        self.num = num

    def __eq__(self, other: 'Value') -> bool:
        return self.num == other.num

    def __hash__(self) -> int:
        return hash(self.num)

    def __str__(self) -> str:
        return str(self.num) if self.num is not None else "?"

    def __repr__(self) -> str:
        return self.__str__()

    def is_set(self) -> bool:
        return self.num is not None

    def is_empty(self) -> bool:
        return self.num is None


Value.NUM_RANGE = [num for num in range(1, config.SIZE + 1)]
Value.VALUE_RANGE = [Value(num) for num in range(1, config.SIZE + 1)]
Value.EMPTY_VALUE = Value(None)
