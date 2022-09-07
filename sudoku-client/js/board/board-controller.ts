import { Row, Col, Value } from "..";
import { Cell, CellState } from "cell";
import { Board } from "board";
import { KeyUtils } from "utils";

export class BoardController{
    board: Board;
    test: null | string;

    constructor(){
        this.board = BoardController.#initTestBoard();
        this.test = null;
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

    static #initTestBoard(){
        const jsonArray: (Value | null)[][] = [
            [null,null,null,7,9,8,null,null,null],
            [null,null,null,null,1,null,2,5,null],
            [null,null,null,null,2,null,3,null,null],
            [7,null,9,null,null,null,null,null,2],
            [null,null,null,null,null,null,null,7,null],
            [null,null,8,null,null,1,null,9,null],
            [null,5,null,null,null,null,null,null,6],
            [2,null,null,null,null,6,null,null,null],
            [null,1,null,8,null,null,null,null,null]
        ];
        return Board.fromJsonArray(jsonArray);
    }

    #initBoardKeyEventHandler(): (event: Event) => void {
        return (event: Event) => {
            const keyboardEvent: KeyboardEvent = event as KeyboardEvent;
            const key: string = keyboardEvent.key;

            if (KeyUtils.isEnterKey(keyboardEvent)){
                this.handleEnterKey();
            }
        };
    }

    handleEnterKey(): void{
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
            this.test = res.body;
        });
        return;
    }
}