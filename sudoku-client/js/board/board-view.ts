import { DomUtils } from "utils";

export class BoardView{
    static #getBoardElement(): HTMLElement{
        const id: string = `board`;
        const element: HTMLElement | null = DomUtils.getElementById(id);
        if (element == null) {
            const errorString: string = `Expected HTML Element could not be found. id: {id}.`;
            console.error(errorString);
            throw new Error(errorString);
        }
        return element;
    }

    static registerBoardEventListener(eventType: string, listener: (event: Event) => void): void{
        console.log (`BoardView adding EventListener. eventType: ${eventType}.`);
        const boardView: Element = BoardView.#getBoardElement();
        boardView.addEventListener(eventType, listener);
        return;
    }
}