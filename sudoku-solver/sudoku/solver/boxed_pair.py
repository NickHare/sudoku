from sudoku.core.group_type import GroupType
from sudoku.core.group import Group
from sudoku.core.cell import Cell
from sudoku.core.value import Value
from sudoku.core.position import Position


class BoxedPair:

    @staticmethod
    def validate_boxed_pair_args(group_type: GroupType, group_num: int, positions: tuple[Position, Position], value: Value, eliminated_candidates: list[Cell]) -> None:
        assert group_type != GroupType.BOX
        assert Group.MIN_GROUP_NUM <= group_num <= Group.MAX_GROUP_NUM
        assert len(positions) == 2
        assert positions[0] != positions[1]
        assert Group.pos_to_box_num(positions[0]) == Group.pos_to_box_num(positions[1])
        assert positions[0].row_num == positions[1].row_num or positions[0].col_num == positions[1].col_num
        assert len(set(eliminated_candidates)) == len(eliminated_candidates)
        for candidate in eliminated_candidates:
            assert Group.pos_to_box_num(candidate.pos) == Group.pos_to_box_num(positions[0])
            assert candidate.pos not in positions
            assert candidate.val == value

    def __init__(self, group_type: GroupType, group_num: int, positions: tuple[Position, Position], value: Value, eliminated_candidates: list[Cell]) -> None:
        BoxedPair.validate_boxed_pair_args(group_type, group_num, positions, value, eliminated_candidates)
        self.group_type = group_type
        self.group_num = group_num
        self.positions = sorted(positions)
        self.value = value
        self.eliminated_candidates = sorted(eliminated_candidates)

    def __eq__(self, other):
        if not isinstance(other, BoxedPair):
            return False
        is_equal = self.group_type == other.group_type
        is_equal &= self.group_num == other.group_num
        is_equal &= sorted(self.positions) == sorted(other.positions)
        is_equal &= self.value == other.value
        return is_equal

    def __str__(self):
        return f'Boxed Pair - {self.group_type} {self.group_num} - {self.positions} - {self.value} - Removed Candidate Cells: {self.eliminated_candidates}'

    def __repr__(self):
        return self.__str__()
