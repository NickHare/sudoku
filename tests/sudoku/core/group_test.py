import pytest

from sudoku.core.value import Value
from sudoku.core.cell import Cell
from sudoku.core.group import Group
from sudoku.core.group_type import GroupType
from sudoku.config import Config

from tests.sudoku.core.group_data import GroupData


def assert_group_invariants(group: Group, group_type: GroupType, group_num: int, group_cells: list[Cell]):
    cells = group.cells
    set_cells = group.get_set_cells()
    empty_cells = group.get_empty_cells()

    assert group.type == group_type
    assert group.num == group_num
    assert cells == group_cells
    assert len(cells) == Config.SIZE
    assert len(set_cells) + len(empty_cells) == Config.SIZE
    assert sorted(set_cells + empty_cells) == sorted(cells)


@pytest.mark.parametrize("test_group_type, test_group_num, test_group_cells", GroupData.INVALID_TYPE_GROUP_ARGS)
def test_invalid_type_group(test_group_type, test_group_num, test_group_cells):
    with pytest.raises(AssertionError):
        actual_group = Group(test_group_type, test_group_num, test_group_cells)


@pytest.mark.parametrize("test_group_type, test_group_num, test_group_cells", GroupData.REPEATED_POSITION_GROUP_ARGS)
def test_invalid_repeated_position_group(test_group_type, test_group_num, test_group_cells):
    with pytest.raises(AssertionError):
        actual_group = Group(test_group_type, test_group_num, test_group_cells)


@pytest.mark.parametrize("test_group_type, test_group_num, test_group_cells", GroupData.WRONG_POSITION_GROUP_ARGS)
def test_invalid_wrong_position_group(test_group_type, test_group_num, test_group_cells):
    with pytest.raises(AssertionError):
        actual_group = Group(test_group_type, test_group_num, test_group_cells)


@pytest.mark.parametrize("test_group_type, test_group_num, test_group_cells", GroupData.EMPTY_GROUP_ARGS)
def test_valid_empty_groups(test_group_type, test_group_num, test_group_cells):
    actual_group = Group(test_group_type, test_group_num, test_group_cells)
    assert_group_invariants(actual_group, test_group_type, test_group_num, test_group_cells)

    assert actual_group.conflicts == []
    assert not actual_group.has_conflicts()

    assert actual_group.get_set_cells() == []
    assert sorted(actual_group.get_empty_cells()) == sorted(actual_group.cells)

    for val in Value.VALUE_RANGE:
        assert not actual_group.is_value_in_group(val)


@pytest.mark.parametrize("test_group_type, test_group_num, test_group_cells", GroupData.PARTIAL_GROUP_ARGS)
def test_valid_partial_groups(test_group_type, test_group_num, test_group_cells):
    actual_group = Group(test_group_type, test_group_num, test_group_cells)
    assert_group_invariants(actual_group, test_group_type, test_group_num, test_group_cells)

    assert actual_group.conflicts == []
    assert not actual_group.has_conflicts()


@pytest.mark.parametrize("test_group_type, test_group_num, test_group_cells", GroupData.FULL_GROUP_ARGS)
def test_valid_full_groups(test_group_type, test_group_num, test_group_cells):
    actual_group = Group(test_group_type, test_group_num, test_group_cells)
    assert_group_invariants(actual_group, test_group_type, test_group_num, test_group_cells)

    assert actual_group.conflicts == []
    assert not actual_group.has_conflicts()

    assert actual_group.get_empty_cells() == []
    assert sorted(actual_group.get_set_cells()) == sorted(actual_group.cells)

    for val in Value.VALUE_RANGE:
        assert actual_group.is_value_in_group(val)


@pytest.mark.parametrize("test_group_type, test_group_num, test_group_cells, expected_conflicts", GroupData.REPEATED_VALUE_GROUP_ARGS)
def test_valid_repeated_value_group(test_group_type, test_group_num, test_group_cells, expected_conflicts):
    actual_group = Group(test_group_type, test_group_num, test_group_cells)
    assert_group_invariants(actual_group, test_group_type, test_group_num, test_group_cells)

    assert actual_group.conflicts == expected_conflicts
    assert actual_group.has_conflicts()


@pytest.mark.parametrize("test_group_num, expected_group_positions", GroupData.ROW_POSITIONS)
def test_valid_row_positions(test_group_num, expected_group_positions):
    actual_group_positions = Group.get_row_positions(test_group_num)
    assert sorted(actual_group_positions) == sorted(expected_group_positions)


@pytest.mark.parametrize("test_group_num, expected_group_positions", GroupData.COL_POSITIONS)
def test_valid_col_positions(test_group_num, expected_group_positions):
    actual_group_positions = Group.get_col_positions(test_group_num)
    assert sorted(actual_group_positions) == sorted(expected_group_positions)


@pytest.mark.parametrize("test_group_num, expected_group_positions", GroupData.BOX_POSITIONS)
def test_valid_box_positions(test_group_num, expected_group_positions):
    actual_group_positions = Group.get_box_positions(test_group_num)
    assert sorted(actual_group_positions) == sorted(expected_group_positions)

