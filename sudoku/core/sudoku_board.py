import sudoku_config as config
from core.sudoku_position import SudokuPosition
from core.sudoku_value import SudokuValue
from core.sudoku_cell import SudokuCell
from core.sudoku_group import SudokuGroup
from core.sudoku_group import SudokuGroupType


class SudokuBoard:

    @classmethod
    def board_from_numbers(cls, num_board: list[int]):
        assert len(num_board) == config.ROW_SIZE
        for row in num_board:
            assert len(row) == config.COL_SIZE

        board = [[SudokuCell(SudokuPosition(row, col), SudokuValue(num_board[row][col])) for col in range(config.COL_SIZE)] for row in range(config.ROW_SIZE)]
        return cls(board)

    def __init__(self, board: list[SudokuCell]):
        assert len(board) == config.ROW_SIZE
        for row in board:
            assert len(row) == config.COL_SIZE

        self.board = board
        self.valid = self.validate_board()
        assert self.valid

    def get_row(self, row_num: int) -> SudokuGroup:
        assert 0 <= row_num < config.ROW_SIZE
        return self.get_sudoku_group(SudokuGroupType.ROW, row_num)

    def get_col(self, col_num: int) -> SudokuGroup:
        assert 0 <= col_num < config.COL_SIZE
        return self.get_sudoku_group(SudokuGroupType.COL, col_num)

    def get_box(self, box_num: int) -> SudokuGroup:
        assert 0 <= box_num < config.SIZE
        return self.get_sudoku_group(SudokuGroupType.BOX, box_num)

    def get_sudoku_group(self, group_type: SudokuGroupType, group_num: int) -> SudokuGroup:
        assert 0 <= group_num < config.SIZE
        pos_list = []

        if group_type == SudokuGroupType.ROW:
            pos_list = SudokuGroup.get_row_positions(group_num)
        elif group_type == SudokuGroupType.COL:
            pos_list = SudokuGroup.get_col_positions(group_num)
        elif group_type == SudokuGroupType.BOX:
            pos_list = SudokuGroup.get_box_positions(group_num)

        group_cells = []
        for pos in pos_list:
            group_cells.append(self.board[pos.row_num][pos.col_num])

        return SudokuGroup(group_type, group_num, group_cells)

    def get_cell(self, pos: SudokuPosition) -> SudokuCell:
        return self.board[pos.row_num][pos.col_num]

    def set_cell(self, cell: SudokuCell) -> bool:
        is_set = True
        val = cell.val
        pos = cell.pos
        current_cell = self.get_cell(pos)
        if val.is_empty() or current_cell.is_set():
            is_set = False
        else:
            row = self.get_row(pos.row_num)
            col = self.get_col(pos.col_num)
            box = self.get_box(SudokuGroup.pos_to_box_num(pos))
            if cell in row.get_cells() or cell in col.get_cells() or cell in box.get_cells():
                is_set = False
        if is_set:
            self.board[pos.row_num][pos.col_num] = cell
        return is_set

    def is_completed(self) -> bool:
        is_completed = True
        for row in self.board:
            for cell in row:
                if cell.is_empty():
                    is_completed = False
                    break
        return is_completed

    def validate_board(self) -> bool:
        valid = True
        num = 0
        while valid and num < config.SIZE:
            row = self.get_row(num)
            col = self.get_col(num)
            box = self.get_box(num)
            if not row.validate() or not col.validate() or not box.validate():
                valid = False
            num += 1
        return valid

    def __str__(self) -> str:
        result = '  - - -SudokuBoard- - - \n'
        for n in range(config.BOX_SIZE):
            for m in range(config.BOX_SIZE):
                row = self.get_row(n*config.BOX_SIZE + m)
                values = [cell.val for cell in row.get_cells()]
                values.insert(0, '|')
                values.insert(4, '|')
                values.insert(8, '|')
                values.insert(12, '|')
                result += (' '.join([str(val) for val in values]) + '\n')
            result += '  - - -   - - -   - - - \n'

        return result
