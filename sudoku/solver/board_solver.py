from sudoku.config import Config
from sudoku.core.board import Board
from sudoku.core.group import Group
from sudoku.core.group_type import GroupType
from sudoku.core.cell import Cell
from sudoku.core.position import Position
from sudoku.core.value import Value
from sudoku.solver.cell_candidates import CellCandidates
from sudoku.solver.group_candidates import GroupCandidates
from sudoku.solver.hidden_pair import HiddenPair
from sudoku.solver.naked_pair import NakedPair
from sudoku.solver.pointing_pair import PointingPair
from sudoku.solver.boxed_pair import BoxedPair


class BoardSolver:

    def __init__(self, board: Board) -> None:
        self.board = board
        self.board_cell_candidates = self.gather_board_cell_candidates()
        self.board_group_candidates = self.gather_board_group_candidates()
        self.removed_candidates = self.remove_extra_candidates()
        self.solvable_cells = self.gather_solvable_cells()
        self.solution_history = []

    def gather_board_cell_candidates(self) -> list[list[CellCandidates]]:
        board_cell_candidates = []
        for row_num in range(Config.ROW_SIZE):
            row_candidates = []
            for col_num in range(Config.COL_SIZE):
                pos = Position(row_num, col_num)
                cell = self.board.get_cell(pos)
                cell_candidates = self.gather_cell_candidates(cell)
                row_candidates.append(cell_candidates)
            board_cell_candidates.append(row_candidates)
        return board_cell_candidates

    def gather_cell_candidates(self, cell: Cell) -> CellCandidates:
        pos = cell.pos
        val = cell.val

        row = self.board.rows[pos.row_num]
        col = self.board.cols[pos.col_num]
        box_num = Group.pos_to_box_num(pos)
        box = self.board.boxes[box_num]

        candidate_values = []
        if val.is_set():
            candidate_values = [val]
        elif val.is_empty():
            candidate_values = [candidate_value for candidate_value in Value.VALUE_RANGE
                                if not row.is_value_in_group(candidate_value)
                                and not col.is_value_in_group(candidate_value)
                                and not box.is_value_in_group(candidate_value)]
        return CellCandidates(pos, candidate_values)

    def gather_board_group_candidates(self) -> dict[GroupType, list[GroupCandidates]]:
        group_candidates_board = {
            GroupType.ROW: [self.gather_group_candidates(self.board.rows[group_num])
                            for group_num in Group.GROUP_NUM_RANGE],
            GroupType.COL: [self.gather_group_candidates(self.board.cols[group_num])
                            for group_num in Group.GROUP_NUM_RANGE],
            GroupType.BOX: [self.gather_group_candidates(self.board.boxes[group_num])
                            for group_num in Group.GROUP_NUM_RANGE]
        }
        return group_candidates_board

    def gather_group_candidates(self, group: Group) -> GroupCandidates:
        group_candidates = {}
        for cell in group.get_empty_cells():
            pos = cell.pos
            cell_candidates = self.board_cell_candidates[pos.row_num][pos.col_num]
            for candidate_value in cell_candidates.candidate_values:
                if candidate_value not in group_candidates:
                    group_candidates[candidate_value] = []
                group_candidates[candidate_value].append(pos)
        return GroupCandidates(group_candidates)

    def remove_extra_candidates(self):
        removed_candidates = []
        while True:
            removed_candidates_step = []
            for group_num in Group.GROUP_NUM_RANGE:
                row = self.board.rows[group_num]
                removed_candidates_step += self.remove_hidden_pair_extra_candidates(row)
                removed_candidates_step += self.remove_naked_pair_extra_candidates(row)
                removed_candidates_step += self.remove_boxed_pair_extra_candidates(row)

                col = self.board.cols[group_num]
                removed_candidates_step += self.remove_hidden_pair_extra_candidates(col)
                removed_candidates_step += self.remove_naked_pair_extra_candidates(col)
                removed_candidates_step += self.remove_boxed_pair_extra_candidates(col)

                box = self.board.boxes[group_num]
                removed_candidates_step += self.remove_hidden_pair_extra_candidates(box)
                removed_candidates_step += self.remove_naked_pair_extra_candidates(box)
                removed_candidates_step += self.remove_pointing_pair_extra_candidates(box)
            if not removed_candidates_step:
                break
            removed_candidates += removed_candidates_step
        return removed_candidates

    def remove_hidden_pair_extra_candidates(self, group: Group) -> list[HiddenPair]:
        hidden_pairs = []
        group_candidates = self.board_group_candidates[group.type][group.num]
        candidate_values_with_two_cells = group_candidates.get_candidate_values_for_count(2)
        num_values = len(candidate_values_with_two_cells)

        if num_values >= 2 and len(group.get_empty_cells()) >= 2:
            for n in range(num_values):
                first_candidate_value = candidate_values_with_two_cells[n]
                first_candidate_positions = group_candidates.get_positions_for_candidate_value(first_candidate_value)
                for m in range(n + 1, num_values):
                    second_candidate_value = candidate_values_with_two_cells[m]
                    second_candidate_positions = group_candidates.get_positions_for_candidate_value(second_candidate_value)
                    if set(first_candidate_positions) == set(second_candidate_positions):
                        removed_candidate_cells = []
                        for pos in first_candidate_positions:
                            cell_candidates = self.board_cell_candidates[pos.row_num][pos.col_num]
                            for value in cell_candidates.candidate_values:
                                if value != first_candidate_value and value != second_candidate_value:
                                    removed_candidate_cells.append(Cell(pos, value))
                            for cell in removed_candidate_cells:
                                if cell.pos == pos:
                                    cell_candidates.remove_candidate_value(cell.val)
                        hidden_pairs.append(HiddenPair(group.type, group.num, (first_candidate_positions[0], first_candidate_positions[1]), (first_candidate_value, second_candidate_value), removed_candidate_cells))
            for hidden_pair in hidden_pairs:
                for candidate_cell in hidden_pair.eliminated_candidates:
                    group_candidates.remove_group_candidate(candidate_cell)
        return hidden_pairs

    def remove_naked_pair_extra_candidates(self, group: Group) -> list[NakedPair]:
        naked_pairs = []
        group_candidates = self.board_group_candidates[group.type][group.num]
        cells_with_two_candidate_values = [cell for cell in group.cells if self.board_cell_candidates[cell.pos.row_num][cell.pos.col_num].candidate_count == 2]
        num_cells = len(cells_with_two_candidate_values)

        if num_cells >= 2 and len(group.get_empty_cells()) >= 2:
            for n in range(num_cells):
                first_candidate_cell = cells_with_two_candidate_values[n]
                first_candidate_pos = first_candidate_cell.pos
                first_candidate_values = self.board_cell_candidates[first_candidate_cell.pos.row_num][first_candidate_cell.pos.col_num].candidate_values
                for m in range(n + 1, num_cells):
                    second_candidate_cell = cells_with_two_candidate_values[m]
                    second_candidate_pos = second_candidate_cell.pos
                    second_candidate_values = self.board_cell_candidates[second_candidate_cell.pos.row_num][second_candidate_cell.pos.col_num].candidate_values
                    if set(first_candidate_values) == set(second_candidate_values):
                        removed_candidate_cells = []
                        for cell in group.get_empty_cells():
                            pos = cell.pos
                            cell_candidates = self.board_cell_candidates[pos.row_num][pos.col_num]
                            if pos != first_candidate_pos and pos != second_candidate_pos:
                                if first_candidate_values[0] in cell_candidates.candidate_values:
                                    removed_cell = Cell(pos, first_candidate_values[0])
                                    cell_candidates.remove_candidate_value(removed_cell.val)
                                    group_candidates.remove_group_candidate(removed_cell)
                                    removed_candidate_cells.append(removed_cell)
                                if first_candidate_values[1] in cell_candidates.candidate_values:
                                    removed_cell = Cell(pos, first_candidate_values[1])
                                    cell_candidates.remove_candidate_value(removed_cell.val)
                                    group_candidates.remove_group_candidate(removed_cell)
                                    removed_candidate_cells.append(removed_cell)
                        naked_pairs.append(NakedPair(group.type, group.num, (first_candidate_pos, second_candidate_pos), (first_candidate_values[0], first_candidate_values[1]), removed_candidate_cells))
        return naked_pairs

    def remove_pointing_pair_extra_candidates(self, box_group: Group) -> list[PointingPair]:
        assert box_group.type == GroupType.BOX

        pointing_pairs = []
        group_candidates = self.board_group_candidates[box_group.type][box_group.num]
        candidate_values_with_two_cells = group_candidates.get_candidate_values_for_count(2)
        for candidate_value in candidate_values_with_two_cells:
            pair_positions = group_candidates.get_positions_for_candidate_value(candidate_value)
            assert len(pair_positions) == 2
            if pair_positions[0].row_num == pair_positions[1].row_num:
                row_candidates = self.board_group_candidates[GroupType.ROW][pair_positions[0].row_num]
                row_candidate_value_positions = row_candidates.get_positions_for_candidate_value(candidate_value)
                if len(row_candidate_value_positions) > 2:
                    removed_candidate_cells = [Cell(pos, candidate_value) for pos in row_candidate_value_positions if pos not in pair_positions]
                    pointing_pairs.append(PointingPair(box_group.type, box_group.num, (pair_positions[0], pair_positions[1]), candidate_value, removed_candidate_cells))
                    for cell in removed_candidate_cells:
                        self.board_cell_candidates[cell.pos.row_num][cell.pos.col_num].remove_candidate_value(cell.val)
                        row_candidates.remove_group_candidate(cell)

            elif pair_positions[0].col_num == pair_positions[1].col_num:
                col_candidates = self.board_group_candidates[GroupType.COL][pair_positions[0].col_num]
                col_candidate_value_positions = col_candidates.get_positions_for_candidate_value(candidate_value)
                if len(col_candidate_value_positions) > 2:
                    removed_candidate_cells = [Cell(pos, candidate_value) for pos in col_candidate_value_positions if pos not in pair_positions]
                    pointing_pairs.append(PointingPair(box_group.type, box_group.num, (pair_positions[0], pair_positions[1]), candidate_value, removed_candidate_cells))
                    for cell in removed_candidate_cells:
                        self.board_cell_candidates[cell.pos.row_num][cell.pos.col_num].remove_candidate_value(cell.val)
                        col_candidates.remove_group_candidate(cell)
        return pointing_pairs

    def remove_boxed_pair_extra_candidates(self, group: Group) -> list[BoxedPair]:
        assert group.type != GroupType.BOX

        boxed_pairs = []
        group_candidates = self.board_group_candidates[group.type][group.num]
        candidate_values_with_two_cells = group_candidates.get_candidate_values_for_count(2)
        for candidate_value in candidate_values_with_two_cells:
            pair_positions = group_candidates.get_positions_for_candidate_value(candidate_value)
            assert len(pair_positions) == 2
            if Group.pos_to_box_num(pair_positions[0]) == Group.pos_to_box_num(pair_positions[1]):
                box_candidates = self.board_group_candidates[GroupType.BOX][Group.pos_to_box_num(pair_positions[0])]
                box_candidate_value_positions = box_candidates.get_positions_for_candidate_value(candidate_value)
                if len(box_candidate_value_positions) > 2:
                    removed_candidate_cells = [Cell(pos, candidate_value) for pos in box_candidate_value_positions if pos not in pair_positions]
                    boxed_pairs.append(BoxedPair(group.type, group.num, (pair_positions[0], pair_positions[1]), candidate_value, removed_candidate_cells))
                    for cell in removed_candidate_cells:
                        self.board_cell_candidates[cell.pos.row_num][cell.pos.col_num].remove_candidate_value(cell.val)
                        box_candidates.remove_group_candidate(cell)
        return boxed_pairs

    def solve_single_candidate_cells(self) -> list[Cell]:
        solution_history_step = []
        for cell in self.solvable_cells:
            self.board.set_cell(cell)
            row_num = cell.pos.row_num
            col_num = cell.pos.col_num
            box_num = Group.pos_to_box_num(cell.pos)
            for pos in Group.get_row_positions(row_num):
                group_candidate_cell = Cell(pos, cell.val)
                self.board_group_candidates[GroupType.ROW][row_num].remove_group_candidate(group_candidate_cell)
            for pos in Group.get_col_positions(col_num):
                group_candidate_cell = Cell(pos, cell.val)
                self.board_group_candidates[GroupType.COL][col_num].remove_group_candidate(group_candidate_cell)
            for pos in Group.get_box_positions(box_num):
                group_candidate_cell = Cell(pos, cell.val)
                self.board_group_candidates[GroupType.BOX][box_num].remove_group_candidate(group_candidate_cell)
            solution_history_step.append(cell)
            print(f'Set {cell}')
        self.solution_history.append(solution_history_step)
        self.removed_candidates = self.remove_extra_candidates()
        self.solvable_cells = self.gather_solvable_cells()
        return solution_history_step

    def gather_solvable_cells(self) -> list[Cell]:
        single_cell_candidates = self.find_single_candidate_cells()
        single_group_candidates = self.find_single_group_candidate_cells()
        solvable_cells = list(set(single_group_candidates).union(single_cell_candidates))
        return solvable_cells

    def find_single_candidate_cells(self) -> list[Cell]:
        single_candidate_cells = []
        for row_num in range(Config.ROW_SIZE):
            for col_num in range(Config.COL_SIZE):
                pos = Position(row_num, col_num)
                cell = self.board.get_cell(pos)
                cell_candidates = self.board_cell_candidates[row_num][col_num]
                if cell.is_empty() and cell_candidates.is_single_candidate_cell():
                    candidate_value = cell_candidates.get_single_candidate_value()
                    candidate_cell = Cell(pos, candidate_value)
                    print(f'Single Candidate Cell... {candidate_cell}')
                    single_candidate_cells.append(candidate_cell)
        return single_candidate_cells

    def find_single_group_candidate_cells(self) -> list[Cell]:
        single_group_candidate_cells = []
        for group_type in GroupType:
            for group_num in Group.GROUP_NUM_RANGE:
                group_candidates = self.board_group_candidates[group_type][group_num]
                for value in group_candidates.get_candidate_values_for_count(1):
                    pos = group_candidates.get_positions_for_candidate_value(value)[0]
                    print(f'Single Candidate Value Group... {group_type} {group_num}: {pos} - {value}')
                    single_group_candidate_cells.append(Cell(pos, value))
        return single_group_candidate_cells
