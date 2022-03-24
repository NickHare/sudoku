from tests.sudoku.core.board_data import BoardData

from sudoku.core.board import Board
from sudoku.core.group import Group
from sudoku.core.group import GroupType
from sudoku.core.cell import Cell
from sudoku.core.value import Value
from sudoku.core.position import Position

board = Board(BoardData.VALID_PARTIAL_BOARD_ARGS[0])
print(board)
row = board.rows[1]
col = board.cols[0]
box = board.boxes[0]
cell = Cell(Position(1, 0), Value(9))
board.set_cell(cell)
print(board)
row = board.rows[1]
col = board.cols[0]
box = board.boxes[0]
cell = Cell(Position(1, 2), Value(9))
board.set_cell(cell)
print(board)
row = board.rows[1]
print(row)