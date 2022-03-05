from sudoku.core.position import Position


class PositionData:
    INVALID_TYPE_POSITION_ARGS = [
        (None, None), (None, 1), (1, None),
        ("", ""), ("", 1), (1, ""), ("1", "1"), ("abc", "def"),
        ((), ()), ((), 1), (1, ()), ((1, 2, 3), (3, 2, 1)),
        ([], []), ([], 1), (1, []), ([1, 2, 3], [3, 2, 1]),
        ({}, {}), ({}, 1), (1, {}), ({"a": 1}, {"b": 2})
    ]
    OUT_OF_RANGE_POSITION_ARGS = [
        (-100, -100), (-100, 1), (1, -100),
        (-1, -1), (-1, 1), (1, -1),
        (9, 9), (9, 1), (1, 9),
        (10, 10), (10, 1), (1, 10),
        (100, 100), (100, 1), (1, 100)
    ]
    VALID_POSITION_ARGS = [(r, c) for r in Position.ROW_RANGE for c in Position.COL_RANGE]
    ORDERED_POSITIONS = [Position(r, c) for r in Position.ROW_RANGE for c in Position.COL_RANGE]
