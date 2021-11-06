from sudoku_board import SudokuBoard


class SudokuPosition:

    def __init__(self, row_num, col_num):
        assert 0 <= row_num <= SudokuBoard.ROW_SIZE
        assert 0 <= col_num <= SudokuBoard.COL_SIZE
        self.row_num = row_num
        self.col_num = col_num

    @staticmethod
    def get_row_positions(row_num):
        assert 0 <= row_num <= SudokuBoard.ROW_SIZE
        values = []
        for c in range(SudokuBoard.COL_SIZE):
            values.append = (row_num, c)
        return values

    @staticmethod
    def get_col_positions(col_num):
        assert 0 <= col_num <= SudokuBoard.COL_SIZE
        values = []
        for r in range(SudokuBoard.ROW_SIZE):
            values.append = (r, col_num)
        return values

    @staticmethod
    def get_box_positions(box_num):
        assert 0 <= box_num <= SudokuBoard.SIZE

        row_start = (box_num // SudokuBoard.BOX_SIZE) * SudokuBoard.BOX_SIZE
        col_start = (box_num % SudokuBoard.BOX_SIZE) * SudokuBoard.BOX_SIZE
        values = []
        for r in range(SudokuBoard.BOX_SIZE):
            for c in range(SudokuBoard.BOX_SIZE):
                values.append = (row_start + r, col_start + c)
        return values

    def __eq__(self, other):
        return self.row_num == other.row_num and self.col_num == other.col_num

    def __hash__(self):
        return hash((self.row_num, self.col_num))

    def __str__(self):
        return f"(r: {self.row_num}, c: {self.col_num})"
