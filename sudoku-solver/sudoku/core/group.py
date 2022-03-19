from sudoku.config import Config
from sudoku.core.group_type import GroupType
from sudoku.core.conflict import Conflict
from sudoku.core.position import Position
from sudoku.core.value import Value
from sudoku.core.cell import Cell


class Group:
    MIN_GROUP_NUM = 0
    MAX_GROUP_NUM = Config.SIZE - 1
    GROUP_NUM_RANGE = list(range(Config.SIZE))

    @staticmethod
    def get_row_positions(row_num: int) -> list[Position]:
        assert Group.MIN_GROUP_NUM <= row_num <= Group.MAX_GROUP_NUM
        positions = []
        for c in range(Config.COL_SIZE):
            positions.append(Position(row_num, c))
        return positions

    @staticmethod
    def get_col_positions(col_num: int) -> list[Position]:
        assert Group.MIN_GROUP_NUM <= col_num <= Group.MAX_GROUP_NUM
        positions = []
        for r in range(Config.ROW_SIZE):
            positions.append(Position(r, col_num))
        return positions

    @staticmethod
    def get_box_positions(box_num: int) -> list[Position]:
        assert Group.MIN_GROUP_NUM <= box_num <= Group.MAX_GROUP_NUM
        row_start = (box_num // Config.BOX_SIZE) * Config.BOX_SIZE
        col_start = (box_num % Config.BOX_SIZE) * Config.BOX_SIZE
        positions = []
        for r in range(Config.BOX_SIZE):
            for c in range(Config.BOX_SIZE):
                positions.append(Position(row_start + r, col_start + c))
        return positions

    @staticmethod
    def pos_to_box_num(pos: Position) -> int:
        return (pos.row_num // Config.BOX_SIZE) * Config.BOX_SIZE + pos.col_num // Config.BOX_SIZE

    @staticmethod
    def validate_group_args(group_type: GroupType, group_num: int, group_cells: list[Cell]) -> None:
        assert isinstance(group_num, int)
        assert isinstance(group_cells, list)

        assert Group.MIN_GROUP_NUM <= group_num <= Group.MAX_GROUP_NUM
        assert len(group_cells) == Config.SIZE
        assert len(set(group_cells)) == len(group_cells)

        position_counts = {}
        for cell in group_cells:
            assert isinstance(cell, Cell)

            pos = cell.pos
            if group_type == GroupType.ROW:
                assert pos.row_num == group_num
            elif group_type == GroupType.COL:
                assert pos.col_num == group_num
            elif group_type == GroupType.BOX:
                assert Group.pos_to_box_num(pos) == group_num

            if pos not in position_counts:
                position_counts[pos] = 0
            position_counts[pos] += 1

        for pos in position_counts:
            assert position_counts[pos] <= 1

    def __init__(self, group_type: GroupType, group_num: int, group_cells: list[Cell]) -> None:
        Group.validate_group_args(group_type, group_num, group_cells)
        self.type = group_type
        self.num = group_num
        self.cells = sorted(group_cells)
        self.conflicts = self.gather_conflicts()

    def gather_conflicts(self) -> list[Conflict]:
        conflicts = []
        value_to_positions = {}
        for cell in self.cells:
            val = cell.val
            pos = cell.pos
            if val.is_set():
                if val not in value_to_positions:
                    value_to_positions[val] = []
                value_to_positions[val].append(pos)

        for val in Value.VALUE_RANGE:
            if val in value_to_positions and len(value_to_positions[val]) >= 2:
                conflicts.append(Conflict(self.type, self.num, val, value_to_positions[val]))

        return conflicts

    def get_set_cells(self) -> list[Cell]:
        return [cell for cell in self.cells if cell.is_set()]

    def get_empty_cells(self) -> list[Cell]:
        return [cell for cell in self.cells if cell.is_empty()]

    def is_value_in_group(self, value: Value) -> bool:
        result = False
        for cell in self.cells:
            if cell.val == value:
                result = True
                break
        return result

    def has_conflicts(self) -> bool:
        return self.conflicts != []

    def __str__(self) -> str:
        return f'{self.type} {self.num}: {self.cells}'

    def __repr__(self) -> str:
        return self.__str__()
