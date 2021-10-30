from sudoku_board import SudokuBoard


class SudokuValue:

    def __init__(self, value):
        assert value is None or 1 <= value <= SudokuBoard.SIZE
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        return str(self.value) if self.value is not None else "?"