import json

from sudoku.core.position import Position
from sudoku.core.board import Board
from sudoku.solver.board_solver import BoardSolver
from sudoku.api.sudoku_json_encoder import SudokuJSONEncoder


class EventHandler:

    @staticmethod
    def validate_event(event):
        errors = []
        if 'board' not in event:
            errors.append(
                "Event payload must contain 'board' property containing a 9x9 2D list of nulls or numbers from 1-9 inclusive")
            return errors

        board = event['board']
        if not isinstance(board, list):
            errors.append(
                "Event property 'board' must be a 2D list of numbers from 1-9 inclusive. The property 'board' is not a list.")
            return errors

        for r in range(len(board)):
            row = board[r]
            if not isinstance(row, list) and len(row) != 9:
                errors.append(
                    f"Event property 'board' must be a 2D list of numbers from 1-9 inclusive. The value at index '{r}' of 'board' is not a list.")
            for c in range(len(row)):
                num = row[c]
                if num is not None and not isinstance(num, int) and 1 <= num <= 9:
                    errors.append(
                        f"Event property 'board' must be a 2D list of numbers from 1-9 inclusive. The value in row: {r} and col: {c} is not null or a number between 1 and 9 inclusive.")
        return errors

    @staticmethod
    def handle_errors(errors):
        response = dict()
        response['statusCode'] = 400
        response['body'] = errors
        return response

    @staticmethod
    def handle_event(event):
        response = dict()
        board = Board(event['board'])
        is_valid = board.is_valid()

        response['statusCode'] = 200
        response['body'] = dict()
        response['body']['isValid'] = is_valid
        response['body']['conflicts'] = json.loads(json.dumps(board.conflicts, cls=SudokuJSONEncoder))
        if is_valid:
            solver = BoardSolver(board)
            candidates = [solver.board_cell_candidates[row_num][col_num]
                          for row_num in Position.ROW_RANGE
                          for col_num in Position.COL_RANGE
                          if board.get_cell(Position(row_num, col_num)).is_empty()]
            response['body']['candidates'] = json.loads(json.dumps(candidates, cls=SudokuJSONEncoder))
            response['body']['removedCandidates'] = json.loads(json.dumps(solver.removed_candidates, cls=SudokuJSONEncoder))
            response['body']['']
        # ToDo: Add solution Cells.
        return response