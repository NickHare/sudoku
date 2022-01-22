import pytest

from sudoku.core.position import Position
from sudoku.core.value import Value
from sudoku.core.cell import Cell


@pytest.mark.parametrize("test_pos, test_val", [
    (Position(0, 0), Value(None)), (Position(0, 0), Value(1)), (Position(0, 0), Value(5)), (Position(0, 0), Value(9)),
    (Position(1, 1), Value(None)), (Position(1, 1), Value(1)), (Position(1, 1), Value(5)), (Position(1, 1), Value(9)),
    (Position(4, 4), Value(None)), (Position(4, 4), Value(1)), (Position(4, 4), Value(5)), (Position(4, 4), Value(9)),
    (Position(8, 8), Value(None)), (Position(8, 8), Value(1)), (Position(8, 8), Value(5)), (Position(8, 8), Value(9)),
])
def test_valid_cells(test_pos, test_val):
    actual = Cell(test_pos, test_val)
    assert actual.pos == test_pos
    assert actual.val == test_val
    assert actual.is_set() == test_val.is_set()
    assert actual.is_empty() == test_val.is_empty()
    assert actual.is_set() or actual.is_empty()


@pytest.mark.parametrize("test_pos, test_val", [
    ("", ""), (1, 1), ([], []), ({}, {})
])
def test_invalid_cells(test_pos, test_val):
    with pytest.raises(AssertionError):
        actual = Cell(test_pos, test_val)


@pytest.mark.parametrize("test_cell, test_pos, test_val", [
    (Cell(Position(0, 0), Value(None)), Position(0, 0), Value(None)),
    (Cell(Position(1, 1), Value(1)), Position(1, 1), Value(1)),
    (Cell(Position(4, 4), Value(5)), Position(4, 4), Value(5)),
    (Cell(Position(8, 8), Value(9)), Position(8, 8), Value(9)),
])
def test_cells_equal(test_cell, test_pos, test_val):
    actual = Cell(test_pos, test_val)
    assert actual == test_cell

