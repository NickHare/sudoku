from enum import Enum

import sudoku.config as config
from sudoku.core.position import Position
from sudoku.core.value import Value
from sudoku.core.cell import Cell


class GroupType(Enum):
    ROW = 'Row'
    COL = 'Col'
    BOX = 'Box'

    def __str__(self):
        return self.value


class Group:
    GROUP_NUM_RANGE = range(config.SIZE)

    @staticmethod
    def pos_to_box_num(pos: Position) -> int:
        return (pos.row_num // config.BOX_SIZE) * config.BOX_SIZE + (pos.col_num // config.BOX_SIZE)

    @staticmethod
    def get_row_positions(row_num: int) -> list[Position]:
        assert 0 <= row_num < config.ROW_SIZE
        positions = []
        for c in range(config.COL_SIZE):
            positions.append(Position(row_num, c))
        return positions

    @staticmethod
    def get_col_positions(col_num: int) -> list[Position]:
        assert 0 <= col_num < config.COL_SIZE
        positions = []
        for r in range(config.ROW_SIZE):
            positions.append(Position(r, col_num))
        return positions

    @staticmethod
    def get_box_positions(box_num: int) -> list[Position]:
        assert 0 <= box_num < config.SIZE

        row_start = (box_num // config.BOX_SIZE) * config.BOX_SIZE
        col_start = (box_num % config.BOX_SIZE) * config.BOX_SIZE
        positions = []
        for r in range(config.BOX_SIZE):
            for c in range(config.BOX_SIZE):
                positions.append(Position(row_start + r, col_start + c))
        return positions

    def __init__(self, group_type: GroupType, group_num: int, group_cells: list[Cell]) -> None:
        assert 0 <= group_num < config.SIZE

        self.group_cells = group_cells
        self.group_type = group_type
        self.group_num = group_num

    def validate(self) -> bool:
        assert len(self.group_cells) == config.SIZE

        value_to_value_counts = dict([(val, 0) for val in Value.VALUE_RANGE])
        result = True

        for cell in self.group_cells:
            pos = cell.pos
            val = cell.val
            if self.group_type == GroupType.ROW:
                assert pos.row_num == self.group_num
            elif self.group_type == GroupType.COL:
                assert pos.col_num == self.group_num
            elif self.group_type == GroupType.BOX:
                assert self.pos_to_box_num(pos) == self.group_num

            if val.is_set():
                value_to_value_counts[val] += 1
                if value_to_value_counts[val] > 1:
                    result = False
        return result

    def get_cells(self) -> list[Cell]:
        return self.group_cells

    def get_set_cells(self) -> list[Cell]:
        return [cell for cell in self.group_cells if cell.is_set()]

    def get_empty_cells(self) -> list[Cell]:
        return [cell for cell in self.group_cells if cell.is_empty()]

    def is_value_in_group(self, value):
        result = False
        for cell in self.group_cells:
            if cell.val == value:
                result = True
                break
        return result

    def __str__(self) -> str:
        return f'{self.group_type} {self.group_num}: {self.get_cells()}'

    def __repr__(self) -> str:
        return self.__str__()
