from sudoku_board import SudokuBoard


class SudokuPosition:

    def __init__(self, row_num, col_num):
        assert 0 <= row_num <= SudokuBoard.ROW_SIZE
        assert 0 <= col_num <= SudokuBoard.COL_SIZE
        self.row_num = row_num
        self.col_num = col_num

    def __eq__(self, other):
        return self.row_num == other.row_num and self.col_num == other.col_num

    def __hash__(self):
        return hash((self.row_num, self.col_num))

    def __str__(self):
        return f"(r: {self.row_num}, c: {self.col_num})"
