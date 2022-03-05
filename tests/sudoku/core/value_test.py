import pytest

from sudoku.core.value import Value
from tests.sudoku.core.value_data import ValueData


@pytest.mark.parametrize("test_num", ValueData.INVALID_TYPE_VALUE_ARGS)
def test_invalid_type_values(test_num):
    with pytest.raises(AssertionError):
        actual_value = Value(test_num)


@pytest.mark.parametrize("test_num", ValueData.OUT_OF_RANGE_VALUE_ARGS)
def test_out_of_range_values(test_num):
    with pytest.raises(AssertionError):
        actual_value = Value(test_num)


@pytest.mark.parametrize("test_num", ValueData.VALID_VALUE_ARGS)
def test_valid_values(test_num):
    actual = Value(test_num)
    assert actual == Value(test_num)
    assert actual.num == test_num
    assert actual.is_set() or actual.is_empty()
    assert test_num in Value.NUM_RANGE or test_num == Value.EMPTY_NUM
    assert actual in Value.VALUE_RANGE or actual == Value.EMPTY_VALUE


@pytest.mark.parametrize("test_num", ValueData.SET_VALUE_ARGS)
def test_set_values(test_num):
    actual = Value(test_num)
    assert actual == Value(test_num)
    assert actual.num == test_num
    assert actual.is_set() and not actual.is_empty()
    assert test_num in Value.NUM_RANGE
    assert actual in Value.VALUE_RANGE


@pytest.mark.parametrize("test_num", ValueData.EMPTY_VALUE_ARGS)
def test_empty_values(test_num):
    actual = Value(test_num)
    assert actual == Value(test_num)
    assert actual.num is None
    assert not actual.is_set() and actual.is_empty()
    assert test_num == Value.EMPTY_NUM
    assert actual == Value.EMPTY_VALUE


def test_value_order():
    val_list = ValueData.ORDERED_VALUES
    for i in range(len(val_list) - 1):
        assert val_list[i] < val_list[i + 1]
    for i in range(len(val_list) - 1, 0, -1):
        assert val_list[i] > val_list[i - 1]