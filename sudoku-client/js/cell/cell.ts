import { Row, Col, Value } from "root";
import Joi from "joi";

export type CellState = "EMPTY" | "CANDIDATES" | "SET" | "LOCKED";

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
    state: CellState;

    static emptyCellState: CellState = "EMPTY";
    static candidatesCellState: CellState = "CANDIDATES";
    static setCellState: CellState = "SET";
    static lockedCellState: CellState = "LOCKED";
    static cellStates: CellState[] = ["EMPTY", "CANDIDATES", "SET", "LOCKED"];

    static cellSchemaValidator = Joi.object({
        row: Joi.number().required().min(0).max(8),
        col: Joi.number().required().min(0).max(8),
        value: Joi.number().required().min(1).max(9),
        candidates: Joi.array(),
        element: "",
        state: "",
    });

    constructor(row: Row, col: Col, state: CellState, value?: Value, candidates?: Value[]){
        this.row = row;
        this.col = col;
        this.value = value ?? null;
        this.candidates = candidates ?? [];
        this.state = state;
        return;
    }

    isEmpty(): boolean {
        return this.state == Cell.emptyCellState && this.value == null && this.candidates.length == 0;
    }
    
    clearCell(): void{
        this.value = null;
        this.candidates = [];
        this.state = Cell.emptyCellState;
        return;
    }

    isSet(): boolean{
        return this.state == Cell.setCellState && this.value != null && this.candidates.length == 0;
    }

    setCell(value: Value): void{
        this.value = value;
        this.candidates = [];
        this.state = Cell.setCellState;
        return;
    }

    isCandidate(value: Value): boolean{
        return [Cell.candidatesCellState, Cell.lockedCellState].includes(this.state) && this.candidates.includes(value);
    }

    setCandidate(value: Value): void{
        if (!this.candidates.includes(value) && [Cell.emptyCellState, Cell.candidatesCellState].includes(this.state)){
            let index = 0;
            while (this.candidates[index] < value) index++;

            this.value = null;
            this.candidates.splice(index, 0, value);
            this.state = Cell.candidatesCellState;
        }
        return;
    }

    clearCandidate(value: Value): void{
        if (this.candidates.includes(value) && [Cell.candidatesCellState].includes(this.state)){
            let index = 0;
            while (this.candidates[index] < value) index++;

            this.value = null;
            this.candidates.splice(index, 1);
            this.state = (this.candidates.length > 0)? Cell.candidatesCellState : Cell.emptyCellState;
        }
        return;
    }

    hasCandidates(): boolean{
        return [Cell.candidatesCellState, Cell.lockedCellState].includes(this.state) && this.candidates.length != 0;
    }

    setCandidates(values: Value[]): void{
        if ([Cell.emptyCellState, Cell.candidatesCellState].includes(this.state)){
            this.value = null;
            this.candidates = values;
            this.state = (this.candidates.length > 0)? Cell.candidatesCellState : Cell.emptyCellState;
        }
        return;
    }

    clearCandidates(): void{
        if (this.state == Cell.candidatesCellState){
            this.value = null;
            this.candidates = [];
            this.state = Cell.emptyCellState;
        }
        return;
    }

    toString(){
        return `<${this.state} (${this.row},${this.col}): ${this.value} - ${this.candidates}>`;
    }
}