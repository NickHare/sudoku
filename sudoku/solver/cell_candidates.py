from sudoku.core.value import Value


class CellCandidates:

    def __init__(self, cell_candidates: list[bool]) -> None:
        self.candidates = cell_candidates
        self.candidate_counts = 0
        for value_index in Value.NUM_RANGE:
            if self.candidates[value_index]:
                value = Value(value_index)
                self.candidate_counts += 1
                self.single_candidate_value = value
        assert self.candidate_counts > 0
        self.candidates[0] = True if self.candidate_counts == 1 else False
        self.single_candidate_value = self.single_candidate_value if self.candidate_counts == 1 else None

    def is_candidate_value(self, value: Value) -> bool:
        value_index = value.num
        return self.candidates[value_index]

    def is_single_candidate_cell(self) -> bool:
        return self.candidate_counts == 1 and self.candidates[0]

    def get_candidate_values(self) -> list[Value]:
        return [Value(num) for num in Value.NUM_RANGE if self.candidates[num]]

    def remove_candidate_value(self, value: Value) -> bool:
        assert self.candidate_counts >= 1
        is_removed = False
        if self.candidates[value.num]:
            self.candidate_counts -= 1
            self.candidates[value.num] = False
            is_removed = True

            if self.candidate_counts == 1:
                self.candidates[0] = True
                for num in Value.NUM_RANGE:
                    if self.candidates[num]:
                        self.single_candidate_value = Value(num)
        return is_removed

    def __str__(self) -> str:
        return f'Cell Candidates: {[Value(num) for num in Value.NUM_RANGE if self.candidates[num]]}'

    def __repr__(self) -> str:
        return self.__str__()
