from sudoku.config import Config


class Position:

    MIN_ROW = 0
    MIN_COL = 0
    MAX_ROW = Config.ROW_SIZE - 1
    MAX_COL = Config.COL_SIZE - 1
    ROW_RANGE = list(range(Config.ROW_SIZE))
    COL_RANGE = list(range(Config.COL_SIZE))

    @staticmethod
    def validate_position_args(row_num: int, col_num: int) -> None:
        assert isinstance(row_num, int)
        assert isinstance(col_num, int)
        assert Position.MIN_ROW <= row_num <= Position.MAX_ROW
        assert Position.MIN_COL <= col_num <= Position.MAX_COL

    def __init__(self, row_num: int, col_num: int) -> None:
        Position.validate_position_args(row_num, col_num)
        self.row_num = row_num
        self.col_num = col_num

    def __eq__(self, other: 'Position') -> bool:
        return self.row_num == other.row_num and self.col_num == other.col_num

    def __lt__(self, other: 'Position') -> bool:
        return self.row_num < other.row_num or (self.row_num == other.row_num and self.col_num < other.col_num)

    def __hash__(self) -> int:
        return hash((self.row_num, self.col_num))

    def __str__(self) -> str:
        return f"({self.row_num}, {self.col_num})"

    def __repr__(self) -> str:
        return self.__str__()
