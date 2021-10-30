from sudoku_board import SudokuBoard


class SudokuSolver:

    def __init__(self, board: SudokuBoard):
        self.board = board
        self.candidates = self.gather_board_candidates()

    def gather_board_candidates(self):
        board_candidates = []
        for r in range(SudokuBoard.ROW_SIZE):
            board_candidates.append([])
            for c in range(SudokuBoard.COL_SIZE):
                cell_candidates = self.gather_cell_candidates(r, c)
                board_candidates[r].append(cell_candidates)
        return board_candidates

    def gather_cell_candidates(self, row_num, col_num):
        row = self.board.get_row(row_num)
        col = self.board.get_col(col_num)
        box_num = SudokuBoard.row_col_to_box_num(row_num, col_num)
        box = self.board.get_box(box_num)
        cell_value = self.board.get_cell(row_num, col_num)

        if cell_value is not None:
            cell_candidates = [True] + [False] * SudokuBoard.SIZE
            cell_candidates[cell_value] = True
        elif cell_value is None:
            cell_candidates = [False] + [True] * SudokuBoard.SIZE
            num_candidates = SudokuBoard.SIZE

            for n in range(1, SudokuBoard.SIZE + 1):
                if (n in row) or (n in col) or (n in box):
                    cell_candidates[n] = False
                    num_candidates -= 1

            assert num_candidates > 0
            if num_candidates == 1:
                cell_candidates[0] = True

        return cell_candidates

    def solve_candidate_cells(self):
        pass

    def gather_solvable_cells(self):
        solvable_cells = {}
        for n in range(SudokuBoard.SIZE):
            row = self.board.get_row(n)
            col = self.board.get_col(n)
            box = self.board.get_box(n)

            row_candidates = [0] * 10
            col_candidates = [0] * 10
            box_candidates = [0] * 10
            # for pos, value in row:
            #     if value is None:
            #         if len(self.candidates[pos[0], pos[1]]) == 1:

        pass
