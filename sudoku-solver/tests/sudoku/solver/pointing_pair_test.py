from sudoku.core.board import Board
from sudoku.core.group_type import GroupType
from sudoku.solver.board_solver import BoardSolver
from tests.sudoku.solver.pointing_pair_data import PointingPairData

b = Board(PointingPairData.POINTING_PAIR_BOARD)
s = BoardSolver(b)
print(b)
print(b.is_valid())
print(s.board_cell_candidates[0])
print(s.board_group_candidates[GroupType.ROW][0])
pairs = s.remove_pointing_pair_extra_candidates(b.boxes[0])
print(pairs)
print(s.board_cell_candidates[0])
print(s.board_group_candidates[GroupType.ROW][0])
