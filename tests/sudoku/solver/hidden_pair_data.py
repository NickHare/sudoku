from sudoku.core.group_type import GroupType
from sudoku.core.position import Position
from sudoku.core.value import Value
from sudoku.core.cell import Cell
from sudoku.solver.hidden_pair import HiddenPair


class HiddenPairData:
    HIDDEN_PAIR_BOARD = [
        [5, 9, None, None, None, None, None, None, None],
        [None, None, 2, 4, None, None, 6, None, None],
        [None, None, None, None, None, None, 5, 7, 9],
        [None, None, None, None, 1, 7, None, 8, 3],
        [None, None, None, None, 8, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None]
    ]

    HIDDEN_PAIR = HiddenPair(GroupType.ROW, 1, (Position(1, 4), Position(1, 5)), (Value(5), Value(9)), [Cell(Position(1, 4), Value(3)), Cell(Position(1, 4), Value(7)), Cell(Position(1, 5), Value(1)), Cell(Position(1, 5), Value(3)), Cell(Position(1, 5), Value(8))])
