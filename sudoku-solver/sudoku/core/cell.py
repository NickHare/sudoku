from sudoku.core.position import Position
from sudoku.core.value import Value


class Cell:

    @staticmethod
    def validate_cell_args(pos: Position, val: Value) -> None:
        assert isinstance(pos, Position)
        assert isinstance(val, Value)

    def __init__(self, pos: Position, val: Value) -> None:
        Cell.validate_cell_args(pos, val)
        self.pos = pos
        self.val = val

    def is_set(self) -> bool:
        return self.val.is_set()

    def is_empty(self) -> bool:
        return self.val.is_empty()

    def __eq__(self, other: 'Cell') -> bool:
        return self.pos == other.pos and self.val == other.val

    def __lt__(self, other: 'Cell') -> bool:
        return self.pos < other.pos if self.pos != other.pos else self.val < other.val

    def __hash__(self) -> int:
        return hash((self.pos, self.val))

    def __str__(self) -> str:
        return f'<{str(self.pos)}: {str(self.val)}>'

    def __repr__(self) -> str:
        return self.__str__()
