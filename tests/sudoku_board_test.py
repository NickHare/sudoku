import pytest

import sudoku_test_data as test_data
from core.sudoku_board import SudokuBoard


@pytest.mark.parametrize("test", [
    test_data.VALID_ROW_0_NONES,
    test_data.VALID_ROW_0_BASIC_INC,
    test_data.VALID_ROW_0_BASIC_DEC,
    test_data.VALID_ROW_0_STAG_INC,
])
def test_validate_values_valid(test):
    expected = True
    actual = SudokuBoard.validate_values(test)
    assert actual == expected

def test_validate_values_invalid_1(self):
    test = [1, 1, 3, 4, 5, 6, 7, 8, 9]
    expected = False
    result = SudokuBoard.validate_values(test)
    self.assertEqual(result, expected, "Class SudokuBoard, Function: validate_row, Sample full row with duplicate should be invalid")

def test_validate_values_invalid_2(self):
    test = [None, None, None, None, None, None, None, 9, 9]
    expected = False
    result = SudokuBoard.validate_values(test)
    self.assertEqual(result, expected, "Class SudokuBoard, Function: validate_row, Sample empty row with duplicate should be invalid")

def test_validate_values_invalid_3(self):
    test = [3, 3, 3, 3, 3, 3, 3, 3, 3]
    expected = False
    result = SudokuBoard.validate_values(test)
    self.assertEqual(result, expected, "Class SudokuBoard, Function: validate_row, Sample repeated row should be invalid")

def test_validate_values_error_1(self):
    test = None
    self.assertRaises(AssertionError, SudokuBoard.validate_values, test)

def test_validate_values_error_2(self):
    test = []
    self.assertRaises(AssertionError, SudokuBoard.validate_values, test)

def test_validate_values_error_3(self):
    test = list(range(9))
    self.assertRaises(AssertionError, SudokuBoard.validate_values, test)

def test_validate_values_error_4(self):
    test = list(range(11))
    self.assertRaises(AssertionError, SudokuBoard.validate_values, test)

def test_validate_values_error_5(self):
    test = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
    self.assertRaises(AssertionError, SudokuBoard.validate_values, test)

def test_validate_values_error_6(self):
    test = [1, "string", 2, 3, 4, 5, 6, 7, 8]
    self.assertRaises(AssertionError, SudokuBoard.validate_values, test)

def test_validate_values_error_6(self):
    test = [1, 15, 3, 4, 5, 6, 7, 8, 9]
    self.assertRaises(AssertionError, SudokuBoard.validate_values, test)

def test_validate_values_error_7(self):
    test = [1, -5, 3, 4, 5, 6, 7, 8, 9]
    self.assertRaises(AssertionError, SudokuBoard.validate_values, test)

def test_validate_board_value_1(self):
    test = []


