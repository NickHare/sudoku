from sudoku_board import SudokuBoard


class SudokuGroup:

    def __init__(self, group):
        assert isinstance(group, dict)

    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        return str(self.value) if self.value is not None else "?"