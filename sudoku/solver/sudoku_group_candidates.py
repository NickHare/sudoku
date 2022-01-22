from core.sudoku_value import Value
from core.sudoku_position import SudokuPosition


class SudokuGroupCandidates:

    def __init__(self, group_candidates: dict[SudokuValue, list[SudokuPosition]]) -> None:
        self.group_candidates = group_candidates
        self.group_candidate_counts = self.count_group_candidates()

    def count_group_candidates(self):
        candidate_counts = {}
        for val, pos in self.group_candidates.items():
            candidate_count = len(pos)
            if candidate_count not in candidate_counts:
                candidate_counts[candidate_count] = []
            candidate_counts[candidate_count].append(val)
        return candidate_counts

    def get_group_candidate_values_for_count(self, count: int) -> list[SudokuValue]:
        return self.group_candidate_counts[count] if count in self.group_candidate_counts else []

    def get_group_candidate_positions_for_value(self, value: SudokuValue) -> list[SudokuPosition]:
        return [pos for pos in self.group_candidates[value]] if value in self.group_candidates else []

    def remove_group_candidate(self, pos: SudokuPosition, val: SudokuValue):
        if val in self.group_candidates.keys():
            if pos in self.group_candidates[val]:
                self.group_candidates[val].remove(pos)

        for count in self.group_candidate_counts:
            if val in self.group_candidate_counts[count]:
                self.group_candidate_counts[count].remove(val)
                old_count = count

        if old_count > 1:
            new_count = old_count - 1
            if new_count not in self.group_candidate_counts:
                self.group_candidate_counts[new_count] = []
            self.group_candidate_counts[new_count].append(val)

    def __str__(self) -> str:
        return f'Group Candidates: {self.group_candidates}, Candidate Counts: {self.group_candidate_counts}'

    def __repr__(self) -> str:
        return self.__str__()
