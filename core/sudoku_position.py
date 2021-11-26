import sudoku_config as config


class SudokuPosition:

    def __init__(self, row_num: int, col_num: int):
        assert 0 <= row_num < config.ROW_SIZE
        assert 0 <= col_num < config.COL_SIZE
        self.row_num = row_num
        self.col_num = col_num

    def __eq__(self, other: 'SudokuPosition') -> bool:
        return self.row_num == other.row_num and self.col_num == other.col_num

    def __hash__(self) -> int:
        return hash((self.row_num, self.col_num))

    def __str__(self) -> str:
        return f"(r: {self.row_num}, c: {self.col_num})"

    def __repr__(self) -> str:
        return self.__str__()
