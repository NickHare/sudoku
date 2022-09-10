import "../css/main.css";
import { Row, Col, Value } from "./types";
import { Cell } from "cell";
import { Board } from "board";
import { CellController } from "./cell/cell-controller";
import { BoardController } from "./board/board-controller";

const board: Board = Board.initTestBoard();
const boardController: BoardController = new BoardController(board);
const cellControllerArray: CellController[][] = board.cellArray.map((cellRow: Cell[]): CellController[] => {
    return cellRow.map((cell: Cell): CellController => {
        return new CellController(cell);
    });
});

export { Row, Col, Value, Board, Cell, board, boardController, cellControllerArray};
