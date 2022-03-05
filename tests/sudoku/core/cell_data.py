from sudoku.core.position import Position
from sudoku.core.value import Value
from sudoku.core.cell import Cell


class CellData:
    INVALID_TYPE_CELL_ARGS = [
        (None, None), (None, 1), (1, None),
        ("", ""), ("", 1), (1, ""), ("1", "1"), ("abc", "def"),
        ((), ()), ((), 1), (1, ()), ((1, 2, 3), (3, 2, 1)),
        ([], []), ([], 1), (1, []), ([1, 2, 3], [3, 2, 1]),
        ({}, {}), ({}, 1), (1, {}), ({"a": 1}, {"b": 2})
    ]
    VALID_CELL_ARGS = [
        (Position(r, c), Value(num))
        for num in [None, 1, 5, 9]
        for r in [0, 4, 8]
        for c in [0, 4, 8]
    ]
    ORDERED_CELLS = [Cell(Position(r, c), Value(num)) for r in Position.ROW_RANGE for c in Position.COL_RANGE for num in [Value.EMPTY_NUM] + Value.NUM_RANGE]
