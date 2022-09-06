import { Row, Col, Value } from "../types";
import { Cell, CellState, CellView } from "cell";
import { Board } from "board";
import { KeyUtils } from "utils";


export class CellController{
    board: Board;

    constructor(board: Board){
        this.board = board;
        this.#initCellEventListeners();
    }

    renderAllCells(){
        this.board.cellArray.forEach((cellRow: Cell[]): void => {
            cellRow.forEach((cell: Cell): void => {
                CellView.renderCell(cell);
                return;
            });
            return;
        })
    }

    #initCellEventListeners(): void{
        this.board.cellArray.forEach((cellRow: Cell[]): void => {
            cellRow.forEach((cell: Cell) => {
                let listener = this.#initCellClickEventHandler(cell);
                CellView.registerCellEventListener(cell, "click", listener);
                listener = this.#initCellKeyEventHandler(cell);
                CellView.registerCellEventListener(cell, "keydown", listener);
                return;
            });
        });
    }

    #initCellClickEventHandler(cell: Cell): (event: Event) => void{
        return (event: Event): void => {
            // console.log(`Handling MouseEvent: cell: ${cell}`);
            CellView.focusCell(cell);
            return;
        }
    }

    #initCellKeyEventHandler(cell: Cell): (event: Event) => void{
        return (event: Event): void => {
            const keyboardEvent: KeyboardEvent = event as KeyboardEvent;
            const key: string = keyboardEvent.key;

            // console.log(`Handling KeyboardEvent: cell: ${cell}, key: ${key}`);
            if (KeyUtils.isArrowKey(keyboardEvent)){
                this.#handleArrowKey(cell, key);
            } else if (KeyUtils.isDigitKey(keyboardEvent)){
                if (KeyUtils.isCtrlActive(keyboardEvent)){
                    this.#handleCtrlDigitKey(cell, key);
                    event.preventDefault(); //Prevent browser from firing tab change keyboard shortcut
                }else{
                    this.#handleDigitKey(cell, key);
                }
            } else if (KeyUtils.isBackspace(keyboardEvent)){
                this.#handleBackspace(cell, key);
            }
            return;
        }
    }

    #handleArrowKey(cell: Cell, key: string): void{
        let delta_row: 0 | 1 | -1 = 0;
        let delta_col: 0 | 1 | -1 = 0;
        switch(key){
            case "ArrowUp":
                delta_row = -1;
                break;
            case "ArrowDown":
                delta_row = 1;
                break;
            case "ArrowLeft":
                delta_col = -1;
                break;
            case "ArrowRight":
                delta_col = 1;
                break;
        }

        let newRow: Row = cell.row + delta_row as Row;
        newRow = (newRow > Cell.maxRow)? Cell.minRow as Row : newRow;
        newRow = (newRow < Cell.minRow)? Cell.maxRow as Row : newRow;
        
        let newCol: Col = cell.col + delta_col as Col;
        newCol = (newCol > Cell.maxCol)? Cell.minCol as Col : newCol;
        newCol = (newCol < Cell.minCol)? Cell.maxCol as Col : newCol;

        const newCell: Cell = this.board.getCell(newRow, newCol);
        CellView.focusCell(newCell);
        return;
    }

    #handleDigitKey(cell: Cell, key: string): void{
        const value: Value = parseInt(key) as Value;
        cell.setCell(value);
        CellView.renderCell(cell);
        return;
    }

    #handleCtrlDigitKey(cell: Cell, key: string): void{
        if (cell.isEmpty() || cell.hasCandidates()){
            const value: Value = parseInt(key) as Value;
            if (!cell.isCandidate(value)){
                cell.setCandidate(value);
            } else {
                cell.clearCandidate(value);
            }
            CellView.renderCell(cell);
        }
        return;
    }

    #handleBackspace(cell: Cell, key: string): void{
        cell.clearCell();
        CellView.renderCell(cell);        
        return;
    }
}