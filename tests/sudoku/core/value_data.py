from sudoku.core.value import Value


class ValueData:
    INVALID_TYPE_VALUE_ARGS = [
        "", "string",
        [], [1, 2, 3],
        {}, {"a": 1}
    ]
    OUT_OF_RANGE_VALUE_ARGS = [-100, -1, 0, 10, 11, 100]
    VALID_VALUE_ARGS = [None, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    SET_VALUE_ARGS = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    EMPTY_VALUE_ARGS = [None]
    ORDERED_VALUES = [Value.EMPTY_VALUE] + Value.VALUE_RANGE
