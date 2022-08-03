import { DomUtils } from "./util/dom";
import { isArrowKey, isDigitKey } from "./util/keys";
import { validate } from "validate.js";


export class Cell{
    // static minRow: number = 0;
    // static minCol: number = 0;
    // static minBox: number = 0;
    // static minVal: number = 1;

    // static maxRow: number = 8;
    // static maxCol: number = 8;
    // static maxBox: number = 8;
    // static maxVal: number = 9;

    // row: number;
    // col: number;
    // value: number;
    // candidates: number[];
    // element: HTMLElement;
    // state: string;

    // static cellClassName = "sudoku-cell";
    // static emptyCellClassName = "sudoku-cell-empty";
    // static candidatesCellClassName = "sudoku-cell-candidates";
    // static setCellClassName = "sudoku-cell-set";
    // static lockedCellClassName = "sudoku-cell-locked";
    // static candidateValueClassName = 'sudoku-cell-candidate';

    // static emptyCellState = "EMPTY";
    // static candidatesCellState = "CANDIDATES";
    // static setCellState = "SET";
    // static lockedCellState = "LOCKED";
    // static cellStates = ["EMPTY", "CANDIDATES", "SET", "LOCKED"];

    // static cellStateClassMap = {
    //     [Cell.emptyCellState]: Cell.emptyCellClassName,
    //     [Cell.candidatesCellState]: Cell.candidatesCellClassName,
    //     [Cell.setCellState]: Cell.setCellClassName,
    //     [Cell.lockedCellState]: Cell.lockedCellClassName
    // };
    
    // static validate = validate;
    // static cellStateValidator = (value, options, key, attributes) => {
    //     let cellValue = attributes.value;
    //     let cellCandidates = attributes.candidates;
    //     let cellElement = attributes.element;
    //     let cellElementClasses = DomUtils.getElementClasses(cellElement);
    //     let cellElementChildNodes = DomUtils.getElementChildNodes(cellElement);
    //     let cellState = value;
    //     let messages = []

    //     // Validate cell value
    //     if (validate.isDefined(cellValue) && [this.emptyCellState, this.candidatesCellState].includes(cellState)){
    //         messages.push(`Cell property 'state' is invalid. Property 'value' must not be defined if Cell is in ${cellState} state. state: ${cellState}, value: ${cellValue}`);
    //     }
    //     if (!validate.isDefined(cellValue) && [this.setCellState, this.lockedCellState].includes(cellState)){
    //         messages.push(`Cell property 'state' is invalid. Property 'value' must be defined if Cell is in ${cellState} state. state: ${cellState}, value: ${cellValue}`);
    //     }

    //     // Validate cell candidates
    //     if (!validate.isEmpty(cellCandidates) && [this.setCellState, this.lockedCellState].includes(cellState)){
    //         messages.push(`Cell property 'state' is invalid. Property 'candidates' must be empty if Cell is in ${cellState} state. state: ${cellState}, candidates: ${cellCandidates}`);
    //     }

    //     // Validate cell class
    //     if (!cellElementClasses.includes(this.cellClassName)){
    //         messages.push(`Cell property 'state' is invalid. Property 'element.classList' must contain ${this.cellClassName} class. element.classList: ${cellElementClasses}`);
    //     }
    //     if (!cellElementClasses.includes(Cell.cellStateClassMap[cellState])){
    //         messages.push(`Cell property 'state' is invalid. Property 'element.classList' must contain ${Cell.cellStateClassMap[cellState]} class if Cell is in ${cellState}. element.classList: ${cellElementClasses}`);
    //     }

    //     // Validate element DOM
    //     if (cellState == this.emptyCellState){
    //         if (cellElementChildNodes.length > 0){
    //             messages.push(`Cell property 'state' is invalid. Property 'element.childNodes' must be empty if Cell is in ${cellState} state. state: ${cellState}, element.childNodes: ${cellElementChildNodes.map(node => DomUtils.isTextNode(node)? JSON.stringify(node.textContent.trim()) : node.tagName)}`);
    //         }

    //         let nonEmptyStateClasses = this.cellStates.filter(state => state != this.emptyCellState);
    //         if (cellElementClasses.some(className => nonEmptyStateClasses.includes(className))){
    //             messages.push(`Cell property 'state' is invalid. Property 'element.classList' must not contain ${nonEmptyStateClasses} if Cell is in ${cellState} state. state: ${cellState}, element.classList: ${cellElementClasses}`);
    //         }
    //     }

    //     if (cellState == this.setCellState){
    //         if (cellElementChildNodes.length != 1 || cellElementChildNodes[0].textContent < Cell.minVal || cellElementChildNodes[0].textContent > Cell.maxVal){
    //             messages.push(`Cell property 'state' is invalid. Property 'element.childNodes' must have 1 childNode containing a number between 1 and 9 inclusive if Cell is in ${cellState} state. state: ${cellState}, element.childNodes: ${cellElementChildNodes.map(node => DomUtils.isTextNode(node)? JSON.stringify(node.textContent.trim()) : node.tagName)}}`);
    //         }
            
    //         let nonSetStateClasses = this.cellStates.filter(state => state != this.setCellState);
    //         // if (){
    //         //     messages.push(`Cell property 'state' is invalid. Property 'element.childNodes' must be empty if Cell is in ${cellState} state. state: ${cellState}, element.childNodes: ${cellElementChildNodes.map(node => DomUtils.isTextNode(node)? JSON.stringify(node.textContent.trim()) : node.tagName)}}`);
    //         // }
    //     }

    //     return messages;
    // };
    // static {
    //     Cell.validate.validators.cellState = Cell.cellStateValidator;
    // }
    // static cellConstraints = {
    //     row: {
    //         presence: {
    //             message: value => `Cell property 'row' is not present. Property must be an integer between ${Cell.minRow} and ${Cell.maxRow}. row: ${value}`,
    //         },
    //         numericality: {
    //             noStrings: true,
    //             onlyInteger: true,
    //             greaterThanOrEqualTo: 0,
    //             lessThanOrEqualTo: 8,
    //             message: value => `Cell property 'row' is not valid. Property must be an integer between ${Cell.minRow} and ${Cell.maxRow}. row: ${value}`,
    //         },
    //     },
    //     col: {
    //         presence: {
    //             message: value => `Cell property 'col' is not present. Property must be an integer between ${Cell.minCol} and ${Cell.maxCol}. col: ${value}`,
    //         },
    //         numericality: {
    //             noStrings: true,
    //             onlyInteger: true,
    //             greaterThanOrEqualTo: 0,
    //             lessThanOrEqualTo: 8,
    //             message: value => `Cell property 'col' is not valid. Property must be an integer between ${Cell.minCol} and ${Cell.maxCol}. col: ${value}`,
    //         },
    //     },
    //     value: {
    //         numericality: {
    //             noStrings: true,
    //             onlyInteger: true,
    //             greaterThanOrEqualTo: 1,
    //             lessThanOrEqualTo: 9,
    //             message: value => `Cell property 'value' is not valid. Property must be an integer between ${Cell.minVal} and ${Cell.maxVal}. value: ${value}`,
    //         },
    //     },
    //     candidates: {
    //         presence: {
    //             message: value => `Cell property 'candidates' is not present. Property must be an array of up to ${Cell.maxVal} integers between ${Cell.minVal} and ${Cell.maxVal}. candidates: ${value}`,
    //         },
    //         type: {
    //             type: values => validate.isArray(values) && !values.some(value => !validate.isInteger(value) || value < Cell.minVal || value > Cell.maxVal),
    //             message: value => `Cell property 'candidates' is not a valid type. Property must be an array of up to ${Cell.maxVal} integers between ${Cell.minVal} and ${Cell.maxVal}. candidates: ${value}, type: ${value.constructor.name}`,
    //         },
    //         length: {
    //             minimum: 0,
    //             maximum: 9,
    //             message: value => `Cell property 'candidates' does not have a valid length. Property must be an array of up to ${Cell.maxVal} integers between ${Cell.minVal} and ${Cell.maxVal}. candidates: ${value}`,
    //         },
    //     },
    //     element: {
    //         presence: {
    //             message: value => `Cell property 'element' is not valid type. Property must be a DOMElement. element: ${value}`,
    //         },
    //         type: {
    //             type: value => validate.isDomElement(value),
    //             message: value => `Cell property 'element' is not valid type. Property must be a DOMElement representing the cell. element: ${value}, type: ${value.constructor.name}`,
    //         },
    //     },
    //     state: {
    //         type: {
    //             type: value => validate.isString(value) && Cell.cellStates.includes(value),
    //             message: value => `Cell property 'state' is not a valid type. Property must be a string containing one of the following values: ${Cell.cellStates}. state: ${value}, type: ${value.constructor.name}`,
    //         },
    //         cellState: true,
    //     },
    // };

    // static getAllCellElements(){
    //     return DomUtils.getElementsByClass(Cell.cellClassName);
    // }

    // static getCellElement(row, col){
    //     // if (typeof(row) != "number" || row < Cell.minRow || row > Cell.maxRow){
    //     //     throw new Error(`Cell argument 'row' is invalid. Argument must be a number between ${Cell.minRow} and ${Cell.maxRow}. row: ${row}`);
    //     // }
    //     // if (typeof(col) != "number" || col < Cell.minCol || col > Cell.maxCol){
    //     //     throw new Error(`Cell argument 'col' is invalid. Argument must be a number between ${Cell.minCol} and ${Cell.maxCol}. col: ${col}`);
    //     // }
    //     const id = `cell-${row}-${col}`;
    //     return DomUtils.getElementById(id);
    // }

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

    // constructor(row, col, value=null, candidates=[], state=Cell.emptyCellState){
    //     // if (typeof(row) != "number" || row < Cell.minRow || row > Cell.maxRow){
    //     //     throw new Error(`Cell argument 'row' is invalid. Argument must be a number between ${Cell.minRow} and ${Cell.maxRow} indicating the cell row number. row: ${row}`);
    //     // }
    //     // if (typeof(col) != "number" || col < Cell.minCol || col > Cell.maxCol){
    //     //     throw new Error(`Cell argument 'col' is invalid. Argument must be a number between ${Cell.minCol} and ${Cell.maxCol} indicating the cell column number. col: ${col}`);
    //     // }
    //     // if (value != null && typeof(value) != "number" && (value < Cell.minVal && value > Cell.maxVal)){
    //     //     throw new Error(`Cell argument 'value' is invalid. Argument must be null or a number between ${Cell.minVal} and ${Cell.maxVal} indicating the cell value. value: ${value}`);
    //     // }
    //     // if (typeof(locked) != "boolean"){
    //     //     throw new Error(`Cell argument 'locked' is invalid. Argument must be a boolean. candidates: ${candidates}`);
    //     // }
    //     // if (!Array.isArray(candidates) || candidates.some(val => val < Cell.minVal && val > Cell.maxVal) || new Set(candidates).size != candidates.length){
    //     //     throw new Error(`Cell argument 'candidates' is invalid. Argument must be null or an array of unique candidate values. candidates: ${candidates}`);
    //     // }
    //     // if (value != null && candidates != null){
    //     //     throw new Error(`Cell state is invalid. Properties 'value' and 'candidates' can not both be not null. value: ${value}, candidates: ${candidates}`);
    //     // }
    //     this.row = row;
    //     this.col = col;
    //     this.value = value;
    //     this.candidates = candidates;
    //     this.element = Cell.getCellElement(this.row, this.col);
    //     this.state = state;
    //     let result = Cell.validate.validate(this, Cell.cellConstraints, {fullMessages: false});
    //     console.log(result);
    // }

    // isEmpty(){
    //     console.log(this);
    //     return this.state == Cell.emptyCellState;
    // }
    
    // clearCell(){
    //     this.value = null;
    //     this.candidates = null;
    //     this.state = Cell.emptyCellState
    //     DomUtils.removeAllElementChildNodes(this.element);
    //     DomUtils.setElementClasses(this.element, [Cell.cellClassName, Cell.emptyCellClassName]);
    // }

    // setCell(value){
    //     if (value != null && typeof(value) != "number" && (value < Cell.minVal && value > Cell.maxVal)){
    //         throw new Error(`Cell argument 'value' is invalid. Argument must be null or a number between ${Cell.minVal} and ${Cell.maxVal}. value: ${value}`);
    //     }
    //     this.value = value;
    //     this.candidates = null;
        
    //     let text = DomUtils.createTextNode(value.toString());
    //     DomUtils.removeElementChildNodes(this.element);
    //     DomUtils.addElementChildNode(this.element, text);
    //     DomUtils.setElementClasses(this.element, [Cell.cellClassName, Cell.setCellClassName]);
    // }

    // setCandidate(value){
    //     if (value != null && typeof(value) != "number" && (value < Cell.minVal && value > Cell.maxVal)){
    //         throw new Error(`Cell argument 'value' is invalid. Argument must be null or a number between ${Cell.minVal} and ${Cell.maxVal}. value: ${value}`);
    //     }

    //     if (!this.candidates.includes(value)){
    //         let index = 0;
    //         while (this.candidates[index] < value){
    //             index++;
    //         }
    //         this.candidates.splice(index, 0, value);
    //         let candidateValue = DomUtils.createElement('div', [Cell.candidateValueClassName]);
    //         DomUtils.addElementChildNodeBefore(this.element, candidateValue, index)
    //     }
    // }

    // setCandidates(candidates){
    //     if (candidates != null && (!Array.isArray(candidates) || (candidates.some(val => val < Cell.minVal && val > Cell.maxVal) || (new Set(candidates)).size != candidates.length))){
    //         throw new Error(`Cell arguments 'candidates' is invalid. Argument must be null or an array of unique candidate values. candidates: ${candidates}`);
    //     }
    //     this.state = Cell.candidatesCellState;
    //     this.value = null;
    //     this.candidates = candidates.sort();
    //     DomUtils.setElementClasses(this.element, [Cell.cellClassName, Cell.candidatesCellClassName]);
    //     DomUtils.removeAllElementChildNodes(this.element);
    //     DomUtils.addElementChileNodes(this.element, candidates.map(candidate => DomUtils.createElement('div', [Cell.candidateValueClassName])));
    // }

}