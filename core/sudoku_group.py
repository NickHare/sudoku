from enum import Enum

import sudoku_config as config
from core.sudoku_position import SudokuPosition
from core.sudoku_cell import SudokuCell


class SudokuGroupType(Enum):

    ROW = 'Row'
    COL = 'Col'
    BOX = 'Box'

    def __str__(self):
        return self.value


class SudokuGroup:

    GROUP_NUM_RANGE = range(config.SIZE)

    @staticmethod
    def pos_to_box_num(pos: SudokuPosition) -> int:
        return (pos.row_num // config.BOX_SIZE) * config.BOX_SIZE + (pos.col_num // config.BOX_SIZE)

    @staticmethod
    def get_row_positions(row_num: int) -> list[SudokuPosition]:
        assert 0 <= row_num < config.ROW_SIZE
        positions = []
        for c in range(config.COL_SIZE):
            positions.append(SudokuPosition(row_num, c))
        return positions

    @staticmethod
    def get_col_positions(col_num: int) -> list[SudokuPosition]:
        assert 0 <= col_num < config.COL_SIZE
        positions = []
        for r in range(config.ROW_SIZE):
            positions.append(SudokuPosition(r, col_num))
        return positions

    @staticmethod
    def get_box_positions(box_num: int) -> list[SudokuPosition]:
        assert 0 <= box_num < config.SIZE

        row_start = (box_num // config.BOX_SIZE) * config.BOX_SIZE
        col_start = (box_num % config.BOX_SIZE) * config.BOX_SIZE
        positions = []
        for r in range(config.BOX_SIZE):
            for c in range(config.BOX_SIZE):
                positions.append(SudokuPosition(row_start + r, col_start + c))
        return positions

    def __init__(self, group_type: SudokuGroupType, group_num: int, group: dict[SudokuPosition, SudokuCell]) -> None:
        assert 0 <= group_num < config.SIZE

        self.group = group
        self.group_type = group_type
        self.group_num = group_num

    def validate(self) -> bool:
        assert len(self.group.keys()) == config.SIZE, f'SudokuGroup group have MAX SIZE number of keys. len(group): {len(self.group)}'
        assert isinstance(self.group_type, SudokuGroupType), f'SudokuGroup group_type must be of type SudokuGroupType. type(group_type): {type(self.group_type)}'
        assert isinstance(self.group_num, int) and 0 <= self.group_num < config.SIZE, f'SudokuGroup group_num must be int between 0 and the MAX SIZE. group_num: {self.group_num}'

        value_counts = [0]*(config.SIZE + 1)
        result = True

        for pos, cell in self.group.items():
            assert isinstance(pos, SudokuPosition)
            assert isinstance(cell, SudokuCell)

            if self.group_type == SudokuGroupType.ROW:
                assert pos.row_num == self.group_num
            elif self.group_type == SudokuGroupType.COL:
                assert pos.col_num == self.group_num
            elif self.group_type == SudokuGroupType.BOX:
                assert self.pos_to_box_num(pos) == self.group_num

            if cell.is_set():
                value_counts[cell.value] += 1
                if value_counts[cell.value] > 1:
                    result = False
        return result

    def get_cells(self) -> list[SudokuCell]:
        return list(self.group.values())

    def get_positions(self):
        return list(self.group.keys())

    def get_items(self):
        return list(self.group.items())

    def __str__(self) -> str:
        return f'{self.group_type} {self.group_num}: {self.get_cells()}'

    def __repr__(self) -> str:
        return self.__str__()
