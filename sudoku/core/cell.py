from sudoku.core.position import Position
from sudoku.core.value import Value


class Cell:

    def __init__(self, pos: Position, val: Value) -> None:
        assert isinstance(pos, Position)
        assert isinstance(val, Value)
        self.pos = pos
        self.val = val

    def is_set(self) -> bool:
        return self.val.is_set()

    def is_empty(self) -> bool:
        return self.val.is_empty()

    def __eq__(self, other) -> bool:
        return self.pos == other.pos and self.val == other.val

    def __hash__(self) -> int:
        return hash((self.pos, self.val))

    def __str__(self) -> str:
        return f'({str(self.pos)}, {str(self.val)})'

    def __repr__(self) -> str:
        return self.__str__()
