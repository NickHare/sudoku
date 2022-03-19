from sudoku.core.position import Position
from sudoku.core.value import Value
from sudoku.core.cell import Cell
from sudoku.core.group import Group
from sudoku.core.group import GroupType


class BoardData:
    VALID_EMPTY_BOARD_ARGS = [
        [
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None]
        ]
    ]

    VALID_FULL_BOARD_ARGS = [
        [
            [4, 8, 5, 3, 1, 9, 7, 6, 2],
            [7, 9, 3, 6, 2, 4, 8, 1, 5],
            [2, 6, 1, 8, 7, 5, 4, 9, 3],
            [3, 1, 2, 7, 9, 6, 5, 8, 4],
            [6, 4, 8, 1, 5, 3, 2, 7, 9],
            [5, 7, 9, 2, 4, 8, 6, 3, 1],
            [8, 2, 6, 4, 3, 1, 9, 5, 7],
            [1, 5, 4, 9, 8, 7, 3, 2, 6],
            [9, 3, 7, 5, 6, 2, 1, 4, 8]
        ], [
            [5, 6, 7, 1, 3, 8, 4, 9, 2],
            [4, 3, 2, 9, 7, 6, 5, 1, 8],
            [9, 1, 8, 4, 2, 5, 6, 3, 7],
            [3, 2, 4, 6, 5, 7, 1, 8, 9],
            [1, 8, 6, 3, 4, 9, 2, 7, 5],
            [7, 9, 5, 8, 1, 2, 3, 6, 4],
            [2, 4, 3, 7, 8, 1, 9, 5, 6],
            [8, 5, 9, 2, 6, 3, 7, 4, 1],
            [6, 7, 1, 5, 9, 4, 8, 2, 3]
        ], [
            [9, 1, 3, 6, 8, 5, 4, 2, 7],
            [6, 8, 7, 4, 2, 3, 9, 1, 5],
            [2, 5, 4, 9, 7, 1, 6, 8, 3],
            [4, 7, 9, 8, 5, 6, 1, 3, 2],
            [1, 6, 2, 3, 4, 7, 5, 9, 8],
            [5, 3, 8, 1, 9, 2, 7, 6, 4],
            [3, 4, 5, 2, 6, 9, 8, 7, 1],
            [7, 2, 6, 5, 1, 8, 3, 4, 9],
            [8, 9, 1, 7, 3, 4, 2, 5, 6]
        ],
        [
           [6, 5, 8, 4, 7, 2, 1, 3, 9],
           [4, 3, 2, 9, 5, 1, 8, 7, 6],
           [9, 1, 7, 6, 3, 8, 5, 4, 2],
           [2, 9, 6, 8, 1, 7, 4, 5, 3],
           [7, 4, 3, 2, 6, 5, 9, 1, 8],
           [5, 8, 1, 3, 9, 4, 2, 6, 7],
           [3, 7, 4, 5, 8, 9, 6, 2, 1],
           [1, 2, 9, 7, 4, 6, 3, 8, 5],
           [8, 6, 5, 1, 2, 3, 7, 9, 4]
        ],
        [
            [8, 4, 9, 1, 3, 5, 6, 7, 2],
            [5, 7, 2, 9, 4, 6, 8, 3, 1],
            [1, 3, 6, 7, 2, 8, 5, 4, 9],
            [3, 2, 8, 6, 9, 4, 1, 5, 7],
            [4, 5, 7, 8, 1, 2, 3, 9, 6],
            [9, 6, 1, 3, 5, 7, 2, 8, 4],
            [7, 8, 3, 2, 6, 9, 4, 1, 5],
            [2, 9, 4, 5, 8, 1, 7, 6, 3],
            [6, 1, 5, 4, 7, 3, 9, 2, 8]
        ],
        [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [4, 5, 6, 7, 8, 9, 1, 2, 3],
            [7, 8, 9, 1, 2, 3, 4, 5, 6],
            [2, 3, 1, 5, 6, 4, 8, 9, 7],
            [5, 6, 4, 8, 9, 7, 2, 3, 1],
            [8, 9, 7, 2, 3, 1, 5, 6, 4],
            [3, 1, 2, 6, 4, 5, 9, 7, 8],
            [6, 4, 5, 9, 7, 8, 3, 1, 2],
            [9, 7, 8, 3, 1, 2, 6, 4, 5],
        ],
    ]

    VALID_PARTIAL_BOARD_ARGS = [
        [  # 0, Random Sheet Easy
            [None, None, None, None, None, None, None, None, None],
            [None, 9, None, 6, None, None, None, None, None],
            [None, 6, None, None, 7, None, 4, None, 3],
            [None, None, 2, None, None, 6, None, None, None],
            [None, None, 8, 1, None, None, None, None, 9],
            [5, None, None, 2, None, None, None, None, None],
            [None, None, None, None, 3, None, None, 5, None],
            [None, None, None, None, 8, 7, None, 2, None],
            [9, 3, None, None, None, None, None, 4, None]
        ],
        [  # 1, Random Sheet Moderate
            [5, None, None, 1, None, None, None, None, None],
            [None, 3, None, None, None, 6, None, None, None],
            [None, None, None, 4, None, None, None, None, 7],
            [None, None, 4, None, 5, None, None, 8, None],
            [None, None, None, None, 4, None, 2, None, None],
            [None, 9, None, None, None, None, 3, None, None],
            [2, 4, None, None, None, 1, None, None, 6],
            [8, None, None, None, 6, None, 7, None, 1],
            [None, 7, 1, None, None, None, 8, 2, None]
        ], [  # 2, Sudoku.com Hard
            [None, None, 3, 6, None, None, None, None, 7],
            [None, None, None, None, None, None, None, 1, 5],
            [None, 5, None, None, 7, None, 6, 8, None],
            [None, None, 9, 8, None, None, None, None, None],
            [1, None, 2, None, None, 7, None, None, 8],
            [None, None, None, 1, None, 2, None, None, None],
            [None, 4, None, None, None, None, None, None, None],
            [7, None, None, None, None, None, 3, None, 9],
            [8, None, 1, None, None, 4, 2, None, None],
        ], [  # 3, Sudoku.com Hard
            [6, None, None, None, None, 2, 1, None, None],
            [None, 3, 2, 9, None, None, None, 7, None],
            [None, None, None, None, None, 8, None, None, None],
            [2, None, None, None, None, None, 4, None, None],
            [7, None, 3, None, None, None, 9, 1, None],
            [None, 8, None, None, 9, 4, None, None, None],
            [None, None, 4, None, None, None, 6, None, None],
            [1, 2, None, 7, None, None, None, None, 5],
            [None, None, None, None, None, None, None, 9, 4]
        ], [  # 4, Sudoku.com Hard
            [None, 4, None, None, None, 5, 6, None, 2],
            [None, None, None, 9, None, None, None, None, None],
            [None, None, None, None, None, 8, 5, 4, None],
            [None, 2, None, 6, None, None, 1, None, None],
            [None, 5, None, None, None, 2, 3, None, 6],
            [None, None, None, 3, None, 7, 2, 8, None],
            [7, 8, 3, 2, 6, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [6, None, 5, None, 7, 3, None, None, None]
        ], [  # 5, Sudoku.com Expert
            [None, None, 4, None, None, None, None, 5, None],
            [2, None, None, None, 5, 1, None, None, None],
            [9, None, None, None, None, None, 6, None, None],
            [None, None, None, 7, None, None, None, None, None],
            [None, 6, None, 3, None, None, None, 9, None],
            [None, 3, 7, None, 4, None, None, None, None],
            [None, None, None, None, None, 8, None, None, 4],
            [None, None, None, None, None, None, 7, 6, 3],
            [None, None, None, 2, None, 4, None, None, 9]
        ], [  # 6, Sudoku.com Expert
            [5, None, None, 4, None, None, None, None, None],
            [None, None, 2, None, None, None, None, None, 6],
            [None, None, 7, None, 8, 3, None, 5, None],
            [None, None, 5, None, None, None, None, 7, None],
            [None, None, None, None, 6, None, 8, 3, None],
            [None, None, None, 5, 9, None, None, 6, None],
            [9, 2, None, None, 7, None, None, None, None],
            [8, None, None, None, None, None, None, None, None],
            [4, None, 3, None, None, None, 1, None, None]
        ], [  # 7 Sudoku.com Expert
            [None, None, None, 7, 9, 8, None, None, None],
            [None, None, None, None, 1, None, 2, 5, None],
            [None, None, None, None, 2, None, 3, None, None],
            [7, None, 9, None, None, None, None, None, 2],
            [None, None, None, None, None, None, None, 7, None],
            [None, None, 8, None, None, 1, None, 9, None],
            [None, 5, None, None, None, None, 4, None, 6],
            [2, None, None, None, None, 6, None, None, None],
            [None, 1, None, 8, None, None, None, None, None]
        ], [  # 8, Sudoku.com Evil
            [None, None, None, None, None, 5, None, 9, None],
            [None, None, 6, 8, 9, None, None, None, 4],
            [8, None, None, None, None, 7, None, None, None],
            [None, 2, None, None, None, None, None, None, 6],
            [None, None, None, None, None, 9, None, None, None],
            [5, None, None, 3, 1, None, None, 4, None],
            [3, None, None, 4, 8, None, None, 1, None],
            [None, None, 5, None, None, None, 3, None, None],
            [None, None, None, 7, None, None, None, None, None],
        ],
    ]

    INVALID_SIZE_BOARD_ARGS = [
        [
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 9],
            [4, 5, 6, 7, 8, 9, 1, 2, 3, 3],
            [7, 8, 9, 1, 2, 3, 4, 5, 6, 6],
            [2, 3, 1, 5, 6, 4, 8, 9, 7, 7],
            [5, 6, 4, 8, 9, 7, 2, 3, 1, 1],
            [8, 9, 7, 2, 3, 1, 5, 6, 4, 4],
            [3, 1, 2, 6, 4, 5, 9, 7, 8, 8],
            [6, 4, 5, 9, 7, 8, 3, 1, 2, 2],
            [9, 7, 8, 3, 1, 2, 6, 4, 5, 5],
        ],
        [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [4, 5, 6, 7, 8, 9, 1, 2, 3],
            [7, 8, 9, 1, 2, 3, 4, 5, 6],
            [2, 3, 1, 5, 6, 4, 8, 9, 7],
            [5, 6, 4, 8, 9, 7, 2, 3, 1],
            [8, 9, 7, 2, 3, 1, 5, 6, 4],
            [3, 1, 2, 6, 4, 5, 9, 7, 8],
            [6, 4, 5, 9, 7, 8, 3, 1, 2],
            [9, 7, 8, 3, 1, 2, 6, 4, 5],
            [9, 7, 8, 3, 1, 2, 6, 4, 5],
        ],
        [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [4, 5, 6, 7, 8, 9, 1, 2, 3],
            [7, 8, 9, 1, 2, 3, 4, 5, 6],
            [2, 3, 1, 5, 6, 4, 8, 9, 7],
            [5, 6, 4, 8, 9, 7, 2, 3, 1],
            [8, 9, 7, 2, 3, 1, 5, 6, 4],
            [3, 1, 2, 6, 4, 5, 9, 7, 8],
            [6, 4, 5, 9, 7, 8, 3, 1, 2],
        ],
        [
            [1, 2, 3, 4, 5, 6, 7, 8],
            [4, 5, 6, 7, 8, 9, 1, 2],
            [7, 8, 9, 1, 2, 3, 4, 5],
            [2, 3, 1, 5, 6, 4, 8, 9],
            [5, 6, 4, 8, 9, 7, 2, 3],
            [8, 9, 7, 2, 3, 1, 5, 6],
            [3, 1, 2, 6, 4, 5, 9, 7],
            [6, 4, 5, 9, 7, 8, 3, 1],
            [9, 7, 8, 3, 1, 2, 6, 4],
        ],
        [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [4, 5, 6, 7, 8, 9, 1, 2, 3],
            [7, 8, 9, 1, 2, 3, 4, 5, 6],
            [2, 3, 1, 5, 6, 4, 8, 9, 7],
            [5, 6, 4, 8, 9, 7, 2, 3, 1],
            [8, 9, 7, 2, 3, 1, 5, 6, 4],
            [3, 1, 2, 6, 4, 5, 9, 7, 8],
            [6, 4, 5, 9, 7, 8, 3, 1, 2],
            [9, 7, 8, 3, 1, 2, 6, 4, 5],
        ],
        [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [4, 5, 6, 7, 8, 9, 1, 2, 3],
            [7, 8, 9, 1, 2, 3, 4, 5, 6],
            [2, 3, 1, 5, 6, 4, 8, 9, 7],
            [5, 6, 4, 8, 9, 7, 2, 3, 1, None],
            [8, 9, 7, 2, 3, 1, 5, 6, 4],
            [3, 1, 2, 6, 4, 5, 9, 7, 8],
            [6, 4, 5, 9, 7, 8, 3, 1, 2],
            [9, 7, 8, 3, 1, 2, 6, 4, 5],
        ],
        [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [4, 5, 6, 7, 8, 9, 1, 2, 3],
            [7, 8, 9, 1, 2, 3, 4, 5, 6],
            [2, 3, 1, 5, 6, 4, 8, 9, 7],
            [5, 6, 4, 8, 9, 7, 2, 3, 1],
            [None],
            [8, 9, 7, 2, 3, 1, 5, 6, 4],
            [3, 1, 2, 6, 4, 5, 9, 7, 8],
            [6, 4, 5, 9, 7, 8, 3, 1, 2],
            [9, 7, 8, 3, 1, 2, 6, 4, 5],
        ]
    ]

    INVALID_OUT_OF_RANGE_BOARD_ARGS = [
        [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [4, 5, 6, 7, 8, 9, 1, 2, 3],
            [7, 8, 9, 1, 2, 3, 4, 5, 6],
            [2, 3, 1, 5, 6, 4, 8, 9, 7],
            [5, 6, 4, 8, 9, 7, 2, 3, 1],
            [8, 9, 7, 2, 3, 1, 5, 6, 4],
            [3, 1, 10, 6, 4, 5, 9, 7, 8],
            [6, 4, 5, 9, 7, 8, 3, 1, 2],
            [9, 7, 8, 3, 1, 2, 6, 4, 5],
        ], [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [4, 5, 6, 7, 8, 9, 1, 2, 3],
            [7, 8, 9, -1, 2, 3, 4, 5, 6],
            [2, 3, 1, 5, 6, 4, 8, 9, 7],
            [5, 6, 4, 8, 9, 7, 2, 3, 1],
            [8, 9, 7, 2, 3, 1, 5, 6, 4],
            [3, 1, 2, 6, 4, 5, 9, 7, 8],
            [6, 4, 5, 9, 7, 8, 3, 1, 2],
            [9, 7, 8, 3, 1, 2, 6, 4, 5],
        ], [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [4, 5, 6, 7, 8, 9, 1, 2, 3],
            [7, 8, 9, 1, 2, 3, 4, 5, 6],
            [2, 3, 1, 5, 6, 4, 8, 9, 7],
            [5, 6, 4, 8, 9, 7, 2, 3, 1],
            [8, 9, 7, 2, 300, 1, 5, 6, 4],
            [3, 1, 2, 6, 4, 5, 9, 7, 8],
            [6, 4, 5, 9, 7, 8, 3, 1, 2],
            [9, 7, 8, 3, 1, 2, 6, 4, 5],
        ],
    ]

    INVALID_REPEATED_NUM_BOARD_ARGS = [
        [
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
        ], [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [4, 5, 6, 7, 8, 9, 1, 2, 3],
            [7, 8, 9, 1, 2, 3, 4, 5, 6],
            [2, 3, 1, 5, 6, 4, 8, 9, 7],
            [5, 6, 4, 8, 9, 9, 2, 3, 1],
            [8, 9, 7, 2, 3, 1, 5, 6, 4],
            [3, 1, 2, 6, 4, 5, 9, 7, 8],
            [6, 4, 5, 9, 7, 8, 3, 1, 2],
            [9, 7, 8, 3, 1, 2, 6, 4, 5],
        ]
    ]

    INVALID_TYPE_BOARD_ARGS = [
        [], {}, (),
        ['abc'], ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'],
        [
            ['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'i']
        ],
        [
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'],
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'],
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'],
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'],
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'],
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'],
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'],
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'],
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'],
        ],
        [1, 2, 3], [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            (),
            ()
        ],
        [
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {},
            {}
        ],
        [
            (1, 2, 3, 4, 5, 6, 7, 8, 9),
            (1, 2, 3, 4, 5, 6, 7, 8, 9),
            (1, 2, 3, 4, 5, 6, 7, 8, 9),
            (1, 2, 3, 4, 5, 6, 7, 8, 9),
            (1, 2, 3, 4, 5, 6, 7, 8, 9),
            (1, 2, 3, 4, 5, 6, 7, 8, 9),
            (1, 2, 3, 4, 5, 6, 7, 8, 9),
            (1, 2, 3, 4, 5, 6, 7, 8, 9),
            (1, 2, 3, 4, 5, 6, 7, 8, 9),
        ]
    ]

    VALID_BOARD_GROUPS = [
        (VALID_FULL_BOARD_ARGS[0], Group(GroupType.ROW, 0, [
            Cell(Position(0, 0), Value(1)),
            Cell(Position(0, 1), Value(2)),
            Cell(Position(0, 2), Value(3)),
            Cell(Position(0, 3), Value(4)),
            Cell(Position(0, 4), Value(5)),
            Cell(Position(0, 5), Value(6)),
            Cell(Position(0, 6), Value(7)),
            Cell(Position(0, 7), Value(8)),
            Cell(Position(0, 8), Value(9)),
        ])),
        (VALID_FULL_BOARD_ARGS[0], Group(GroupType.ROW, 4, [
            Cell(Position(4, 0), Value(5)),
            Cell(Position(4, 1), Value(6)),
            Cell(Position(4, 2), Value(4)),
            Cell(Position(4, 3), Value(8)),
            Cell(Position(4, 4), Value(9)),
            Cell(Position(4, 5), Value(7)),
            Cell(Position(4, 6), Value(2)),
            Cell(Position(4, 7), Value(3)),
            Cell(Position(4, 8), Value(1)),
        ])),
        (VALID_FULL_BOARD_ARGS[0], Group(GroupType.ROW, 8, [
            Cell(Position(8, 0), Value(9)),
            Cell(Position(8, 1), Value(7)),
            Cell(Position(8, 2), Value(8)),
            Cell(Position(8, 3), Value(3)),
            Cell(Position(8, 4), Value(1)),
            Cell(Position(8, 5), Value(2)),
            Cell(Position(8, 6), Value(6)),
            Cell(Position(8, 7), Value(4)),
            Cell(Position(8, 8), Value(5)),
        ])),
        (VALID_FULL_BOARD_ARGS[0], Group(GroupType.COL, 0, [
            Cell(Position(0, 0), Value(1)),
            Cell(Position(1, 0), Value(4)),
            Cell(Position(2, 0), Value(7)),
            Cell(Position(3, 0), Value(2)),
            Cell(Position(4, 0), Value(5)),
            Cell(Position(5, 0), Value(8)),
            Cell(Position(6, 0), Value(3)),
            Cell(Position(7, 0), Value(6)),
            Cell(Position(8, 0), Value(9)),
        ])),
        (VALID_FULL_BOARD_ARGS[0], Group(GroupType.COL, 4, [
            Cell(Position(0, 4), Value(5)),
            Cell(Position(1, 4), Value(8)),
            Cell(Position(2, 4), Value(2)),
            Cell(Position(3, 4), Value(6)),
            Cell(Position(4, 4), Value(9)),
            Cell(Position(5, 4), Value(3)),
            Cell(Position(6, 4), Value(4)),
            Cell(Position(7, 4), Value(7)),
            Cell(Position(8, 4), Value(1)),
        ])),
        (VALID_FULL_BOARD_ARGS[0], Group(GroupType.COL, 8, [
            Cell(Position(0, 8), Value(9)),
            Cell(Position(1, 8), Value(3)),
            Cell(Position(2, 8), Value(6)),
            Cell(Position(3, 8), Value(7)),
            Cell(Position(4, 8), Value(1)),
            Cell(Position(5, 8), Value(4)),
            Cell(Position(6, 8), Value(8)),
            Cell(Position(7, 8), Value(2)),
            Cell(Position(8, 8), Value(5)),
        ])),
        (VALID_FULL_BOARD_ARGS[0], Group(GroupType.BOX, 0, [
            Cell(Position(0, 0), Value(1)),
            Cell(Position(0, 1), Value(2)),
            Cell(Position(0, 2), Value(3)),
            Cell(Position(1, 0), Value(4)),
            Cell(Position(1, 1), Value(5)),
            Cell(Position(1, 2), Value(6)),
            Cell(Position(2, 0), Value(7)),
            Cell(Position(2, 1), Value(8)),
            Cell(Position(2, 2), Value(9)),
        ])),
        (VALID_FULL_BOARD_ARGS[0], Group(GroupType.BOX, 4, [
            Cell(Position(3, 3), Value(5)),
            Cell(Position(3, 4), Value(6)),
            Cell(Position(3, 5), Value(4)),
            Cell(Position(4, 3), Value(8)),
            Cell(Position(4, 4), Value(9)),
            Cell(Position(4, 5), Value(7)),
            Cell(Position(5, 3), Value(2)),
            Cell(Position(5, 4), Value(3)),
            Cell(Position(5, 5), Value(1)),
        ])),
        (VALID_FULL_BOARD_ARGS[0], Group(GroupType.BOX, 8, [
            Cell(Position(6, 6), Value(9)),
            Cell(Position(6, 7), Value(7)),
            Cell(Position(6, 8), Value(8)),
            Cell(Position(7, 6), Value(3)),
            Cell(Position(7, 7), Value(1)),
            Cell(Position(7, 8), Value(2)),
            Cell(Position(8, 6), Value(6)),
            Cell(Position(8, 7), Value(4)),
            Cell(Position(8, 8), Value(5)),
        ]))
    ]

    VALID_BOARD_SET_CELL = [
        (VALID_PARTIAL_BOARD_ARGS[0], Cell(Position(3, 3), Value(7))),
        (VALID_PARTIAL_BOARD_ARGS[0], Cell(Position(7, 6), Value(3))),
        (VALID_PARTIAL_BOARD_ARGS[0], Cell(Position(0, 0), Value(1))),
    ]

    INVALID_BOARD_SET_CELL = [
        (VALID_PARTIAL_BOARD_ARGS[0], Cell(Position(6, 2), Value(5))),
        (VALID_PARTIAL_BOARD_ARGS[0], Cell(Position(3, 4), Value(3))),
        (VALID_PARTIAL_BOARD_ARGS[0], Cell(Position(0, 0), Value(9))),
    ]