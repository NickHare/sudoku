from solver.sudoku_solver import SudokuSolver
from core.sudoku_board import SudokuBoard
from tests import sudoku_test_data as data

sb = SudokuBoard.board_from_numbers(data.TEST_SUDOKU_BOARDS[5])
# sb = SudokuBoard.board_from_numbers(data.TEST_SUDOKU_BOARD)
print("Starting Board...")
print(sb)
print('--------')
print(f'Valid Board: {sb.validate_board()}')
print('--------')

ss = SudokuSolver(sb)
step = 0
while not sb.is_completed():
    step += 1
    solution_cells = ss.solve_single_candidate_cells()
    print("Solving Board...")
    print(sb)
    print('--------')
    print(f'Step: {step}')
    print(f'Solution Step: {solution_cells}')
    print(f'Valid Board: {sb.validate_board()}')
    print('--------')
print(sb)
