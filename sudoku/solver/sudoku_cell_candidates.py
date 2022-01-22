from core.sudoku_value import SudokuValue


class SudokuCellCandidates:

    def __init__(self, cell_candidates: list[bool]) -> None:
        self.cell_candidates = cell_candidates
        self.candidate_count = 0
        for value_index in SudokuValue.NUM_RANGE:
            if self.cell_candidates[value_index]:
                value = SudokuValue(value_index)
                self.candidate_count += 1
                self.single_candidate_value = value
        assert self.candidate_count > 0
        self.cell_candidates[0] = True if self.candidate_count == 1 else False
        self.single_candidate_value = self.single_candidate_value if self.candidate_count == 1 else None

    def is_candidate_value(self, value: SudokuValue) -> bool:
        value_index = value.num
        return self.cell_candidates[value_index]

    def is_single_candidate_cell(self) -> bool:
        return self.candidate_count == 1 and self.cell_candidates[0]

    def get_candidate_values(self) -> list[SudokuValue]:
        return [SudokuValue(num) for num in SudokuValue.NUM_RANGE if self.cell_candidates[num]]

    def remove_candidate_value(self, value: SudokuValue) -> bool:
        assert self.candidate_count >= 1
        is_removed = self.cell_candidates[value.num]
        if is_removed:
            self.candidate_count -= 1

        self.cell_candidates[value.num] = False
        return is_removed

    def __str__(self) -> str:
        return f'Cell Candidates: {[SudokuValue(value) for value in range(1, len(self.cell_candidates)) if self.cell_candidates[value]]}'

    def __repr__(self) -> str:
        return self.__str__()
