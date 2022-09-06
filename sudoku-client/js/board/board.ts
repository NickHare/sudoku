import { Row, Col, Value } from "root";
import { Cell } from "cell";
import Joi from "joi";

export class Board{
    cellArray: Cell[][];

    constructor(cellArray: Cell[][]){
        this.cellArray = cellArray;
    }

    getCell(row: Row, col:Col): Cell{
        return this.cellArray[row][col];
    }

//     isCellEmpty(row: Row, col: Col): boolean{
//         return this.cellArray[row][col].isEmpty();
//     }

//     clearCell(row: Row, col: Col): Cell{
//         this.cellArray[row][col].clearCell();
//         return this.cellArray[row][col];
//     }

//     isCellSet(row: Row, col: Col): boolean{
//         return this.cellArray[row][col].isSet();
//     }

//     setCell(row: Row, col: Col, value: Value): Cell{
//         this.cellArray[row][col].setCell(value);
//         return this.cellArray[row][col];
//     }

//     isCellCandidate(row: Row, col: Col, value: Value): boolean{
//         return this.cellArray[row][col].isCandidate(value);
//     }

//     setCellCandidate(row: Row, col: Col, value: Value): Cell{
//         this.cellArray[row][col].setCandidate(value);
//         return this.cellArray[row][col];
//     }
    
//     clearCellCandidate(row: Row, col: Col, value: Value): Cell{
//         this.cellArray[row][col].clearCandidate(value);
//         return this.cellArray[row][col];
//     }

//     isCellCandidates(row: Row, col: Col): boolean{
//         return this.cellArray[row][col].hasCandidates();
//     }

//     setCellCandidates(row: Row, col: Col, values: Value[]): Cell{
//         this.cellArray[row][col].setCandidates(values);
//         return this.cellArray[row][col];
//     }

//     clearCellCandidates(row: Row, col: Col): Cell{
//         this.cellArray[row][col].clearCandidates();
//         return this.cellArray[row][col];
//     }
}