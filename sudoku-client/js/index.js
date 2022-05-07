import "../css/main.css";
import {Cell} from "./cell.js"
import {DomUtils} from "./util/dom"

Cell.registerEventListeners();
let c = new Cell(0, 3, null, [1, 2]);
console.log(c);

export {Cell, DomUtils};