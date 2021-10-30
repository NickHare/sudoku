from sudoku_position import SudokuPosition


class SudokuBoard:
    SIZE = 9
    ROW_SIZE = 9
    COL_SIZE = 9
    BOX_SIZE = 3

    def __init__(self, board: list):
        self.board = board
        assert self.validate_board()

    def get_row(self, row_num):
        assert 0 <= row_num < self.ROW_SIZE

        values = {}
        for c in range(self.COL_SIZE):
            values[SudokuPosition(row_num, c)] = self.board[row_num][c]
        return values

    def get_col(self, col_num):
        assert 0 <= col_num < self.COL_SIZE

        values = {}
        for r in range(self.ROW_SIZE):
            values[SudokuPosition(r, col_num)] = self.board[r][col_num]
        return values

    def get_box(self, box_num):
        assert 0 <= box_num < self.SIZE
        row_start = (box_num // self.BOX_SIZE) * self.BOX_SIZE
        col_start = (box_num % self.BOX_SIZE) * self.BOX_SIZE

        values = {}
        for r in range(self.BOX_SIZE):
            for c in range(self.BOX_SIZE):
                values[SudokuPosition(r, c)] = self.board[row_start + r][col_start + c]
        return values

    def get_cell(self, row_num, col_num):
        assert 0 <= row_num < self.ROW_SIZE
        assert 0 <= col_num < self.COL_SIZE
        return self.board[row_num][col_num]

    def get_cell_from_pos(self, pos: SudokuPosition):
        return self.get_cell(pos.row_num, pos.col_num)

    def set_cell(self, row_num, col_num):
        pass

    def validate_board(self):
        valid = True
        for num in range(self.SIZE):
            row = self.get_row(num)
            col = self.get_col(num)
            box = self.get_box(num)
            if valid and not self.validate_values(row):
                valid = False
            if valid and not self.validate_values(col):
                valid = False
            if valid and not self.validate_values(box):
                valid = False
        return valid

    @classmethod
    def validate_values(cls, values):
        assert values is not None
        assert isinstance(values, dict)
        assert len(values) == cls.SIZE

        value_counts = [0]*9
        result = True

        for pos, value in values.items():
            assert value is None or (isinstance(value, int) and 1 <= value <= cls.SIZE)
            if value is not None:
                value_counts[value-1] += 1
                if value_counts[value-1] > 1:
                    result = False
                    break
        return result

    @classmethod
    def row_col_to_box_num(cls, row_num, col_num):
        assert 0 <= row_num < cls.ROW_SIZE
        assert 0 <= col_num < cls.COL_SIZE
        return (row_num // cls.BOX_SIZE) * cls.BOX_SIZE + (col_num // cls.BOX_SIZE)

    @classmethod
    def pos_to_box_num(cls, pos):
        assert type(pos) in ('tuple', 'list') and len(pos) >= 2
        return (pos.row_num // cls.BOX_SIZE) * cls.BOX_SIZE + (pos.col_num // cls.BOX_SIZE)

    def __deepcopy__(self, obj):
        board_copy = []
        for row in self.board:
            row_copy = []
            for cell in row:
                row_copy.append(cell)
            board_copy.append(row_copy)
        return board_copy

