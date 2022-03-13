from sudoku.core.group_type import GroupType
from sudoku.core.position import Position
from sudoku.core.value import Value
from sudoku.core.cell import Cell
from sudoku.solver.boxed_pair import BoxedPair


class BoxedPairData:
    BOXED_PAIR_BOARD = [
        [8, None, None, None, 2, 7, 5, None, 6],
        [7, 6, 2, None, None, 8, None, None, None],
        [None, None, None, 6, None, None, 7, 8, 2],
        [4, 1, 5, 3, None, None, None, None, None],
        [None, 3, None, 9, 4, 1, None, None, None],
        [None, None, None, None, 5, None, None, 1, None],
        [None, None, None, 1, None, 4, None, None, None],
        [None, None, None, None, None, 5, None, None, None],
        [None, None, None, None, None, None, None, None, None]
    ]

    BOXED_PAIR = BoxedPair(GroupType.ROW, 2, (Position(2, 1), Position(2, 2)), Value(4), [Cell(Position(0, 1), Value(4)), Cell(Position(0, 2), Value(4))])
