import pytest

import sudoku_test_data as test_data
import sudoku_config as config


@pytest.mark.parametrize('test, expected', [
    (0, test_data.ROW_0_POSITIONS),
    (8, test_data.ROW_8_POSITIONS),
])
def test_row_positions(test, expected):
    actual = config.get_row_positions(test)
    assert len(actual) == len(expected)
    assert actual == expected


@pytest.mark.parametrize('test, expected', [
    (0, test_data.COL_0_POSITIONS),
    (8, test_data.COL_8_POSITIONS),
])
def test_col_positions(test, expected):
    actual = config.get_col_positions(test)
    assert len(actual) == len(expected)
    assert actual == expected


@pytest.mark.parametrize('test, expected', [
    (0, test_data.BOX_0_POSITIONS),
    (8, test_data.BOX_8_POSITIONS),
])
def test_box_positions(test, expected):
    actual = config.get_box_positions(test)
    assert len(actual) == len(expected)
    assert actual == expected

