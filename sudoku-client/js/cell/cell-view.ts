import { Value } from "..";
import { Cell } from "cell";
import { DomUtils } from "utils";

export class CellView{

    static cellClassName: string = "sudoku-cell";
    static emptyCellClassName: string = "sudoku-cell-empty";
    static candidatesCellClassName: string = "sudoku-cell-candidates";
    static setCellClassName: string = "sudoku-cell-set";
    static lockedCellClassName: string = "sudoku-cell-locked";
    static candidateValueClassName: string = 'sudoku-cell-candidate';

    static setCellPropertyName = "value";
    static candidateCellPropertyName = "candidateValue";

    // static cellStateClassMap: Record<CellState, string> = {
    //     [Cell.emptyCellState]: CellView.emptyCellClassName,
    //     [Cell.candidatesCellState]: CellView.candidatesCellClassName,
    //     [Cell.setCellState]: CellView.setCellClassName,
    //     [Cell.lockedCellState]: CellView.lockedCellClassName,
    // } as Record<CellState, string>;
    //Type Assertion used because of bug issue described in https://stackoverflow.com/questions/58760022/computed-property-name-is-not-assignable-to-record-type
    //TLDR - Record types widen when using computed name property cause a compiler type error


    static #getAllCellElements(): Element[]{
        return DomUtils.getElementsByClass(CellView.cellClassName); 
    }

    static #getCellElement(cell: Cell): HTMLElement{
        const id: string = `cell-${cell.row}-${cell.col}`;
        const element: HTMLElement | null = DomUtils.getElementById(id);
        if (element == null) {
            const errorString: string = `Expected HTML Element could not be found. id: {id}.`;
            console.error(errorString);
            throw new Error(errorString);
        }
        return element;
    }
    
    static registerCellEventListener(cell: Cell, eventType: string, listener: (event: Event) => void): void{
        console.log (`CellView adding EventListener. cell: ${cell}, eventType: ${eventType}.`);
        const cellView: Element = CellView.#getCellElement(cell);
        cellView.addEventListener(eventType, listener);
        return;
    }

    static focusCell(cell: Cell): void{
        const element: HTMLElement = CellView.#getCellElement(cell);
        DomUtils.focusElement(element);
        return;
    }

    static renderCell(cell: Cell): void{
        const element: HTMLElement = CellView.#getCellElement(cell);
        switch(cell.state){
            case Cell.emptyCellState:
                CellView.#renderEmptyCell(element);
                break;
            case Cell.setCellState:
                CellView.#renderSetCell(element, cell.value);
                break;
            case Cell.candidatesCellState:
                CellView.#renderCandidatesCell(element, cell.candidates);
                break;
        }
        return;
    }

    static #renderEmptyCell(element: HTMLElement): void{
        DomUtils.removeAllElementChildNodes(element);
        DomUtils.setElementClasses(element, [CellView.cellClassName, CellView.emptyCellClassName]);
        return;
    }

    static #renderSetCell(element: HTMLElement, value: Value | null): void{
        const valueString: string = value? value.toString() : "!";
        const valueTextNode: Node = DomUtils.createTextNode(valueString);
        element = DomUtils.removeAllElementChildNodes(element);
        element = DomUtils.addElementChildNode(element, valueTextNode);
        element = DomUtils.setElementClasses(element, [CellView.cellClassName, CellView.setCellClassName]);
        element = DomUtils.setElemenetDatasetPropery(element, CellView.setCellPropertyName, valueString);
        return;
    }

    static #renderCandidatesCell(element: HTMLElement, candidates: Value[]): void{
        element = DomUtils.removeAllElementChildNodes(element);
        const candidateElements: HTMLElement[] = [...Array(9).keys()]
            .map((index: number): number => index + 1)
            .map((candidate: Value): HTMLElement => {
                const candidateString: string = candidate.toString();
                const candidateTextNode: Node = DomUtils.createTextNode(candidateString);
                let candidateElement: HTMLElement = DomUtils.createElement('div', [CellView.candidateValueClassName]);
                candidateElement = DomUtils.setElemenetDatasetPropery(candidateElement, CellView.candidateCellPropertyName, candidateString);
                if (candidates.includes(candidate)){
                    candidateElement = DomUtils.addElementChildNode(candidateElement, candidateTextNode);
                }
                return candidateElement;
            });

        element = DomUtils.addElementChildNodes(element, candidateElements);
        element = DomUtils.setElementClasses(element, [CellView.cellClassName, CellView.candidatesCellClassName]);
        return;
    }
}