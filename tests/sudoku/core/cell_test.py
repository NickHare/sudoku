import pytest

from sudoku.core.cell import Cell
from tests.sudoku.core.cell_data import CellData


@pytest.mark.parametrize("test_pos, test_val", CellData.VALID_CELL_ARGS)
def test_valid_cells(test_pos, test_val):
    actual_cell = Cell(test_pos, test_val)
    assert actual_cell.pos == test_pos
    assert actual_cell.val == test_val
    assert actual_cell.is_set() == test_val.is_set()
    assert actual_cell.is_empty() == test_val.is_empty()
    assert actual_cell.is_set() or actual_cell.is_empty()


@pytest.mark.parametrize("test_pos, test_val", CellData.INVALID_TYPE_CELL_ARGS)
def test_invalid_cells(test_pos, test_val):
    with pytest.raises(AssertionError):
        actual_cell = Cell(test_pos, test_val)


def test_cell_order():
    cell_list = CellData.ORDERED_CELLS
    for i in range(len(cell_list) - 1):
        assert cell_list[i] < cell_list[i + 1]
    for i in range(len(cell_list) - 1, 0, -1):
        assert cell_list[i] > cell_list[i - 1]
