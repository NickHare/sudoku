from sudoku.core.board import Board
from sudoku.core.group_type import GroupType
from sudoku.solver.board_solver import BoardSolver
from tests.sudoku.solver.boxed_pair_data import BoxedPairData

b = Board(BoxedPairData.BOXED_PAIR_BOARD)
s = BoardSolver(b)
print(b)
print(b.is_valid())
print(s.board_cell_candidates[2])
print(s.board_group_candidates[GroupType.ROW][2])
pairs = s.remove_boxed_pair_extra_candidates(b.rows[2])
print(pairs)
print(s.board_cell_candidates[2])
print(s.board_group_candidates[GroupType.ROW][2])
