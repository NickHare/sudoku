from sudoku_board import SudokuPosition

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