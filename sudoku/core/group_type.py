from enum import Enum


class GroupType(Enum):
    ROW = 'Row'
    COL = 'Col'
    BOX = 'Box'

    def __str__(self):
        return self.value