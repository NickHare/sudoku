import { getElementById, getElementsByClassName } from "./util/dom";
import { isArrowKey, isDigitKey } from "./util/keys";

export class Cell{
    static maxRow = 8;
    static maxCol = 8;
    static maxBox = 8;
    static minRow = 0;
    static minCol = 0;
    static minBox = 0;
    static minVal = 1;
    static maxVal = 9;
    static cellClassName = "sudoku-cell";

    static getAllCellElements(){
        return getElementsByClassName(Cell.cellClassName);
    }

    static getCellElement(row, col){
        if (typeof(row) != "number" || row < Cell.minRow || row > Cell.maxRow){
            throw new Error(`Cell argument 'row' is invalid. Argument must be a number between ${Cell.minRow} and ${Cell.maxRow}. row: ${row}`);
        }
        if (typeof(col) != "number" || col < Cell.minCol || col > Cell.maxCol){
            throw new Error(`Cell argument 'col' is invalid. Argument must be a number between ${Cell.minCol} and ${Cell.maxCol}. col: ${col}`);
        }
        const id = `cell-${row}-${col}`;
        return getElementById(id);
    }

    static registerEventListeners(){
        const cells = Cell.getAllCellElements();
        cells.forEach(cell => cell.addEventListener("keydown", Cell.#cellOnKeyEventHandler));
    }

    static #cellOnKeyEventHandler = event => {
        const row = parseInt(event.currentTarget.dataset.row);
        const col = parseInt(event.currentTarget.dataset.col);
        const key = event.key;
        console.log(row + ", " + col + ": " + key)
        if (isArrowKey(key)){
            Cell.#handleArrowKey(row, col, key);
        } else if (isDigitKey(key)){
            if (event.ctrlKey){

            }
            Cell.#handleDigitKey(row, col, key);
        } else if (key == "Backspace"){
            Cell.#handleBackspace(row, col);
        }
    }

    static #handleArrowKey = (row, col, key) => {
        let delta_row = 0;
        let delta_col = 0;
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

        let newRow = row + delta_row;
        let newCol = col + delta_col;

        if (newRow > Cell.maxRow){
            newRow = Cell.minRow;
        } else if (newRow < Cell.minRow){
            newRow = Cell.maxRow;
        }

        if (newCol > Cell.maxCol){
            newCol = Cell.minCol;
        } else if (newCol < Cell.minCol){
            newCol = Cell.maxCol;
        }

        let cellElement = Cell.getCellElement(newRow, newCol);
        cellElement.focus();
    }

    static #handleDigitKey = (row, col, key) => {
        let cellElement = Cell.getCellElement(row, col);
        cellElement.innerHTML = key;
    }

    static #handleCtrlDigitKey = (row, col, key) => {

    }

    static #handleBackspace = (row, col, key) => {
        let cellElement = Cell.getCellElement(row, col);
        cellElement.innerHTML = "";
    }

    constructor(row, col, value=null, candidates=[]){
        if (typeof(row) != "number" || row < Cell.minRow || row > Cell.maxRow){
            throw new Error(`Cell argument 'row' is invalid. Argument must be a number between ${Cell.minRow} and ${Cell.maxRow}. row: ${row}`);
        }
        if (typeof(col) != "number" || col < Cell.minCol || col > Cell.maxCol){
            throw new Error(`Cell argument 'col' is invalid. Argument must be a number between ${Cell.minCol} and ${Cell.maxCol}. col: ${col}`);
        }
        if (value != null && typeof(value) != "number" && (value < Cell.minVal && value > Cell.maxVal)){
            throw new Error(`Cell argument 'value' is invalid. Argument must be null or a number between ${Cell.minVal} and ${Cell.maxVal}. value: ${value}`);
        }
        if (candidates != null && (!Array.isArray(candidates) || (candidates.some(val => val < Cell.minVal && val > Cell.maxVal) || (new Set(candidates)).size != candidates.length))){
            throw new Error(`Cell arguments 'candidates' is invalid. Argument must be null or an array of unique candidate values. candidates: ${candidates}`);
        }

        this.row = row;
        this.col = col;
        this.value = value;
        this.candidates = candidates.sort();
    }

    isEmpty(){
        return this.value == null;
    }

    isSet(){
        return this.value != null;
    }

    getValue(){
        return this.value;
    }

    getCandidates(){
        return this.candidates;
    }

    setValue(value){
        if (value != null && typeof(value) != "number" && (value < Cell.minVal && value > Cell.maxVal)){
            throw new Error(`Cell argument 'value' is invalid. Argument must be null or a number between ${Cell.minVal} and ${Cell.maxVal}. value: ${value}`);
        }
        this.value = value;
        return this.value;
    }

    setCandidates(candidates){
        if (candidates != null && (!Array.isArray(candidates) || (candidates.some(val => val < Cell.minVal && val > Cell.maxVal) || (new Set(candidates)).size != candidates.length))){
            throw new Error(`Cell arguments 'candidates' is invalid. Argument must be null or an array of unique candidate values. candidates: ${candidates}`);
        }
        this.candidates = candidates.sort();
        return this.candidates;
    }

    clearCell(){
        let cell = Cell.getCellElement(row, col);
        cell.innerHTML = "";
    }
    
    setCell(value){
        if (value != null && typeof(value) != "number" && (value < Cell.minVal && value > Cell.maxVal)){
            throw new Error(`Cell argument 'value' is invalid. Argument must be null or a number between ${Cell.minVal} and ${Cell.maxVal}. value: ${value}`);
        }
        this.value = value;
        this.candidates = null;
        
        let cell = Cell.getCellElement(row, col);
        cell.innerHTML = value.toString();
    }

}