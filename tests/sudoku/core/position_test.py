import pytest
from sudoku.core.position import Position
from tests.sudoku.core.position_data import PositionData


@pytest.mark.parametrize("test_row_num, test_col_num", PositionData.INVALID_TYPE_POSITION_ARGS)
def test_invalid_type_positions(test_row_num, test_col_num):
    with pytest.raises(AssertionError):
        actual_position = Position(test_row_num, test_col_num)


@pytest.mark.parametrize("test_row_num, test_col_num", PositionData.OUT_OF_RANGE_POSITION_ARGS)
def test_out_of_range_positions(test_row_num, test_col_num):
    with pytest.raises(AssertionError):
        actual_position = Position(test_row_num, test_col_num)


@pytest.mark.parametrize("test_row_num, test_col_num", PositionData.VALID_POSITION_ARGS)
def test_valid_positions(test_row_num, test_col_num):
    actual_position = Position(test_row_num, test_col_num)
    assert actual_position == Position(test_row_num, test_col_num)
    assert actual_position.row_num == test_row_num
    assert actual_position.col_num == test_col_num


def test_position_order():
    pos_list = PositionData.ORDERED_POSITIONS
    for i in range(len(pos_list) - 1):
        assert pos_list[i] < pos_list[i + 1]
    for i in range(len(pos_list) - 1, 0, -1):
        assert pos_list[i] > pos_list[i - 1]

