from core.sudoku_board import SudokuPosition


EMPTY_BOARD = [
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

TEST_SUDOKU_BOARDS = [
    [  # Random Sheet Easy
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
    [  # Random Sheet Moderate
        [5, None, None, 1, None, None, None, None, None],
        [None, 3, None, None, None, 6, None, None, None],
        [None, None, None, 4, None, None, None, None, 7],
        [None, None, 4, None, 5, None, None, 8, None],
        [None, None, None, None, 4, None, 2, None, None],
        [None, 9, None, None, None, None, 3, None, None],
        [2, 4, None, None, None, 1, None, None, 6],
        [8, None, None, None, 6, None, 7, None, 1],
        [None, 7, 1, None, None, None, 8, 2, None]
    ], [  # Sudoku.com Hard
        [None, None, 3, 6, None, None, None, None, 7],
        [None, None, None, None, None, None, None, 1, 5],
        [None, 5, None, None, 7, None, 6, 8, None],
        [None, None, 9, 8, None, None, None, None, None],
        [1, None, 2, None, None, 7, None, None, 8],
        [None, None, None, 1, None, 2, None, None, None],
        [None, 4, None, None, None, None, None, None, None],
        [7, None, None, None, None, None, 3, None, 9],
        [8, None, 1, None, None, 4, 2, None, None],
    ], [  # Sudoku.com Hell
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
    [  # Sudoku.com Hard
        [6, None, None, None, None, 2, 1, None, None],
        [None, 3, 2, 9, None, None, None, 7, None],
        [None, None, None, None, None, 8, None, None, None],
        [2, None, None, None, None, None, 4, None, None],
        [7, None, 3, None, None, None, 9, 1, None],
        [None, 8, None, None, 9, 4, None, None, None],
        [None, None, 4, None, None, None, 6, None, None],
        [1, 2, None, 7, None, None, None, None, 5],
        [None, None, None, None, None, None, None, 9, 4]
    ], [  # Sudoku.com Hard
        [None, 4, None, None, None, 5, 6, None, 2],
        [None, None, None, 9, None, None, None, None, None],
        [None, None, None, None, None, 8, 5, 4, None],
        [None, 2, None, 6, None, None, 1, None, None],
        [None, 5, None, None, None, 2, 3, None, 6],
        [None, None, None, 3, None, 7, 2, 8, None],
        [7, 8, 3, 2, 6, None, None, None, None],
        [None, None, None, None, None, None, None, None, None],
        [6, None, 5, None, 7, 3, None, None, None]
    ], [  # Sudoku.com Expert
        [None, None, 4, None, None, None, None, 5, None],
        [2, None, None, None, 5, 1, None, None, None],
        [9, None, None, None, None, None, 6, None, None],
        [None, None, None, 7, None, None, None, None, None],
        [None, 6, None, 3, None, None, None, 9, None],
        [None, 3, 7, None, 4, None, None, None, None],
        [None, None, None, None, None, 8, None, None, 4],
        [None, None, None, None, None, None, 7, 6, 3],
        [None, None, None, 2, None, 4, None, None, 9]
    ], [  # Sudoku.com Expert
        [5, None, None, 4, None, None, None, None, None],
        [None, None, 2, None, None, None, None, None, 6],
        [None, None, 7, None, 8, 3, None, 5, None],
        [None, None, 5, None, None, None, None, 7, None],
        [None, None, None, None, 6, None, 8, 3, None],
        [None, None, None, 5, 9, None, None, 6, None],
        [9, 2, None, None, 7, None, None, None, None],
        [8, None, None, None, None, None, None, None, None],
        [4, None, 3, None, None, None, 1, None, None]
    ]
]

TEST_SUDOKU_BOARD_SOLUTIONS = [
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
    ], [  # Unknown Evil
    ],
    [
        [6, 5, 8, 4, 7, 2, 1, 3, 9],
        [4, 3, 2, 9, 5, 1, 8, 7, 6],
        [9, 1, 7, 6, 3, 8, 5, 4, 2],
        [2, 6, 9, 8, 1, 7, 4, 5, 3],
        [7, 4, 3, 2, 6, 5, 9, 1, 8],
        [5, 8, 1, 3, 9, 4, 2, 6, 7],
        [3, 7, 4, 5, 8, 9, 6, 2, 1],
        [1, 2, 9, 7, 4, 6, 3, 8, 5],
        [8, 6, 5, 1, 2, 3, 7, 9, 4]
    ], [
        [8, 4, 9, 1, 3, 5, 6, 7, 2],
        [5, 7, 2, 9, 4, 6, 8, 3, 1],
        [1, 3, 6, 7, 2, 8, 5, 4, 9],
        [3, 2, 8, 6, 9, 4, 1, 5, 7],
        [4, 5, 7, 8, 1, 2, 3, 9, 6],
        [9, 6, 1, 3, 5, 7, 2, 8, 4],
        [7, 8, 3, 2, 6, 9, 4, 1, 5],
        [2, 9, 4, 5, 8, 1, 7, 6, 3],
        [6, 1, 5, 4, 7, 3, 9, 2, 8]
    ], [  # Unknown Expert
    ]









]

TEST_SUDOKU_BOARD = [
    [4, 8, 5, 3, 1, 9, 7, 6, 2],
    [7, 9, 3, 6, 2, 4, 8, 1, 5],
    [2, 6, 1, 8, 7, 5, 4, 9, 3],
    [3, 1, 2, 7, 9, 6, 5, 8, 4],
    [6, 4, 8, 1, 5, 3, 2, 7, 9],
    [5, 7, 9, 2, 4, 8, 6, 3, 1],
    [8, 2, 6, 4, 3, 1, 9, 5, 7],
    [1, 5, 4, 9, 8, 7, 3, 2, 6],
    [9, 3, 7, 5, 6, 2, 1, 4, 8]
]

VALID_ROW_0_NONES = {
    SudokuPosition(0, 0): None,
    SudokuPosition(0, 1): None,
    SudokuPosition(0, 2): None,
    SudokuPosition(0, 3): None,
    SudokuPosition(0, 4): None,
    SudokuPosition(0, 5): None,
    SudokuPosition(0, 6): None,
    SudokuPosition(0, 7): None,
    SudokuPosition(0, 8): None,
}

VALID_ROW_0_BASIC_INC = {
    SudokuPosition(0, 0): 1,
    SudokuPosition(0, 1): 2,
    SudokuPosition(0, 2): 3,
    SudokuPosition(0, 3): 4,
    SudokuPosition(0, 4): 5,
    SudokuPosition(0, 5): 6,
    SudokuPosition(0, 6): 7,
    SudokuPosition(0, 7): 8,
    SudokuPosition(0, 8): 9,
}

VALID_ROW_0_BASIC_DEC = {
    SudokuPosition(0, 0): 9,
    SudokuPosition(0, 1): 8,
    SudokuPosition(0, 2): 7,
    SudokuPosition(0, 3): 6,
    SudokuPosition(0, 4): 5,
    SudokuPosition(0, 5): 4,
    SudokuPosition(0, 6): 3,
    SudokuPosition(0, 7): 2,
    SudokuPosition(0, 8): 1,
}

VALID_ROW_0_STAG_INC = {
    SudokuPosition(0, 0): 1,
    SudokuPosition(0, 1): 2,
    SudokuPosition(0, 2): 3,
    SudokuPosition(0, 3): 4,
    SudokuPosition(0, 4): 5,
    SudokuPosition(0, 5): 6,
    SudokuPosition(0, 6): 7,
    SudokuPosition(0, 7): 8,
    SudokuPosition(0, 8): 10,
}


ROW_0_POSITIONS = [
    SudokuPosition(0, 0),
    SudokuPosition(0, 1),
    SudokuPosition(0, 2),
    SudokuPosition(0, 3),
    SudokuPosition(0, 4),
    SudokuPosition(0, 5),
    SudokuPosition(0, 6),
    SudokuPosition(0, 7),
    SudokuPosition(0, 8),
]

ROW_8_POSITIONS = [
    SudokuPosition(8, 0),
    SudokuPosition(8, 1),
    SudokuPosition(8, 2),
    SudokuPosition(8, 3),
    SudokuPosition(8, 4),
    SudokuPosition(8, 5),
    SudokuPosition(8, 6),
    SudokuPosition(8, 7),
    SudokuPosition(8, 8),
]

COL_0_POSITIONS = [
    SudokuPosition(0, 0),
    SudokuPosition(1, 0),
    SudokuPosition(2, 0),
    SudokuPosition(3, 0),
    SudokuPosition(4, 0),
    SudokuPosition(5, 0),
    SudokuPosition(6, 0),
    SudokuPosition(7, 0),
    SudokuPosition(8, 0),
]

COL_8_POSITIONS = [
    SudokuPosition(0, 8),
    SudokuPosition(1, 8),
    SudokuPosition(2, 8),
    SudokuPosition(3, 8),
    SudokuPosition(4, 8),
    SudokuPosition(5, 8),
    SudokuPosition(6, 8),
    SudokuPosition(7, 8),
    SudokuPosition(8, 8),
]

BOX_0_POSITIONS = [
    SudokuPosition(0, 0),
    SudokuPosition(0, 1),
    SudokuPosition(0, 2),
    SudokuPosition(1, 0),
    SudokuPosition(1, 1),
    SudokuPosition(1, 2),
    SudokuPosition(2, 0),
    SudokuPosition(2, 1),
    SudokuPosition(2, 2),
]

BOX_8_POSITIONS = [
    SudokuPosition(6, 6),
    SudokuPosition(6, 7),
    SudokuPosition(6, 8),
    SudokuPosition(7, 6),
    SudokuPosition(7, 7),
    SudokuPosition(7, 8),
    SudokuPosition(8, 6),
    SudokuPosition(8, 7),
    SudokuPosition(8, 8),
]
