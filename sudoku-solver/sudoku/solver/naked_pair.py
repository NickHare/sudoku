from sudoku.core.group_type import GroupType
from sudoku.core.group import Group
from sudoku.core.cell import Cell
from sudoku.core.value import Value
from sudoku.core.position import Position


class NakedPair:

    @staticmethod
    def validate_naked_pair_args(group_type: GroupType, group_num: int, positions: tuple[Position, Position], values: tuple[Value, Value], eliminated_candidates: list[Cell]) -> None:
        assert Group.MIN_GROUP_NUM <= group_num <= Group.MAX_GROUP_NUM
        assert len(positions) == 2
        assert len(values) == 2
        assert positions[0] != positions[1]
        assert values[0] != values[1]
        assert len(set(eliminated_candidates)) == len(eliminated_candidates)
        for candidate in eliminated_candidates:
            assert candidate.pos not in positions
            assert candidate.val in values

    def __init__(self, group_type: GroupType, group_num: int, positions: tuple[Position, Position], values: tuple[Value, Value], eliminated_candidates: list[Cell]) -> None:
        NakedPair.validate_naked_pair_args(group_type, group_num, positions, values, eliminated_candidates)
        self.group_type = group_type
        self.group_num = group_num
        self.positions = sorted(positions)
        self.values = sorted(values)
        self.eliminated_candidates = sorted(eliminated_candidates)

    def __eq__(self, other):
        if not isinstance(other, NakedPair):
            return False
        is_equal = self.group_type == other.group_type
        is_equal &= self.group_num == other.group_num
        is_equal &= sorted(self.positions) == sorted(other.positions)
        is_equal &= sorted(self.values) == sorted(other.values)
        return is_equal

    def __str__(self):
        return f'Naked Pair - {self.group_type} {self.group_num} - {self.positions} - {self.values} - Removed Candidate Cells: {self.eliminated_candidates}'

    def __repr__(self):
        return self.__str__()
