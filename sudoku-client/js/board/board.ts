import { Row, Col, Value } from "root";
import { Cell } from "cell";
import Joi from "joi";

export class Board{
    cellArray: Cell[][];

    constructor(cellArray: Cell[][]){
        this.cellArray = cellArray;
    }
    
    static initEmptyCellBoard(): Board{
        const cellArray: Cell[][] = [];
        for(let i = Cell.minRow; i <= Cell.maxRow; i++){
            let row: Cell[] = [];
            for(let j = Cell.minCol; j <= Cell.maxCol; j++){
                let c: Cell = new Cell(i as Row, j as Col, "EMPTY");
                row.push(c);
            }
            cellArray.push(row);
        }
        return new Board(cellArray);
    }

    static initTestBoard(){
        const jsonArray: (Value | null)[][] = [
            [null, null, null, null, null, null, null, null, null],
            [null, 9, null, 6, null, null, null, null, null],
            [null, 6, null, null, 7, null, 4, null, 3],
            [null, null, 2, null, null, 6, null, null, null],
            [null, null, 8, 1, null, null, null, null, 9],
            [5, null, null, 2, null, null, null, null, null],
            [null, null, null, null, 3, null, null, 5, null],
            [null, null, null, null, 8, 7, null, 2, null],
            [9, 3, null, null, null, null, null, 4, null]
        ];
        return Board.fromJsonArray(jsonArray);
    }

    static fromJsonArray(jsonArray: (Value | null)[][]){
        const cellArray: Cell[][] = jsonArray.map((jsonRow: (Value | null)[], row: Row): Cell[] =>{
            return jsonRow.map((jsonCell: (Value | null), col: Col): Cell => {
                return jsonCell? new Cell(row, col, Cell.setCellState, jsonCell) : new Cell(row, col, Cell.emptyCellState);
            });
        });
        return new Board(cellArray);
    }

    getCell(row: Row, col:Col): Cell{
        return this.cellArray[row][col];
    }

    isCellEmpty(row: Row, col: Col): boolean{
        return this.cellArray[row][col].isEmpty();
    }

    isCellSet(row: Row, col: Col): boolean{
        return this.cellArray[row][col].isSet();
    }

    isCellCandidate(row: Row, col: Col, value: Value): boolean{
        return this.cellArray[row][col].isCandidate(value);
    }

    isCellCandidates(row: Row, col: Col): boolean{
        return this.cellArray[row][col].hasCandidates();
    }

    setCell(row: Row, col: Col, value: Value): Cell{
        this.cellArray[row][col].setCell(value);
        return this.cellArray[row][col];
    }

    clearCell(row: Row, col: Col): Cell{
        this.cellArray[row][col].clearCell();
        return this.cellArray[row][col];
    }

    setCellCandidate(row: Row, col: Col, value: Value): Cell{
        this.cellArray[row][col].setCandidate(value);
        return this.cellArray[row][col];
    }
    
    clearCellCandidate(row: Row, col: Col, value: Value): Cell{
        this.cellArray[row][col].clearCandidate(value);
        return this.cellArray[row][col];
    }

    setCellCandidates(row: Row, col: Col, values: Value[]): Cell{
        this.cellArray[row][col].setCandidates(values);
        return this.cellArray[row][col];
    }

    clearCellCandidates(row: Row, col: Col): Cell{
        this.cellArray[row][col].clearCandidates();
        return this.cellArray[row][col];
    }
}