from sudoku.core.cell import Cell
from sudoku.core.value import Value
from sudoku.core.position import Position


class GroupCandidates:

    def __init__(self, group_candidates: dict[Value, list[Position]]) -> None:
        self.candidates = group_candidates
        self.candidate_counts = self.gather_candidate_counts()

    def gather_candidate_counts(self):
        candidate_counts = {}
        for val, pos in self.candidates.items():
            candidate_count = len(pos)
            if candidate_count not in candidate_counts:
                candidate_counts[candidate_count] = []
            candidate_counts[candidate_count].append(val)
        return candidate_counts

    def get_candidate_values_for_count(self, count: int) -> list[Value]:
        return self.candidate_counts[count] if count in self.candidate_counts else []

    def get_positions_for_candidate_value(self, value: Value) -> list[Position]:
        return [pos for pos in self.candidates[value]] if value in self.candidates else []

    def remove_group_candidate(self, cell: Cell):
        pos = cell.pos
        val = cell.val
        if val in self.candidates and pos in self.candidates[val]:
            self.candidates[val].remove(pos)

            for count in self.candidate_counts:
                if val in self.candidate_counts[count]:
                    old_count = count
                    self.candidate_counts[count].remove(val)

            assert old_count >= 1
            if old_count > 1:
                new_count = old_count - 1
                if new_count not in self.candidate_counts:
                    self.candidate_counts[new_count] = []
                self.candidate_counts[new_count].append(val)

    def __str__(self) -> str:
        return f'Group Candidates: {self.candidates}, Candidate Counts: {self.candidate_counts}'

    def __repr__(self) -> str:
        return self.__str__()
