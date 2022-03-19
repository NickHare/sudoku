from sudoku.core.group_type import GroupType
from sudoku.core.position import Position
from sudoku.core.value import Value
from sudoku.core.cell import Cell
from sudoku.solver.naked_pair import NakedPair


class NakedPairData:
    NAKED_PAIR_BOARD = [
        [None, None, None, None, None, 2, 4, 8, None],
        [7, 6, None, 9, 1, None, None, 5, None],
        [4, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None]
    ]

    NAKED_PAIR = NakedPair(GroupType.ROW, 1, (Position(1, 6), Position(1, 8)), (Value(2), Value(3)), [Cell(Position(1, 2), Value(2)), Cell(Position(1, 2), Value(3)), Cell(Position(1, 5), Value(3))])
