import json
from sudoku.core.position import Position
from sudoku.core.value import Value
from sudoku.core.cell import Cell
from sudoku.core.group_type import GroupType
from sudoku.core.conflict import Conflict
from sudoku.solver.cell_candidates import CellCandidates
from sudoku.solver.naked_pair import NakedPair
from sudoku.solver.hidden_pair import HiddenPair
from sudoku.solver.pointing_pair import PointingPair
from sudoku.solver.boxed_pair import BoxedPair


class SudokuJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if type(obj) in [Cell, Conflict, CellCandidates, ]:
            return obj.__dict__
        elif type(obj) in [NakedPair, HiddenPair, PointingPair, BoxedPair]:
            json = obj.__dict__
            json['strategy'] = obj.__class__.__name__
            return json
        elif type(obj) == GroupType:
            return obj.name
        elif type(obj) == Value:
            return obj.num
        elif type(obj) == Position:
            return {'row': obj.row_num, 'col': obj.col_num}
        else:
            return super().default(obj)
