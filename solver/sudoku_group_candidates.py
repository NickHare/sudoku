from core.sudoku_cell import SudokuCell
from core.sudoku_position import SudokuPosition


class SudokuGroupCandidates:

    def __init__(self, group_candidates: dict[SudokuCell, list[SudokuPosition]]) -> None:
        self.group_candidates = group_candidates
        self.single_candidates = {}
        for cell, positions in self.group_candidates.items():
            if len(positions) == 1:
                self.single_candidates[positions[0]] = cell

    def has_single_candidate_cells(self) -> bool:
        return len(self.single_candidates) > 0

    def __str__(self) -> str:
        return f'Group Candidates: {self.group_candidates}'

    def __repr__(self) -> str:
        return self.__str__()
