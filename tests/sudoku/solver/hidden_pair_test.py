from sudoku.core.board import Board
from sudoku.core.group_type import GroupType
from sudoku.solver.board_solver import BoardSolver
from tests.sudoku.solver.hidden_pair_data import HiddenPairData

b = Board(HiddenPairData.HIDDEN_PAIR_BOARD)
s = BoardSolver(b)
print(b.is_valid())
print(s.board_cell_candidates[1])
print(s.board_group_candidates[GroupType.ROW][1])
pairs = s.remove_hidden_pair_extra_candidates(b.rows[1])
print(pairs)
print(s.board_cell_candidates[1])
print(s.board_group_candidates[GroupType.ROW][1])
