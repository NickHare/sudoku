import pytest
from sudoku.core.position import Position


@pytest.mark.parametrize("test_pair", [
    (0, 0), (0, 1), (1, 0), (4, 5), (5, 4), (5, 5), (5, 6), (6, 5), (7, 8), (8, 7), (8, 8)
])
def test_valid_positions(test_pair):
    actual = Position(test_pair[0], test_pair[1])
    assert actual.row_num == test_pair[0]
    assert actual.col_num == test_pair[1]


@pytest.mark.parametrize("test_pair", [
    (-5, -5), (-1, -1), (-5, 0), (0, -5), (-1, 0), (0, -1),
    (-1, 5), (5, -1), (5, 9), (9, 5), (9, 8), (8, 9), (9, 9), (15, 15),
    ("", ""), ("1", "1"), ([], []), ({}, {})
])
def test_invalid_positions(test_pair):
    with pytest.raises(AssertionError):
        actual = Position(test_pair[0], test_pair[1])


@pytest.mark.parametrize("test_pos, test_row, test_col", [
    (Position(0, 0), 0, 0), (Position(0, 1), 0, 1), (Position(1, 0), 1, 0),
    (Position(1, 1), 1, 1), (Position(5, 5), 5, 5), (Position(7, 8), 7, 8),
    (Position(8, 7), 8, 7), (Position(8, 8), 8, 8)
])
def test_equal_positions(test_pos, test_row, test_col):
    actual = Position(test_row, test_col)
    assert actual == test_pos

