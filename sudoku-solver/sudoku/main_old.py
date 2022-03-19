from solver.board_solver import BoardSolver
from core.board import Board
from tests.sudoku.core.board_data import BoardData

b = Board(BoardData.VALID_PARTIAL_BOARD_ARGS[7])
# sb = SudokuBoard.board_from_numbers(data.TEST_SUDOKU_BOARD)
print("Starting Board...")
print(b)
print('--------')
print(f'Valid Board: {b.conflicts}')
print('--------')

s = BoardSolver(b)
step = 0
while not b.is_completed():
    step += 1
    solution_cells = s.solve_single_candidate_cells()
    print("Solving Board...")
    print(b)
    print('--------')
    print(f'Step: {step}')
    print(f'Solution Step: {solution_cells}')
    print(f'Valid Board: {b.is_valid()}')
    print('--------')
print(b)
