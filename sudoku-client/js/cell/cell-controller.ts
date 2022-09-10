import { Row, Col, Value } from "../types";
import { Cell, CellState, CellView } from "cell";
import { Board } from "board";
import { KeyUtils } from "utils";


export class CellController{
    cell: Cell;

    constructor(cell: Cell){
        this.cell = cell;
        this.#initCellEventListeners();
        CellView.renderCell(cell);
    }

    #initCellEventListeners(): void{
        let listener = this.#cellClickEventHandler(this.cell);
        CellView.registerCellEventListener(this.cell, "click", listener);
        listener = this.#cellKeyEventHandler(this.cell);
        CellView.registerCellEventListener(this.cell, "keydown", listener);
        return;
    }

    #cellClickEventHandler(cell: Cell): (event: Event) => void{
        return (event: Event): void => {
            // console.log(`Handling MouseEvent: cell: ${cell}`);
            CellView.focusCell(cell);
            return;
        };
    }

    #cellKeyEventHandler(cell: Cell): (event: Event) => void{
        return (event: Event): void => {
            const keyboardEvent: KeyboardEvent = event as KeyboardEvent;
            const key: string = keyboardEvent.key;

            // console.log(`Handling KeyboardEvent: cell: ${cell}, key: ${key}`);
            if (KeyUtils.isDigitKey(keyboardEvent)){
                if (KeyUtils.isCtrlActive(keyboardEvent)){
                    this.#handleCtrlDigitKey(cell, key);
                    event.preventDefault(); //Prevent browser from firing tab change keyboard shortcut
                }else{
                    this.#handleDigitKey(cell, key);
                }
            } else if (KeyUtils.isBackspaceKey(keyboardEvent)){
                this.#handleBackspace(cell);
            }
            return;
        };
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

    #handleBackspace(cell: Cell): void{
        cell.clearCell();
        CellView.renderCell(cell);        
        return;
    }
}