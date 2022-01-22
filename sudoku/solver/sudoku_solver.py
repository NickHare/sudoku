import sudoku_config as config
from core.sudoku_board import SudokuBoard
from core.sudoku_group import SudokuGroup
from core.sudoku_group import SudokuGroupType
from core.sudoku_cell import SudokuCell
from core.sudoku_position import SudokuPosition
from core.sudoku_value import SudokuValue
from solver.sudoku_cell_candidates import SudokuCellCandidates
from solver.sudoku_group_candidates import SudokuGroupCandidates


class SudokuSolver:

    def __init__(self, board: SudokuBoard) -> None:
        self.board = board
        self.cell_candidates_board = self.gather_all_cell_candidates()
        self.group_candidates_board = self.gather_all_group_candidates()
        self.eliminate_extra_candidates()
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
            cell_value = cell.val
            value_index = cell_value.num
            cell_candidates = [True] + [False] * config.SIZE
            cell_candidates[value_index] = True
        elif cell.is_empty():
            cell_candidates = [False] + [True] * config.SIZE
            num_candidates = config.SIZE

            for candidate_value in SudokuValue.VALUE_RANGE:
                if row.is_value_in_group(candidate_value) or col.is_value_in_group(candidate_value) or box.is_value_in_group(candidate_value):
                    value_index = candidate_value.num
                    cell_candidates[value_index] = False
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
        for cell in group.get_empty_cells():
            pos = cell.pos
            cell_candidates = self.cell_candidates_board[pos.row_num][pos.col_num]
            for candidate_value in SudokuValue.VALUE_RANGE:
                if cell_candidates.is_candidate_value(candidate_value):
                    if candidate_value not in group_candidates:
                        group_candidates[candidate_value] = []
                    group_candidates[candidate_value].append(pos)

        return SudokuGroupCandidates(group_candidates)

    def eliminate_extra_candidates(self):
        for group_num in SudokuGroup.GROUP_NUM_RANGE:
            row = self.board.get_row(group_num)
            self.remove_hidden_pair_extra_candidates(row)
            self.remove_naked_pair_extra_candidates(row)

            col = self.board.get_col(group_num)
            self.remove_hidden_pair_extra_candidates(col)
            self.remove_naked_pair_extra_candidates(col)

            box = self.board.get_box(group_num)
            self.remove_hidden_pair_extra_candidates(box)
            self.remove_naked_pair_extra_candidates(box)

        self.gather_all_group_candidates()
        for group_num in SudokuGroup.GROUP_NUM_RANGE:
            box = self.board.get_box(group_num)
            self.remove_peaking_pair_extra_candidates(box)

        self.gather_all_group_candidates()

    def remove_hidden_pair_extra_candidates(self, group: SudokuGroup):
        group_candidates = self.group_candidates_board[group.group_type][group.group_num]
        double_candidate_cell_values = group_candidates.get_group_candidate_values_for_count(2)
        num_doubles = len(double_candidate_cell_values)
        if num_doubles >= 2 and len(group.get_empty_cells()) > 2:
            for n in range(num_doubles):
                candidate_value = double_candidate_cell_values[n]
                candidate_positions = group_candidates.get_group_candidate_positions_for_value(candidate_value)
                for m in range(n + 1, num_doubles):
                    other_candidate_value = double_candidate_cell_values[m]
                    other_candidate_positions = group_candidates.get_group_candidate_positions_for_value(other_candidate_value)
                    if set(candidate_positions) == set(other_candidate_positions):
                        print(f'Hidden Pair found in {group.group_type} {group.group_num}. Positions: {candidate_positions}, Values: {candidate_value}, {other_candidate_value}')
                        for pos in candidate_positions:
                            cell_candidates = self.cell_candidates_board[pos.row_num][pos.col_num]
                            removed_candidate_cells = []
                            for value in SudokuValue.VALUE_RANGE:
                                if cell_candidates.is_candidate_value(value) and value != candidate_value and value != other_candidate_value:
                                    cell_candidates = self.cell_candidates_board[pos.row_num][pos.col_num]
                                    cell_candidates.remove_candidate_value(value)
                                    removed_candidate_cells.append(SudokuCell(pos, value))
                            if len(removed_candidate_cells) > 0:
                                print(f'Removed Candidate Cells: {removed_candidate_cells}')

    def remove_naked_pair_extra_candidates(self, group: SudokuGroup) -> None:
        double_candidate_cells = []
        num_doubles = 0
        for cell in group.group_cells:
            pos = cell.pos
            cell_candidates = self.cell_candidates_board[pos.row_num][pos.col_num]
            if cell_candidates.candidate_count == 2:
                double_candidate_cells.append(cell)
                num_doubles += 1

        if num_doubles >= 2:
            for n in range(num_doubles):
                candidate_cell = double_candidate_cells[n]
                candidate_pos = candidate_cell.pos
                r1, c1 = candidate_pos.row_num, candidate_pos.col_num
                candidate_values = self.cell_candidates_board[r1][c1].get_candidate_values()
                for m in range(n + 1, num_doubles):
                    other_candidate_cell = double_candidate_cells[m]
                    other_candidate_pos = other_candidate_cell.pos
                    r2, c2 = other_candidate_pos.row_num, other_candidate_pos.col_num
                    other_candidate_values = self.cell_candidates_board[r2][c2].get_candidate_values()
                    if set(candidate_values) == set(other_candidate_values):
                        print(f'Naked Pair found in {group.group_type} {group.group_num}. Positions: {candidate_pos, other_candidate_pos}, Values: {candidate_values}')
                        for cell in group.get_empty_cells():
                            pos = cell.pos
                            cell_candidates = self.cell_candidates_board[pos.row_num][pos.col_num]
                            removed_candidate_cells = []
                            if pos != candidate_pos and pos != other_candidate_pos:
                                if cell_candidates.is_candidate_value(candidate_values[0]):
                                    cell_candidates.remove_candidate_value(candidate_values[0])
                                    removed_candidate_cells.append(SudokuCell(pos, candidate_values[0]))
                                if cell_candidates.is_candidate_value(candidate_values[1]):
                                    cell_candidates.remove_candidate_value(candidate_values[1])
                                    removed_candidate_cells.append(SudokuCell(pos, candidate_values[1]))
                            if len(removed_candidate_cells) > 0:
                                print(f'Removed Candidate Cells: {removed_candidate_cells}')

    def remove_peaking_pair_extra_candidates(self, box_group: SudokuGroup) -> None:
        assert box_group.group_type == SudokuGroupType.BOX

        group_candidates = self.group_candidates_board[box_group.group_type][box_group.group_num]

        for value in group_candidates.get_group_candidate_values_for_count(2):
            removed_candidate_cells = []
            pair_positions = group_candidates.get_group_candidate_positions_for_value(value)
            assert len(pair_positions) == 2
            if pair_positions[0].row_num == pair_positions[1].row_num:
                row_candidates = self.group_candidates_board[SudokuGroupType.ROW][pair_positions[0].row_num]
                row_value_positions = row_candidates.get_group_candidate_positions_for_value(value)
                if len(row_value_positions) > 2:
                    removed_candidate_cells = [SudokuCell(pos, value) for pos in row_value_positions if pos not in pair_positions]

            elif pair_positions[0].col_num == pair_positions[1].col_num:
                col_candidates = self.group_candidates_board[SudokuGroupType.COL][pair_positions[0].col_num]
                col_value_positions = col_candidates.get_group_candidate_positions_for_value(value)
                if len(col_value_positions) > 2:
                    removed_candidate_cells = [SudokuCell(pos, value) for pos in col_value_positions if pos not in pair_positions]

            if len(removed_candidate_cells) > 0:
                for cell in removed_candidate_cells:
                    self.cell_candidates_board[cell.pos.row_num][cell.pos.col_num].remove_candidate_value(value)
                print(f'Peaking Pair found in Box {box_group.group_num}. Positions: {pair_positions}, Value: {value}')
                print(f'Removed Candidate Cells: {removed_candidate_cells}')

    def solve_single_candidate_cells(self) -> list[SudokuCell]:
        solution_history_step = []
        for cell in self.solvable_cells:
            is_set = self.board.set_cell(cell)
            if is_set:
                solution_history_step.append(cell)
                self.cell_candidates_board[cell.pos.row_num][cell.pos.col_num] = self.gather_cell_candidates(cell.pos)
                print(f'Set {cell}')
            else:
                print(f'ERROR: Error setting {cell}.')
        self.solution_history.append(solution_history_step)
        self.cell_candidates_board = self.gather_all_cell_candidates()
        self.group_candidates_board = self.gather_all_group_candidates()
        self.eliminate_extra_candidates()
        self.solvable_cells = self.gather_solvable_cells()
        return solution_history_step

    def gather_solvable_cells(self) -> dict[SudokuPosition, SudokuValue]:
        single_cell_candidates = self.find_single_candidate_cells()
        single_group_candidates = self.find_single_candidate_value_groups()
        solvable_cells = list(set(single_group_candidates).union(single_cell_candidates))
        return solvable_cells

    def find_single_candidate_cells(self) -> dict[SudokuPosition, SudokuValue]:
        single_candidate_cells = []
        for row_num in range(config.ROW_SIZE):
            for col_num in range(config.COL_SIZE):
                pos = SudokuPosition(row_num, col_num)
                cell = self.board.get_cell(pos)
                cell_candidates = self.cell_candidates_board[row_num][col_num]
                if cell.is_empty() and cell_candidates.is_single_candidate_cell():
                    candidate_value = cell_candidates.single_candidate_value
                    candidate_cell = SudokuCell(pos, candidate_value)
                    print(f'Single Candidate Cell... {candidate_cell}')
                    single_candidate_cells.append(candidate_cell)
        return single_candidate_cells

    def find_single_candidate_value_groups(self) -> dict[SudokuPosition, SudokuValue]:
        single_candidate_cells = []
        for group_type in SudokuGroupType:
            for group_num in SudokuGroup.GROUP_NUM_RANGE:
                group_candidates = self.group_candidates_board[group_type][group_num]
                for value in group_candidates.get_group_candidate_values_for_count(1):
                    pos = group_candidates.get_group_candidate_positions_for_value(value)[0]
                    print(f'Single Candidate Value Group... {group_type} {group_num}: {pos} - {value}')
                    single_candidate_cells.append(SudokuCell(pos, value))
        return single_candidate_cells
