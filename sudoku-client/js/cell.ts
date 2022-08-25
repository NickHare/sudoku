import { Value, Row, Col } from "./types";
import { DomUtils } from "./util/dom";
import { KeyUtils } from "./util/keys";
import Joi from "joi";

type CellState = "EMPTY" | "CANDIDATES" | "SET" | "LOCKED";

export class Cell{
    static minRow: number = 0;
    static minCol: number = 0;
    static minBox: number = 0;
    static minVal: number = 1;

    static maxRow: number = 8;
    static maxCol: number = 8;
    static maxBox: number = 8;
    static maxVal: number = 9;

    row: Row;
    col: Col;
    value: Value | null;
    candidates: Value[];
    element: HTMLElement;
    state: CellState;

    static emptyCellState: CellState = "EMPTY";
    static candidatesCellState: CellState = "CANDIDATES";
    static setCellState: CellState = "SET";
    static lockedCellState: CellState = "LOCKED";
    static cellStates: CellState[] = ["EMPTY", "CANDIDATES", "SET", "LOCKED"];

    static cellClassName: string = "sudoku-cell";
    static emptyCellClassName: string = "sudoku-cell-empty";
    static candidatesCellClassName: string = "sudoku-cell-candidates";
    static setCellClassName: string = "sudoku-cell-set";
    static lockedCellClassName: string = "sudoku-cell-locked";
    static candidateValueClassName: string = 'sudoku-cell-candidate';

    static setCellPropertyName = "value";
    static candidateCellPropertyName = "candidateValue";

    static cellStateClassMap: Record<CellState, string> = {
        [Cell.emptyCellState]: Cell.emptyCellClassName,
        [Cell.candidatesCellState]: Cell.candidatesCellClassName,
        [Cell.setCellState]: Cell.setCellClassName,
        [Cell.lockedCellState]: Cell.lockedCellClassName
    } as Record<CellState, string>;
    //Type Assertion used because of bug issue described in https://stackoverflow.com/questions/58760022/computed-property-name-is-not-assignable-to-record-type
    //TLDR - Record types widen when using computed name property cause a compiler type error

    static cellSchemaValidator = Joi.object({
        row: Joi.number().required().min(0).max(8),
        col: Joi.number().required().min(0).max(8),
        value: Joi.number().required().min(1).max(9),
        candidates: Joi.array(),
        element: "",
        state: "",
    });

    static getAllCellElements(): Element[]{
        return DomUtils.getElementsByClass(Cell.cellClassName); 
    }

    static getCellElement(row: Row, col: Col): HTMLElement{
        const id: string = `cell-${row}-${col}`;
        const element: HTMLElement | null = DomUtils.getElementById(id);
        if (element == null) {
            throw new Error(`The expected Element could not be found for id: {id}.`);
        }
        return element;
    }

    // static registerEventListeners(){
    //     const cells = Cell.getAllCellElements();
    //     cells.forEach(cell => cell.addEventListener("keydown", Cell.#cellOnKeyEventHandler));
    // }

    // static #cellOnKeyEventHandler = event => {
    //     const row = parseInt(event.currentTarget.dataset.row);
    //     const col = parseInt(event.currentTarget.dataset.col);
    //     const key = event.key;
    //     console.log(row + ", " + col + ": " + key)
    //     if (isArrowKey(key)){
    //         Cell.#handleArrowKey(row, col, key);
    //     } else if (isDigitKey(key)){
    //         if (event.ctrlKey){

    //         }
    //         Cell.#handleDigitKey(row, col, key);
    //     } else if (key == "Backspace"){
    //         Cell.#handleBackspace(row, col, key);
    //     }
    // }

    // static #handleArrowKey = (row, col, key) => {
    //     let delta_row = 0;
    //     let delta_col = 0;
    //     switch(key){
    //         case "ArrowUp":
    //             delta_row = -1;
    //             break;
    //         case "ArrowDown":
    //             delta_row = 1;
    //             break;
    //         case "ArrowLeft":
    //             delta_col = -1;
    //             break;
    //         case "ArrowRight":
    //             delta_col = 1;
    //             break;
    //     }

    //     let newRow = row + delta_row;
    //     let newCol = col + delta_col;

    //     if (newRow > Cell.maxRow){
    //         newRow = Cell.minRow;
    //     } else if (newRow < Cell.minRow){
    //         newRow = Cell.maxRow;
    //     }

    //     if (newCol > Cell.maxCol){
    //         newCol = Cell.minCol;
    //     } else if (newCol < Cell.minCol){
    //         newCol = Cell.maxCol;
    //     }

    //     let cellElement = Cell.getCellElement(newRow, newCol);
    //     cellElement.focus();
    // }

    // static #handleDigitKey = (row, col, key) => {
    //     let cellElement = Cell.getCellElement(row, col);
    //     cellElement.innerHTML = key;
    // }

    // static #handleCtrlDigitKey = (row, col, key) => {

    // }

    // static #handleBackspace = (row, col, key) => {
    //     let cellElement = Cell.getCellElement(row, col);
    //     cellElement.innerHTML = "";
    // }

    constructor(row: Row, col: Col, state: CellState, value?: Value, candidates?: Value[]){
        this.row = row;
        this.col = col;
        this.value = value ?? null;
        this.candidates = candidates ?? [];
        this.element = Cell.getCellElement(this.row, this.col);
        this.state = state;
        return;
    }

    isEmpty(): boolean {
        return this.state == Cell.emptyCellState && this.value == null && this.candidates == [];
    }
    
    clearCell(): void{
        this.value = null;
        this.candidates = [];
        this.state = Cell.emptyCellState;

        DomUtils.removeAllElementChildNodes(this.element);
        DomUtils.setElementClasses(this.element, [Cell.cellClassName, Cell.emptyCellClassName]);
        return;
    }

    setCell(value: Value): void{
        this.value = value;
        this.candidates = [];
        this.state = Cell.setCellState;
        
        let valueText = DomUtils.createTextNode(value.toString());
        this.element = DomUtils.removeAllElementChildNodes(this.element);
        this.element = DomUtils.addElementChildNode(this.element, valueText);
        this.element = DomUtils.setElementClasses(this.element, [Cell.cellClassName, Cell.setCellClassName]);
        this.element = DomUtils.setElemenetDatasetPropery(this.element, Cell.setCellPropertyName, value.toString());
        return;
    }

    setCandidate(value: Value): void{
        if (!this.candidates.includes(value) && [Cell.emptyCellState, Cell.candidatesCellState].includes(this.state)){
            let index = 0;
            while (this.candidates[index] < value){
                index++;
            }
            this.candidates.splice(index, 0, value);
            this.state = Cell.candidatesCellState;

            this.element = DomUtils.removeAllElementChildNodes(this.element);
            let candidateElements = [...Array(9).keys()]
                .map((index: number): number => index + 1)
                .map((candidate: Value): Element => {
                    let candidateText = DomUtils.createTextNode(candidate.toString());
                    let candidateElement = DomUtils.createElement('div', [Cell.candidateValueClassName]);
                    candidateElement = DomUtils.setElemenetDatasetPropery(candidateElement, Cell.candidateCellPropertyName, candidate.toString());
                    if (this.candidates.includes(candidate)){
                        candidateElement = DomUtils.addElementChildNode(candidateElement, candidateText);
                    }
                    return candidateElement;
                });

            this.element = DomUtils.addElementChildNodes(this.element, candidateElements);
            this.element = DomUtils.setElementClasses(this.element, [Cell.cellClassName, Cell.candidatesCellClassName]);
        }

        return;
    }

    setCandidates(values){
        if ([Cell.emptyCellState, Cell.candidatesCellState].includes(this.state)){
            this.candidates = values;
            this.state = Cell.candidatesCellState;
            
            this.element = DomUtils.removeAllElementChildNodes(this.element);
            let candidateElements = [...Array(9).keys()]
                .map((index: number): number => index + 1)
                .map((candidate: Value): Element => {
                    let candidateText = DomUtils.createTextNode(candidate.toString());
                    let candidateElement = DomUtils.createElement('div', [Cell.candidateValueClassName]);
                    candidateElement = DomUtils.setElemenetDatasetPropery(candidateElement, Cell.candidateCellPropertyName, candidate.toString());
                    if (this.candidates.includes(candidate)){
                        candidateElement = DomUtils.addElementChildNode(candidateElement, candidateText);
                    }
                    return candidateElement;
                });

            this.element = DomUtils.addElementChildNodes(this.element, candidateElements);
            this.element = DomUtils.setElementClasses(this.element, [Cell.cellClassName, Cell.candidatesCellClassName]);
        }

        return;
    }

}