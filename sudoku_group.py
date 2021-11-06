from enum import Enum
from sudoku_board import SudokuBoard


class SudokuGroup:

    def __init__(self, group, type, num):
        assert isinstance(group, dict)
        assert isinstance(type, SudokuGroupType)
        assert 0 <= num < SudokuBoard.SIZE
        self.group = group
        self.type = type
        self.num = num


    # def validate(self):
        # constraints = []
        # for pos, value in self.group.items():

    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        return str(self.value) if self.value is not None else "?"


class SudokuGroupType(Enum):

    ROW = 1
    COL = 2
    BOX = 3

