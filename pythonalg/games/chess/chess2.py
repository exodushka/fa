from abc import ABC, abstractmethod
from enum import Enum
from dataclasses import dataclass
from typing import List, Optional, Tuple


class Color(Enum):
    WHITE = "white"
    BLACK = "black"

@dataclass(frozen=True)
class Position:
    row: int
    col: int

    def is_valid(self) -> bool:
        return 0 <= self.row < 8 and 0 <= self.col < 8

    def __str__(self):
        # шахматная нотация
        return f"{chr(self.col + 97)}{self.row + 1}"


class Piece(ABC):
    def __init__(self, color: Color):
        self.color = color
        self.has_moved = False  # для рокировки и пешек

    @abstractmethod
    def get_symbol(self) -> str:
        pass

    @abstractmethod
    def get_valid_moves(self, current_pos: Position, board: 'Board') -> List[Position]:
        pass

    def __str__(self):
        return self.get_symbol()

class Pawn(Piece):
    def get_symbol(self) -> str:
        return '♟' if self.color == Color.BLACK else '♙'

    def get_valid_moves(self, current_pos: Position, board: 'Board') -> List[Position]:
        moves = []
        direction = 1 if self.color == Color.WHITE else -1
        start_row = 1 if self.color == Color.WHITE else 6

        next_pos = Position(current_pos.row + direction, current_pos.col)
        if next_pos.is_valid() and board.is_empty(next_pos):
            moves.append(next_pos)
            if not self.has_moved and current_pos.row == start_row:
                double_pos = Position(current_pos.row + 2 * direction, current_pos.col)
                if board.is_empty(double_pos):
                    moves.append(double_pos)
        
        for d_col in [-1, 1]:
            capture_pos = Position(current_pos.row + direction, current_pos.col + d_col)
            if capture_pos.is_valid():
                target = board.get_piece(capture_pos)
                if target and target.color != self.color:
                    moves.append(capture_pos)
        return moves

class Rook(Piece):
    def get_symbol(self) -> str:
        return '♜' if self.color == Color.BLACK else '♖'

    def get_valid_moves(self, current_pos: Position, board: 'Board') -> List[Position]:
        return self._get_sliding_moves(current_pos, board, [(0, 1), (0, -1), (1, 0), (-1, 0)])

    def _get_sliding_moves(self, pos: Position, board: 'Board', directions: List[Tuple[int, int]]) -> List[Position]:
        moves = []
        for d_row, d_col in directions:
            for i in range(1, 8):
                new_pos = Position(pos.row + i * d_row, pos.col + i * d_col)
                if not new_pos.is_valid():
                    break
                target = board.get_piece(new_pos)
                if target is None:
                    moves.append(new_pos)
                else:
                    if target.color != self.color:
                        moves.append(new_pos)
                    break
        return moves

class Knight(Piece):
    def get_symbol(self) -> str:
        return '♞' if self.color == Color.BLACK else '♘'

    def get_valid_moves(self, current_pos: Position, board: 'Board') -> List[Position]:
        moves = []
        offsets = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        for d_row, d_col in offsets:
            new_pos = Position(current_pos.row + d_row, current_pos.col + d_col)
            if new_pos.is_valid():
                target = board.get_piece(new_pos)
                if target is None or target.color != self.color:
                    moves.append(new_pos)
        return moves

class Bishop(Piece):
    def get_symbol(self) -> str:
        return '♝' if self.color == Color.BLACK else '♗'

    def get_valid_moves(self, current_pos: Position, board: 'Board') -> List[Position]:
        return self._get_sliding_moves(current_pos, board, [(1, 1), (1, -1), (-1, 1), (-1, -1)])
    
    def _get_sliding_moves(self, pos: Position, board: 'Board', directions: List[Tuple[int, int]]) -> List[Position]:
        moves = []
        for d_row, d_col in directions:
            for i in range(1, 8):
                new_pos = Position(pos.row + i * d_row, pos.col + i * d_col)
                if not new_pos.is_valid(): break
                target = board.get_piece(new_pos)
                if target is None: moves.append(new_pos)
                else:
                    if target.color != self.color: moves.append(new_pos)
                    break
        return moves

class Queen(Piece):
    def get_symbol(self) -> str:
        return '♛' if self.color == Color.BLACK else '♕'

    def get_valid_moves(self, current_pos: Position, board: 'Board') -> List[Position]:
        rook = Rook(self.color)
        bishop = Bishop(self.color)
        moves = rook.get_valid_moves(current_pos, board)
        moves += bishop.get_valid_moves(current_pos, board)
        return moves

class King(Piece):
    def get_symbol(self) -> str:
        return '♚' if self.color == Color.BLACK else '♔'

    def get_valid_moves(self, current_pos: Position, board: 'Board') -> List[Position]:
        moves = []
        for d_row in [-1, 0, 1]:
            for d_col in [-1, 0, 1]:
                if d_row == 0 and d_col == 0: continue
                new_pos = Position(current_pos.row + d_row, current_pos.col + d_col)
                if new_pos.is_valid():
                    target = board.get_piece(new_pos)
                    if target is None or target.color != self.color:
                        moves.append(new_pos)
        return moves


class Square:
    def __init__(self, row: int, col: int):
        self.position = Position(row, col)
        self.piece: Optional[Piece] = None

    def is_empty(self) -> bool:
        return self.piece is None

    def place_piece(self, piece: Piece):
        self.piece = piece

    def remove_piece(self) -> Optional[Piece]:
        p = self.piece
        self.piece = None
        return p

    def __str__(self):
        if self.piece:
            return self.piece.get_symbol()
        return '·'

class Board:
    def __init__(self):
        self.squares: List[List[Square]] = [[Square(r, c) for c in range(8)] for r in range(8)]
        self._setup_initial_position()

    def _setup_initial_position(self):
        #white
        for c in range(8):
            self.squares[1][c].place_piece(Pawn(Color.WHITE))
        
        order = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for c, piece_class in enumerate(order):
            self.squares[0][c].place_piece(piece_class(Color.WHITE))
        
        #black 
        for c in range(8):
            self.squares[6][c].place_piece(Pawn(Color.BLACK))
        
        for c, piece_class in enumerate(order):
            self.squares[7][c].place_piece(piece_class(Color.BLACK))

    def get_square(self, pos: Position) -> Optional[Square]:
        if pos.is_valid():
            return self.squares[pos.row][pos.col]
        return None

    def get_piece(self, pos: Position) -> Optional[Piece]:
        square = self.get_square(pos)
        return square.piece if square else None

    def is_empty(self, pos: Position) -> bool:
        square = self.get_square(pos)
        return square.is_empty() if square else True

    def move_piece(self, from_pos: Position, to_pos: Position) -> bool:
        piece = self.get_piece(from_pos)
        if not piece:
            return False
        
        if to_pos not in piece.get_valid_moves(from_pos, self):
            return False

        self.get_square(to_pos).place_piece(piece)
        self.get_square(from_pos).remove_piece()
        piece.has_moved = True
        return True

    def __str__(self):
        board_str = "  a b c d e f g h\n"
        for r in range(7, -1, -1):
            board_str += f"{r + 1} "
            for c in range(8):
                board_str += f"{self.squares[r][c]} "
            board_str += f"{r + 1}\n"
        board_str += "  a b c d e f g h"
        return board_str


class Player:
    def __init__(self, color: Color, name: str):
        self.color = color
        self.name = name

class ChessGame:
    def __init__(self):
        self.board = Board()
        self.players = [
            Player(Color.WHITE, "Белые"),
            Player(Color.BLACK, "Черные")
        ]
        self.current_turn_index = 0
        self.is_game_over = False

    @property
    def current_player(self) -> Player:
        return self.players[self.current_turn_index]

    def switch_turn(self):
        self.current_turn_index = (self.current_turn_index + 1) % 2

    def parse_input(self, input_str: str) -> Optional[Tuple[Position, Position]]:
        try:
            parts = input_str.split()
            if len(parts) != 2: return None
            c1, r1 = parts[0][0], int(parts[0][1])
            c2, r2 = parts[1][0], int(parts[1][1])
            from_pos = Position(r1 - 1, ord(c1) - 97)
            to_pos = Position(r2 - 1, ord(c2) - 97)
            if from_pos.is_valid() and to_pos.is_valid():
                return from_pos, to_pos
        except:
            pass
        return None

    def start(self):
        print("=== Шахматы (OOP Версия) ===")
        print("Ввод хода: e2 e4 (откуда куда)")
        print(self.board)

        while not self.is_game_over:
            player = self.current_player
            print(f"\nХод: {player.name}")
            
            move = input("Ваш ход: ")
            parsed = self.parse_input(move)
            
            if not parsed:
                print("Неверный формат. Пример: e2 e4")
                continue

            from_pos, to_pos = parsed
            piece = self.board.get_piece(from_pos)

            if not piece:
                print("Здесь нет фигуры.")
                continue
            
            if piece.color != player.color:
                print("Это не ваша фигура.")
                continue

            if self.board.move_piece(from_pos, to_pos):
                print(self.board)
                self.switch_turn()
            else:
                print("Недопустимый ход для этой фигуры.")

if __name__ == "__main__":
    game = ChessGame()
    game.start()