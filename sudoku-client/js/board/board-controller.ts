import { Row, Col, Value } from "..";
import { Cell, CellState } from "cell";
import { Board } from "board";
import { KeyUtils } from "utils";

export class BoardController{
    board: Board;

    constructor(){
        this.board = BoardController.#initEmptyCellBoard();
    }
        

    static #initEmptyCellBoard(): Board{
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
}