import sudoku_config as config


class SudokuCell:

    VALUE_NUM_RANGE = range(1, config.SIZE + 1)
    EMPTY_VALUE = None

    def __init__(self, value: int) -> None:
        assert value is None or 1 <= value <= config.SIZE
        self.value = value

    def __eq__(self, other: 'SudokuCell') -> bool:
        return self.value == other.value

    def __hash__(self) -> int:
        return hash(self.value)

    def __str__(self) -> str:
        return str(self.value) if self.value is not None else "?"

    def __repr__(self) -> str:
        return self.__str__()

    def is_set(self) -> bool:
        return self.value is not None

    def is_empty(self) -> bool:
        return self.value is None
