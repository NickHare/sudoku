import { Row, Col, Value } from "..";
import { Cell, CellState, CellView } from "cell";
import { Board, BoardView } from "board";
import { KeyUtils } from "utils";

export class BoardController{
    board: Board;
    test: null | string;

    constructor(board: Board){
        this.board = board;
        this.#initBoardEventListeners();
        this.test = null;
    }

    #initBoardEventListeners(): void{
        const listener: (event: Event) => void = this.#boardKeyEventHandler();
        const listeners: ((event: Event) => void)[][] = this.board.cellArray
        .map((cellRow: Cell[]): ((event: Event) => void)[] => {
            return cellRow.map((cell: Cell): (event: Event) => void => {
                return this.#cellKeyEventHandler(cell);
            });
        });

        BoardView.registerBoardEventListener("keydown", listener);
        listeners.forEach((listenerRow: ((event: Event) => void)[], row: Row): void => {
            listenerRow.forEach((listener: (event: Event) => void, col: Col): void => {
                CellView.registerCellEventListener(this.board.getCell(row, col), "keydown", listener);
                return;
            });
        });
        return;
    }

    #boardKeyEventHandler(): (event: Event) => void {
        return (event: Event) => {
            const keyboardEvent: KeyboardEvent = event as KeyboardEvent;
            const key: string = keyboardEvent.key;

            if (KeyUtils.isEnterKey(keyboardEvent)) {
                this.#handleEnterKey();
            }
        };
    }

    #cellKeyEventHandler(cell: Cell): (event: Event) => void {
        return (event: Event) => {
            const keyboardEvent: KeyboardEvent = event as KeyboardEvent;
            const key: string = keyboardEvent.key;

            if (KeyUtils.isArrowKey(keyboardEvent)){
                this.#handleArrowKey(cell, key);
            }
        };
    }


    #handleEnterKey(): void{
        const jsonPayload = {
            board: this.board.cellArray.map((cellRow: Cell[]): (Value | null)[] => {
                return cellRow.map((cell: Cell): (Value | null) => {
                    return cell.isSet()? cell.value : null;
                })
            }),
        };
        const url = "https://sudoku.nickhare.ca/";
        const options: RequestInit = {
            headers: {
                "Content-Type": "application/json",
            },
            method: "POST",
            body: JSON.stringify(jsonPayload),
            // mode: "no-cors",
        };
        fetch(url, options)
        .then((res: Response): Promise<any> => res.json())
        .then((res): void => {
            this.test = res;
            res.candidates.forEach((candidate) => {
                this.board.setCellCandidates(candidate.pos.row, candidate.pos.col, candidate.candidate_values);
                CellView.renderCell(this.board.getCell(candidate.pos.row, candidate.pos.col));
            });
            // res.removedCandidates.forEach((removedCandidate): void => {
            //     removedCandidate.eliminated_candidates.forEach((candidate): void => {
            //         let cell = this.board.getCell(candidate.pos.row, candidate.pos.col);
            //         if (cell.hasCandidates() && cell.isCandidate(candidate.val)){
            //             CellView.removeCellCandidateValue(cell, candidate.val);
            //         }
            //     });
            // });
        });
        return;
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
}