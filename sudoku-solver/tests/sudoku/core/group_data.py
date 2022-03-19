from sudoku.core.conflict import Conflict
from sudoku.core.group import GroupType
from sudoku.core.cell import Cell
from sudoku.core.position import Position
from sudoku.core.value import Value
from sudoku.config import Config


class GroupData:
    INVALID_TYPE_GROUP_ARGS = [
        (None, None, None), (None, None, 1), (None, 1, None), (1, None, None),
        ("", "", ""), ("", "", 1), ("", 1, ""), (1, "", ""), ("1", "2", "3"), ("abc", "def", "ghi"),
        ((), (), ()), ((), (), 1), ((), 1, ()), (1, (), ()), ((1, 2, 3), (3, 2, 1), (2, 1, 3)),
        ([], [], []), ([], [], 1), ([], 1, []), (1, [], []), ([1, 2, 3], [3, 2, 1], [2, 1, 3]),
        ({}, {}, {}), ({}, {}, 1), ({}, 1, {}), (1, {}, {}), ({"a": 1}, {"b": 2}, {"c": 3})
    ]

    REPEATED_POSITION_GROUP_ARGS = [
        (GroupType.ROW, 0, [
            Cell(Position(0, 0), Value(1)),
            Cell(Position(0, 1), Value(2)),
            Cell(Position(0, 2), Value(3)),
            Cell(Position(0, 3), Value(4)),
            Cell(Position(0, 4), Value(5)),
            Cell(Position(0, 5), Value(6)),
            Cell(Position(0, 6), Value(7)),
            Cell(Position(0, 7), Value(8)),
            Cell(Position(0, 7), Value(9)),
        ]),
        (GroupType.COL, 0, [
            Cell(Position(0, 0), Value(1)),
            Cell(Position(1, 0), Value(2)),
            Cell(Position(2, 0), Value(3)),
            Cell(Position(3, 0), Value(4)),
            Cell(Position(4, 0), Value(5)),
            Cell(Position(5, 0), Value(6)),
            Cell(Position(6, 0), Value(7)),
            Cell(Position(7, 0), Value(8)),
            Cell(Position(7, 0), Value(9)),
        ]),
        (GroupType.BOX, 0, [
            Cell(Position(0, 0), Value(1)),
            Cell(Position(0, 1), Value(2)),
            Cell(Position(0, 2), Value(3)),
            Cell(Position(1, 0), Value(4)),
            Cell(Position(1, 1), Value(5)),
            Cell(Position(1, 2), Value(6)),
            Cell(Position(2, 0), Value(7)),
            Cell(Position(2, 1), Value(8)),
            Cell(Position(2, 1), Value(9)),
        ]),
    ]

    WRONG_POSITION_GROUP_ARGS = [
        (GroupType.ROW, 0, [
            Cell(Position(0, 0), Value(1)),
            Cell(Position(0, 1), Value(2)),
            Cell(Position(0, 2), Value(3)),
            Cell(Position(0, 3), Value(4)),
            Cell(Position(0, 4), Value(5)),
            Cell(Position(0, 5), Value(6)),
            Cell(Position(0, 6), Value(7)),
            Cell(Position(0, 7), Value(8)),
            Cell(Position(1, 8), Value(9)),
        ]),
        (GroupType.COL, 0, [
            Cell(Position(0, 0), Value(1)),
            Cell(Position(1, 0), Value(2)),
            Cell(Position(2, 0), Value(3)),
            Cell(Position(3, 0), Value(4)),
            Cell(Position(4, 0), Value(5)),
            Cell(Position(5, 0), Value(6)),
            Cell(Position(6, 0), Value(7)),
            Cell(Position(7, 0), Value(8)),
            Cell(Position(8, 1), Value(9)),
        ]),
        (GroupType.BOX, 0, [
            Cell(Position(0, 0), Value(1)),
            Cell(Position(0, 1), Value(2)),
            Cell(Position(0, 2), Value(3)),
            Cell(Position(1, 0), Value(4)),
            Cell(Position(1, 1), Value(5)),
            Cell(Position(1, 2), Value(6)),
            Cell(Position(2, 0), Value(7)),
            Cell(Position(2, 1), Value(8)),
            Cell(Position(2, 3), Value(9)),
        ]),
    ]

    EMPTY_GROUP_ARGS = [
        (GroupType.ROW, 0, [Cell(Position(0, c), Value(None)) for c in Position.ROW_RANGE]),
        (GroupType.ROW, 4, [Cell(Position(4, c), Value(None)) for c in Position.ROW_RANGE]),
        (GroupType.ROW, 8, [Cell(Position(8, c), Value(None)) for c in Position.ROW_RANGE]),
        (GroupType.COL, 0, [Cell(Position(r, 0), Value(None)) for r in Position.COL_RANGE]),
        (GroupType.COL, 4, [Cell(Position(r, 4), Value(None)) for r in Position.COL_RANGE]),
        (GroupType.COL, 8, [Cell(Position(r, 8), Value(None)) for r in Position.COL_RANGE]),
        (GroupType.BOX, 0, [Cell(Position(r, c), Value(None)) for r in range(0, 3) for c in range(0, 3)]),
        (GroupType.BOX, 2, [Cell(Position(r, c), Value(None)) for r in range(0, 3) for c in range(6, 9)]),
        (GroupType.BOX, 4, [Cell(Position(r, c), Value(None)) for r in range(3, 6) for c in range(3, 6)]),
        (GroupType.BOX, 6, [Cell(Position(r, c), Value(None)) for r in range(6, 9) for c in range(0, 3)]),
        (GroupType.BOX, 8, [Cell(Position(r, c), Value(None)) for r in range(6, 9) for c in range(6, 9)]),
    ]

    PARTIAL_GROUP_ARGS = [
        (GroupType.ROW, 0, [Cell(Position(0, c), Value(None if c % 2 else c + 1)) for c in Position.ROW_RANGE]),
        (GroupType.ROW, 4, [Cell(Position(4, c), Value(None if c % 2 else c + 1)) for c in Position.ROW_RANGE]),
        (GroupType.ROW, 8, [Cell(Position(8, c), Value(None if c % 2 else c + 1)) for c in Position.ROW_RANGE]),
        (GroupType.COL, 0, [Cell(Position(r, 0), Value(None if r % 2 else r + 1)) for r in Position.COL_RANGE]),
        (GroupType.COL, 4, [Cell(Position(r, 4), Value(None if r % 2 else r + 1)) for r in Position.COL_RANGE]),
        (GroupType.COL, 8, [Cell(Position(r, 8), Value(None if r % 2 else r + 1)) for r in Position.COL_RANGE]),
        (GroupType.BOX, 0, [Cell(Position(r, c), Value(None if r + c % 2 else r * Config.BOX_SIZE + c + 1)) for r in range(0, 3) for c in range(0, 3)]),
        (GroupType.BOX, 2, [Cell(Position(r, c), Value(None if r + c % 2 else r * Config.BOX_SIZE + c - 5)) for r in range(0, 3) for c in range(6, 9)]),
        (GroupType.BOX, 4, [Cell(Position(r, c), Value(None if r + c % 2 else (r - 3) * Config.BOX_SIZE + c - 2)) for r in range(3, 6) for c in range(3, 6)]),
        (GroupType.BOX, 6, [Cell(Position(r, c), Value(None if r + c % 2 else (r - 6) * Config.BOX_SIZE + c + 1)) for r in range(6, 9) for c in range(0, 3)]),
        (GroupType.BOX, 8, [Cell(Position(r, c), Value(None if r + c % 2 else (r - 6) * Config.BOX_SIZE + c - 5)) for r in range(6, 9) for c in range(6, 9)]),
    ]

    FULL_GROUP_ARGS = [
        (GroupType.ROW, 0, [Cell(Position(0, c), Value(c + 1)) for c in Position.ROW_RANGE]),
        (GroupType.ROW, 4, [Cell(Position(4, c), Value(c + 1)) for c in Position.ROW_RANGE]),
        (GroupType.ROW, 8, [Cell(Position(8, c), Value(c + 1)) for c in Position.ROW_RANGE]),
        (GroupType.COL, 0, [Cell(Position(r, 0), Value(r + 1)) for r in Position.COL_RANGE]),
        (GroupType.COL, 4, [Cell(Position(r, 4), Value(r + 1)) for r in Position.COL_RANGE]),
        (GroupType.COL, 8, [Cell(Position(r, 8), Value(r + 1)) for r in Position.COL_RANGE]),
        (GroupType.BOX, 0, [Cell(Position(r, c), Value(r * Config.BOX_SIZE + c + 1)) for r in range(0, 3) for c in range(0, 3)]),
        (GroupType.BOX, 2, [Cell(Position(r, c), Value(r * Config.BOX_SIZE + c - 5)) for r in range(0, 3) for c in range(6, 9)]),
        (GroupType.BOX, 4, [Cell(Position(r, c), Value((r - 3) * Config.BOX_SIZE + c - 2)) for r in range(3, 6) for c in range(3, 6)]),
        (GroupType.BOX, 6, [Cell(Position(r, c), Value((r - 6) * Config.BOX_SIZE + c + 1)) for r in range(6, 9) for c in range(0, 3)]),
        (GroupType.BOX, 8, [Cell(Position(r, c), Value((r - 6) * Config.BOX_SIZE + c - 5)) for r in range(6, 9) for c in range(6, 9)]),
    ]

    REPEATED_VALUE_GROUP_ARGS = [
        (GroupType.ROW, 0, [
            Cell(Position(0, 0), Value(1)),
            Cell(Position(0, 1), Value(2)),
            Cell(Position(0, 2), Value(3)),
            Cell(Position(0, 3), Value(4)),
            Cell(Position(0, 4), Value(5)),
            Cell(Position(0, 5), Value(6)),
            Cell(Position(0, 6), Value(7)),
            Cell(Position(0, 7), Value(8)),
            Cell(Position(0, 8), Value(8)),
        ], [
            Conflict(GroupType.ROW, 0, Value(8), [Position(0, 7), Position(0, 8)])
        ]),
        (GroupType.COL, 0, [
            Cell(Position(0, 0), Value(1)),
            Cell(Position(1, 0), Value(2)),
            Cell(Position(2, 0), Value(3)),
            Cell(Position(3, 0), Value(4)),
            Cell(Position(4, 0), Value(5)),
            Cell(Position(5, 0), Value(6)),
            Cell(Position(6, 0), Value(7)),
            Cell(Position(7, 0), Value(8)),
            Cell(Position(8, 0), Value(8)),
        ], [
            Conflict(GroupType.COL, 0, Value(8), [Position(7, 0), Position(8, 0)])
        ]),
        (GroupType.BOX, 0, [
            Cell(Position(0, 0), Value(1)),
            Cell(Position(0, 1), Value(2)),
            Cell(Position(0, 2), Value(3)),
            Cell(Position(1, 0), Value(4)),
            Cell(Position(1, 1), Value(5)),
            Cell(Position(1, 2), Value(6)),
            Cell(Position(2, 0), Value(7)),
            Cell(Position(2, 1), Value(8)),
            Cell(Position(2, 2), Value(8)),
        ], [
            Conflict(GroupType.BOX, 0, Value(8), [Position(2, 1), Position(2, 2)])
        ]),
    ]

    ROW_POSITIONS = [
        (0, [
            Position(0, 0), Position(0, 1), Position(0, 2),
            Position(0, 3), Position(0, 4), Position(0, 5),
            Position(0, 6), Position(0, 7), Position(0, 8),
        ]),
        (4, [
            Position(4, 0), Position(4, 1), Position(4, 2),
            Position(4, 3), Position(4, 4), Position(4, 5),
            Position(4, 6), Position(4, 7), Position(4, 8),
        ]),
        (8, [
            Position(8, 0), Position(8, 1), Position(8, 2),
            Position(8, 3), Position(8, 4), Position(8, 5),
            Position(8, 6), Position(8, 7), Position(8, 8),
        ])
    ]

    COL_POSITIONS = [
        (0, [
            Position(0, 0), Position(1, 0), Position(2, 0),
            Position(3, 0), Position(4, 0), Position(5, 0),
            Position(6, 0), Position(7, 0), Position(8, 0),
        ]),
        (4, [
            Position(0, 4), Position(1, 4), Position(2, 4),
            Position(3, 4), Position(4, 4), Position(5, 4),
            Position(6, 4), Position(7, 4), Position(8, 4),
        ]),
        (8, [
            Position(0, 8), Position(1, 8), Position(2, 8),
            Position(3, 8), Position(4, 8), Position(5, 8),
            Position(6, 8), Position(7, 8), Position(8, 8),
        ])
    ]
    BOX_POSITIONS = [
        (0, [
            Position(0, 0), Position(0, 1), Position(0, 2),
            Position(1, 0), Position(1, 1), Position(1, 2),
            Position(2, 0), Position(2, 1), Position(2, 2),
        ]),
        (2, [
            Position(0, 6), Position(0, 7), Position(0, 8),
            Position(1, 6), Position(1, 7), Position(1, 8),
            Position(2, 6), Position(2, 7), Position(2, 8),
        ]),
        (4, [
            Position(3, 3), Position(3, 4), Position(3, 5),
            Position(4, 3), Position(4, 4), Position(4, 5),
            Position(5, 3), Position(5, 4), Position(5, 5),
        ]),
        (6, [
            Position(6, 0), Position(6, 1), Position(6, 2),
            Position(7, 0), Position(7, 1), Position(7, 2),
            Position(8, 0), Position(8, 1), Position(8, 2),
        ]),
        (8, [
            Position(6, 6), Position(6, 7), Position(6, 8),
            Position(7, 6), Position(7, 7), Position(7, 8),
            Position(8, 6), Position(8, 7), Position(8, 8),
        ])
    ]
