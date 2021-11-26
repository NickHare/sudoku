import sudoku_config as config
from core.sudoku_board import SudokuBoard
from core.sudoku_group import SudokuGroup
from core.sudoku_group import SudokuGroupType
from core.sudoku_position import SudokuPosition
from core.sudoku_cell import SudokuCell
from solver.sudoku_cell_candidates import SudokuCellCandidates
from solver.sudoku_group_candidates import SudokuGroupCandidates

class SudokuSolver:

    def __init__(self, board: SudokuBoard) -> None:
        self.board = board
        self.cell_candidates_board = self.gather_all_cell_candidates()
        self.group_candidates_board = self.gather_all_group_candidates()
        self.solvable_cells = self.gather_solvable_cells()
        self.solution_history = []

    def gather_all_cell_candidates(self) -> list[list[SudokuCellCandidates]]:
        cell_candidates_board = []
        for row_num in range(config.ROW_SIZE):
            row_candidates = []
            for col_num in range(config.COL_SIZE):
                pos = SudokuPosition(row_num, col_num)
                cell_candidates = self.gather_cell_candidates(pos)
                row_candidates.append(cell_candidates)
            cell_candidates_board.append(row_candidates)
        return cell_candidates_board

    def gather_cell_candidates(self, pos:SudokuPosition) -> SudokuCellCandidates:
        row = self.board.get_row(pos.row_num)
        col = self.board.get_col(pos.col_num)
        box_num = SudokuGroup.pos_to_box_num(pos)
        box = self.board.get_box(box_num)
        cell = self.board.get_cell(pos)

        if cell.is_set():
            cell_candidates = [True] + [False] * config.SIZE
            cell_candidates[cell.value] = True
        elif cell.is_empty():
            cell_candidates = [False] + [True] * config.SIZE
            num_candidates = config.SIZE

            for value in SudokuCell.VALUE_NUM_RANGE:
                candidate_cell = SudokuCell(value)
                if candidate_cell in row.get_cells() or candidate_cell in col.get_cells() or candidate_cell in box.get_cells():
                    cell_candidates[value] = False
                    num_candidates -= 1
            if num_candidates == 1:
                cell_candidates[0] = True
        return SudokuCellCandidates(cell_candidates)

    def gather_all_group_candidates(self) -> list[list[SudokuGroupCandidates]]:
        group_candidates_board = {
            SudokuGroupType.ROW: [],
            SudokuGroupType.COL: [],
            SudokuGroupType.BOX: []
        }
        for group_num in SudokuGroup.GROUP_NUM_RANGE:
            row = self.board.get_row(group_num)
            col = self.board.get_col(group_num)
            box = self.board.get_box(group_num)

            row_candidates = self.gather_group_candidates(row)
            col_candidates = self.gather_group_candidates(col)
            box_candidates = self.gather_group_candidates(box)

            group_candidates_board[SudokuGroupType.ROW].append(row_candidates)
            group_candidates_board[SudokuGroupType.COL].append(col_candidates)
            group_candidates_board[SudokuGroupType.BOX].append(box_candidates)
        return group_candidates_board

    def gather_group_candidates(self, group: SudokuGroup) -> SudokuGroupCandidates:
        group_candidates = {}
        for pos, cell in group.get_items():
            if cell.is_empty():
                for value in SudokuCell.VALUE_NUM_RANGE:
                    cell = SudokuCell(value)
                    cell_candidates = self.cell_candidates_board[pos.row_num][pos.col_num]
                    if cell_candidates.is_cell_candidate(cell):
                        if cell in group_candidates:
                            group_candidates[cell].append(pos)
                        else:
                            group_candidates[cell] = [pos]
        return SudokuGroupCandidates(group_candidates)

    def solve_single_candidate_cells(self) -> list[(SudokuPosition, SudokuCell)]:
        solution_history_step = []
        for pos, cell in self.solvable_cells.items():
            is_set = self.board.set_cell(pos, cell)
            if is_set:
                solution_history_step.append((pos, cell))
                print(f'Set {pos} to {cell}')
            else:
                print(f'ERROR: Error setting {pos} to {cell}.')
        self.solution_history.append(solution_history_step)
        self.cell_candidates_board = self.gather_all_cell_candidates()
        self.group_candidates_board = self.gather_all_group_candidates()
        self.solvable_cells = self.gather_solvable_cells()
        return solution_history_step

    def gather_solvable_cells(self) -> dict[SudokuPosition, SudokuCell]:
        single_cell_candidates = self.find_single_candidate_cells()
        single_group_candidates = self.find_group_candidate_cells()
        solvable_cells = {**single_group_candidates, **single_cell_candidates}
        return solvable_cells

    def find_single_candidate_cells(self) -> dict[SudokuPosition, SudokuCell]:
        single_candidate_cells = {}
        for row_num in range(config.ROW_SIZE):
            for col_num in range(config.COL_SIZE):
                pos = SudokuPosition(row_num, col_num)
                cell = self.board.get_cell(pos)
                cell_candidates = self.cell_candidates_board[row_num][col_num]
                if cell.is_empty() and cell_candidates.is_single_candidate_cell():
                    single_candidate_cell = cell_candidates.single_candidate_cell
                    # print(f'{pos} - {single_candidate_cell}')
                    single_candidate_cells[pos] = single_candidate_cell
        return single_candidate_cells

    def find_group_candidate_cells(self) -> dict[SudokuPosition, SudokuCell]:
        single_candidate_cells = {}
        for group_type in SudokuGroupType:
            for group_num in SudokuGroup.GROUP_NUM_RANGE:
                group_candidates = self.group_candidates_board[group_type][group_num]
                if group_candidates.has_single_candidate_cells:
                    for pos, cell in group_candidates.single_candidates.items():
                        # print(f'{group_type} {group_num}: {pos} - {cell}')
                        single_candidate_cells[pos] = cell
        return single_candidate_cells
