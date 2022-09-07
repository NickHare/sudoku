import "../css/main.css";
import { Row, Col, Value } from "./types";
import { Cell } from "cell";
import { Board } from "board";
import { CellController } from "./cell/cell-controller";
import { BoardController } from "./board/board-controller";

const boardController: BoardController = new BoardController();
const cellController: CellController = new CellController(boardController.board);
cellController.renderAllCells();

export { Row, Col, Value, Board, Cell, boardController, cellController};
