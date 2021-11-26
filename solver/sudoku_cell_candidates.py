from core.sudoku_cell import SudokuCell

class SudokuCellCandidates:

    def __init__(self, cell_candidates: list[bool]) -> None:
        self.cell_candidates = cell_candidates
        self.candidate_count = 0
        for value in SudokuCell.VALUE_NUM_RANGE:
            if self.cell_candidates[value]:
                self.candidate_count += 1
                self.single_candidate_cell = SudokuCell(value)
        assert self.candidate_count > 0
        self.cell_candidates[0] = True if self.candidate_count == 1 else False
        self.single_candidate_cell = self.single_candidate_cell if self.candidate_count == 1 else None

    def is_cell_candidate(self, cell: SudokuCell) -> bool:
        return self.cell_candidates[cell.value]

    def is_single_candidate_cell(self) -> bool:
        return self.candidate_count == 1 and self.cell_candidates[0]

    def __str__(self) -> str:
        return f'Cell Candidates: {[SudokuCell(value) for value in range(1, len(self.cell_candidates)) if self.cell_candidates[value]]}'

    def __repr__(self) -> str:
        return self.__str__()
