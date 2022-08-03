import "../css/main.css";
import {Cell} from "./cell";
import {DomUtils} from "./util/dom";
import {Point, distance} from "./test";
import Ajv from "ajv";

// Cell.registerEventListeners();
// let c = new Cell(0, 3, null, [1, 2]);
// console.log(c);
const a = new Ajv();
export {Cell, DomUtils, Point, distance, Ajv};