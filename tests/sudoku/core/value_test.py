import pytest

from sudoku.core.value import Value


@pytest.mark.parametrize("test_num", [None, 1, 2, 3, 4, 5, 6, 7, 8, 9])
def test_valid_values(test_num):
    actual = Value(test_num)
    assert actual.num == test_num
    assert actual.is_set() or actual.is_empty()


@pytest.mark.parametrize("test_num", [1, 2, 3, 4, 5, 6, 7, 8, 9])
def test_valid_set_values(test_num):
    actual = Value(test_num)
    assert actual.num == test_num
    assert actual.is_set()
    assert not actual.is_empty()
    assert test_num in Value.NUM_RANGE
    assert actual in Value.VALUE_RANGE


def test_valid_none_value():
    actual = Value(None)
    assert actual.num is None
    assert not actual.is_set()
    assert actual.is_empty()
    assert actual == Value.EMPTY_VALUE


@pytest.mark.parametrize("test_num", [-10, -1, 0, 10, 11, 100, 1.5, "", "1", [], {}])
def test_invalid_values(test_num):
    with pytest.raises(AssertionError):
        actual = Value(test_num)


@pytest.mark.parametrize("test_value, test_num", [
    (Value(None), None), (Value(1), 1), (Value(2), 2), (Value(3), 3), (Value(4), 4),
    (Value(5), 5), (Value(6), 6), (Value(7), 7), (Value(8), 8), (Value(9), 9)
])
def test_values_equal(test_value, test_num):
    actual = Value(test_num)
    assert actual == test_value