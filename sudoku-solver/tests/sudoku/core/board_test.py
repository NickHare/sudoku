import pytest

from sudoku.core.board import Board
from sudoku.core.group import GroupType

from tests.sudoku.core.board_data import BoardData


@pytest.mark.parametrize("test_num_board", BoardData.VALID_EMPTY_BOARD_ARGS)
def test_valid_empty_board(test_num_board):
    actual_board = Board(test_num_board)


@pytest.mark.parametrize("test_num_board", BoardData.VALID_PARTIAL_BOARD_ARGS)
def test_valid_partial_boards(test_num_board):
    actual_board = Board(test_num_board)


@pytest.mark.parametrize("test_num_board", BoardData.VALID_FULL_BOARD_ARGS)
def test_valid_full_boards(test_num_board):
    actual_board = Board(test_num_board)
    assert actual_board.is_completed()


@pytest.mark.parametrize("test_num_board, expected_group", BoardData.VALID_BOARD_GROUPS)
def test_valid_board_groups(test_num_board, expected_group):
    test_group_type = expected_group.type
    test_group_num = expected_group.num
    actual_board = Board(test_num_board)
    actual_group = actual_board.get_sudoku_group(test_group_type, test_group_num)
    actual_group_cells = actual_group.get_cells()
    expected_group_cells = expected_group.get_cells()

    assert len(actual_group_cells) == len(expected_group_cells)
    for cell in expected_group_cells:
        assert cell in actual_group_cells

    if test_group_type == GroupType.ROW:
        actual_group = actual_board.get_row(test_group_num)
    elif test_group_type == GroupType.COL:
        actual_group = actual_board.get_col(test_group_num)
    elif test_group_type == GroupType.BOX:
        actual_group = actual_board.get_box(test_group_num)
    actual_group_cells = actual_group.get_cells()

    assert len(actual_group_cells) == len(expected_group_cells)
    for cell in expected_group_cells:
        assert cell in actual_group_cells


@pytest.mark.parametrize("test_num_board, test_cell", BoardData.VALID_BOARD_SET_CELL)
def test_valid_board_set_cell(test_num_board, test_cell):
    board = Board(test_num_board)
    is_set = board.set_cell(test_cell)
    assert is_set
    assert board.get_cell(test_cell.pos) == test_cell

@pytest.mark.parametrize("test_num_board, test_cell", BoardData.INVALID_BOARD_SET_CELL)
def test_invalid_board_set_cell(test_num_board, test_cell):
    board = Board(test_num_board)
    initial_cell = board.get_cell(test_cell.pos)
    is_set = board.set_cell(test_cell)
    assert not is_set
    assert board.get_cell(test_cell.pos) == initial_cell