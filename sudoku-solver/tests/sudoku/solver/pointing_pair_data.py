from sudoku.core.group_type import GroupType
from sudoku.core.position import Position
from sudoku.core.value import Value
from sudoku.core.cell import Cell
from sudoku.solver.pointing_pair import PointingPair


class PointingPairData:
    POINTING_PAIR_BOARD = [
        [7, None, None, None, None, 5, None, None, 8],
        [None, None, None, None, None, None, 2, None, None],
        [None, 9, 8, None, None, None, None, None, None],
        [1, 6, None, 3, None, None, None, None, None],
        [2, 5, None, 6, None, None, 3, None, None],
        [3, None, None, 4, None, None, None, None, None],
        [4, None, 6, None, None, None, None, 3, None],
        [None, None, 5, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None]
    ]

    POINTING_PAIR = PointingPair(GroupType.BOX, 0, (Position(0, 1), Position(0, 2)), Value(2), [Cell(Position(0, 3), Value(2)), Cell(Position(0, 4), Value(2))])
