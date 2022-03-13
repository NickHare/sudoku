from sudoku.core.position import Position
from sudoku.core.value import Value


class CellCandidates:

    @staticmethod
    def validate_cell_candidate_args(pos: Position, candidate_values: list[Value]) -> None:
        assert candidate_values > 0
        assert sorted(candidate_values) == sorted(list(set(candidate_values)))

    def __init__(self, pos: Position, candidate_values: list[Value]) -> None:
        self.pos = pos
        self.candidate_values = candidate_values
        self.candidate_count = len(candidate_values)

    def is_single_candidate_cell(self) -> bool:
        return self.candidate_count == 1

    def get_single_candidate_value(self):
        return self.candidate_values[0] if self.is_single_candidate_cell() else None

    def remove_candidate_value(self, value: Value) -> bool:
        if value in self.candidate_values:
            assert self.candidate_count > 1
            self.candidate_values.remove(value)
            self.candidate_count -= 1

    def __contains__(self, item):
        return item in self.candidate_values

    def __str__(self) -> str:
        return f'{self.pos}: {self.candidate_values}'

    def __repr__(self) -> str:
        return self.__str__()
