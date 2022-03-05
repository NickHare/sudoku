from sudoku.config import Config
from sudoku.core.position import Position
from sudoku.core.value import Value
from sudoku.core.cell import Cell
from sudoku.core.group_type import GroupType
from sudoku.core.group import Group


class Board:

    @staticmethod
    def validate_board_args(num_board: list[int]) -> None:
        assert isinstance(num_board, list)
        assert len(num_board) == Config.ROW_SIZE
        for row in num_board:
            assert isinstance(row, list)
            assert len(row) == Config.COL_SIZE

        for r in Position.ROW_RANGE:
            for c in Position.COL_RANGE:
                assert num_board[r][c] is None or isinstance(num_board[r][c], int)
                assert num_board[r][c] is None or Value.MIN_NUM <= num_board[r][c] <= Value.MAX_NUM

    def __init__(self, num_board: list[int]):
        Board.validate_board_args(num_board)
        self.board = num_board
        self.rows, self.cols, self.boxes = self.gather_groups()
        self.conflicts = self.gather_conflicts()

    def gather_groups(self):
        rows = [self.gather_group(GroupType.ROW, group_num) for group_num in Group.GROUP_NUM_RANGE]
        cols = [self.gather_group(GroupType.COL, group_num) for group_num in Group.GROUP_NUM_RANGE]
        boxes = [self.gather_group(GroupType.BOX, group_num) for group_num in Group.GROUP_NUM_RANGE]
        return rows, cols, boxes

    def gather_group(self, group_type: GroupType, group_num: int) -> Group:
        assert Group.MIN_GROUP_NUM <= group_num <= Group.MAX_GROUP_NUM

        pos_list = []
        if group_type == GroupType.ROW:
            pos_list = Group.get_row_positions(group_num)
        elif group_type == GroupType.COL:
            pos_list = Group.get_col_positions(group_num)
        elif group_type == GroupType.BOX:
            pos_list = Group.get_box_positions(group_num)
        group_cells = [Cell(pos, Value(self.board[pos.row_num][pos.col_num])) for pos in pos_list]

        return Group(group_type, group_num, group_cells)

    def gather_conflicts(self):
        conflicts = []
        for group_num in Group.GROUP_NUM_RANGE:
            row = self.rows[group_num]
            col = self.cols[group_num]
            box = self.boxes[group_num]
            for conflict in row.conflicts + col.conflicts + box.conflicts:
                conflicts.append(conflict)
        return conflicts

    def get_cell(self, pos: Position) -> Cell:
        return Cell(pos, Value(self.board[pos.row_num][pos.col_num]))

    def set_cell(self, cell: Cell) -> None:
        val = cell.val
        pos = cell.pos

        self.board[pos.row_num][pos.col_num] = val.num
        self.rows[pos.row_num] = self.gather_group(GroupType.ROW, pos.row_num)
        self.cols[pos.col_num] = self.gather_group(GroupType.COL, pos.col_num)
        box_num = Group.pos_to_box_num(pos)
        self.boxes[box_num] = self.gather_group(GroupType.BOX, box_num)
        self.conflicts = self.gather_conflicts()

    def is_completed(self) -> bool:
        is_completed = self.conflicts == []
        for row in self.board:
            for num in row:
                val = Value(num)
                if val.is_empty():
                    is_completed = False
                    break
        return is_completed

    def __str__(self) -> str:
        result = '  - - -SudokuBoard- - - \n'
        for n in range(Config.BOX_SIZE):
            for m in range(Config.BOX_SIZE):
                row = self.board[n * Config.BOX_SIZE + m]
                values = [Value(num) for num in row]
                values.insert(0, '|')
                values.insert(4, '|')
                values.insert(8, '|')
                values.insert(12, '|')
                result += (' '.join([str(val) for val in values]) + '\n')
            result += '  - - -   - - -   - - - \n'

        return result

    def __repr__(self) -> str:
        return self.__str__()
