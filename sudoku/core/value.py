from sudoku.config import Config


class Value:

    MAX_NUM = Config.SIZE
    MIN_NUM = 1
    EMPTY_NUM = None
    NUM_RANGE = [num for num in range(MIN_NUM, MAX_NUM + 1)]

    @staticmethod
    def validate_value_args(num: int) -> None:
        assert num == Value.EMPTY_NUM or isinstance(num, int)
        assert num == Value.EMPTY_NUM or Value.MIN_NUM <= num <= Value.MAX_NUM

    def __init__(self, num: int) -> None:
        Value.validate_value_args(num)
        self.num = num

    def __eq__(self, other: 'Value') -> bool:
        return self.num == other.num

    def __lt__(self, other: 'Value') -> bool:
        result = None
        if other.is_empty():
            result = False
        elif self.is_empty():
            result = True
        else:
            result = self.num < other.num
        return result

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


Value.EMPTY_VALUE = Value(Value.EMPTY_NUM)
Value.VALUE_RANGE = [Value(num) for num in Value.NUM_RANGE]
