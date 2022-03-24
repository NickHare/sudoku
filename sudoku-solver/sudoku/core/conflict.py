from sudoku.config import Config
from sudoku.core.group_type import GroupType
from sudoku.core.value import Value
from sudoku.core.position import Position


class Conflict:

    @staticmethod
    def validate_conflict_args(group_type: GroupType, group_num: int, conflict_value: Value, conflict_positions: list[Position]):
        assert 0 <= group_num < Config.SIZE
        assert len(conflict_positions) >= 2
        for i in range(len(conflict_positions)):
            assert conflict_positions[i] not in conflict_positions[i+1:]

    def __init__(self, group_type: GroupType, group_num: int, conflict_value: Value, conflict_positions: list[Position]):
        Conflict.validate_conflict_args(group_type, group_num, conflict_value, conflict_positions)
        self.group_type = group_type
        self.group_num = group_num
        self.value = conflict_value
        self.positions = sorted(conflict_positions)

    def __eq__(self, other: 'Conflict') -> bool:
        is_equal = True
        if self.group_type != other.group_type:
            is_equal = False
        if self.group_num != other.group_num:
            is_equal = False
        if self.value != other.value:
            is_equal = False
        if sorted(self.positions) != sorted(other.positions):
            is_equal = False
        return is_equal

    def __str__(self):
        return f'{self.group_type} {self.group_num} - {self.value}: {self.positions}'

    def __repr__(self) -> str:
        return self.__str__()
