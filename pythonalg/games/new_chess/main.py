class Piece:
    """Базовый класс для всех фигур"""
    def __init__(self, color):
        self.color = color  # 'white' или 'black'
        self.symbol = '?'

    def can_move(self, board, x1, y1, x2, y2):
        """Проверяет, может ли фигура пойти из (x1, y1) в (x2, y2)"""
        raise NotImplementedError

    def is_path_clear(self, board, x1, y1, x2, y2):
        """Проверяет, свободен ли путь (для ладьи, слона, ферзя)"""
        dx = x2 - x1
        dy = y2 - y1
        steps = max(abs(dx), abs(dy))
        step_x = 0 if dx == 0 else dx // steps
        step_y = 0 if dy == 0 else dy // steps

        for i in range(1, steps):
            if board.get_piece(x1 + step_x * i, y1 + step_y * i) is not None:
                return False
        return True

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = '♟' if color == 'black' else '♙'

    def can_move(self, board, x1, y1, x2, y2):
        direction = 1 if self.color == 'white' else -1
        start_row = 1 if self.color == 'white' else 6
        
        # Ход вперед на 1
        if x2 == x1 + direction and y2 == y1 and board.get_piece(x2, y2) is None:
            return True
        # Ход вперед на 2 (первый ход)
        if x1 == start_row and x2 == x1 + 2 * direction and y2 == y1:
            if board.get_piece(x2, y2) is None and board.get_piece(x1 + direction, y1) is None:
                return True
        # Взятие по диагонали
        if x2 == x1 + direction and abs(y2 - y1) == 1:
            target = board.get_piece(x2, y2)
            if target and target.color != self.color:
                return True
        return False

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = '♜' if color == 'black' else '♖'

    def can_move(self, board, x1, y1, x2, y2):
        if x1 != x2 and y1 != y2: return False
        return self.is_path_clear(board, x1, y1, x2, y2)

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = '♞' if color == 'black' else '♘'

    def can_move(self, board, x1, y1, x2, y2):
        dx, dy = abs(x1 - x2), abs(y1 - y2)
        return (dx == 1 and dy == 2) or (dx == 2 and dy == 1)

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = '♝' if color == 'black' else '♗'

    def can_move(self, board, x1, y1, x2, y2):
        if abs(x1 - x2) != abs(y1 - y2): return False
        return self.is_path_clear(board, x1, y1, x2, y2)

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = '♛' if color == 'black' else '♕'

    def can_move(self, board, x1, y1, x2, y2):
        # Ферзь = Ладья + Слон
        if x1 == x2 or y1 == y2: # Как ладья
            return self.is_path_clear(board, x1, y1, x2, y2)
        if abs(x1 - x2) == abs(y1 - y2): # Как слон
            return self.is_path_clear(board, x1, y1, x2, y2)
        return False

class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.symbol = '♚' if color == 'black' else '♔'

    def can_move(self, board, x1, y1, x2, y2):
        return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1

class Board:
    def __init__(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]
        self.setup_pieces()

    def setup_pieces(self):
        # Исправлено: белые снизу (ряды 6, 7), чёрные сверху (ряды 0, 1)
        # Порядок фигур: Ладья, Конь, Слон, Ферзь, Король, Слон, Конь, Ладья
        self.grid[7] = [Rook('white'), Knight('white'), Bishop('white'), Queen('white'), 
                        King('white'), Bishop('white'), Knight('white'), Rook('white')]
        self.grid[6] = [Pawn('white') for _ in range(8)]
        
        self.grid[0] = [Rook('black'), Knight('black'), Bishop('black'), Queen('black'), 
                        King('black'), Bishop('black'), Knight('black'), Rook('black')]
        self.grid[1] = [Pawn('black') for _ in range(8)]

    def get_piece(self, x, y):
        if 0 <= x < 8 and 0 <= y < 8:
            return self.grid[x][y]
        return None

    def move_piece(self, x1, y1, x2, y2):
        piece = self.get_piece(x1, y1)
        target = self.get_piece(x2, y2)

        # Проверка: фигура существует, цвет совпадает с ходом, путь свободен (если нужно), 
        # и мы не едим своих
        if piece and (target is None or target.color != piece.color):
            if piece.can_move(self, x1, y1, x2, y2):
                self.grid[x2][y2] = piece
                self.grid[x1][y1] = None
                return True
        return False

    def __str__(self):
        res = "  a b c d e f g h\n"
        for i in range(8):
            row_str = f"{8-i} "
            for j in range(8):
                p = self.grid[i][j]
                row_str += (p.symbol if p else '.') + " "
            res += row_str + f"{8-i}\n"
        res += "  a b c d e f g h\n"
        return res

class Game:
    def __init__(self):
        self.board = Board()
        self.current_turn = 'white'

    def parse_input(self, text):
        # Преобразует ввод типа "e2 e4" в координаты (6, 4, 4, 4)
        try:
            cols = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
            parts = text.split()
            if len(parts) != 2: return None
            
            y1 = cols[parts[0][0]]
            x1 = 8 - int(parts[0][1])
            y2 = cols[parts[1][0]]
            x2 = 8 - int(parts[1][1])
            return x1, y1, x2, y2
        except:
            return None

    def run(self):
        print("Шахматы (Python OOP). Ввод: e2 e4")
        while True:
            print(self.board)
            print(f"Ход: {self.current_turn}")
            move = input("Введите ход (или 'exit'): ")
            
            if move.lower() == 'exit':
                break

            coords = self.parse_input(move)
            if not coords:
                print("Неверный формат. Пример: e2 e4")
                continue

            x1, y1, x2, y2 = coords
            piece = self.board.get_piece(x1, y1)

            if not piece:
                print("Здесь нет фигуры.")
                continue
            if piece.color != self.current_turn:
                print("Сейчас не ваш ход этой фигурой.")
                continue

            if self.board.move_piece(x1, y1, x2, y2):
                # Смена хода
                self.current_turn = 'black' if self.current_turn == 'white' else 'white'
            else:
                print("Недопустимый ход!")

if __name__ == "__main__":
    game = Game()
    game.run()