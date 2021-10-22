from sudoku_board import SudokuBoard
from sudoku_solver import SudokuSolver

t = [
    [None, None, None, None, None, None, None, None, None],
    [None, 9, None, 6, None, None, None, None, None],
    [None, 6, None, None, 7, None, 4, None, 3],
    [None, None, 2, None, None, 6, None, None, None],
    [None, None, 8, 1, None, None, None, None, 9],
    [5, None, None, 2, None, None, None, None, None],
    [None, None, None, None, 3, None, None, 5, None],
    [None, None, None, None, 8, 7, None, 2, None],
    [9, 3, None, None, None, None, None, 4, None]
]

sb = SudokuBoard(t)
v = sb.validate_board()
print(v)
ss = SudokuSolver(sb)
print(ss.candidates)
can = ss.candidates
l = [(r, c) for r in range(9) for c in range(9) if can[r][c][0] == True]
pos = (0, 0)
print(sb.get_cell_from_pos(pos))
print()
