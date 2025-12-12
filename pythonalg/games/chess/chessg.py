import sys
import re
import os

UNICODE_PIECES = {
    'r': '♜', 'n': '♞', 'b': '♝', 'q': '♛', 'k': '♚', 'p': '♟',
    'R': '♖', 'N': '♘', 'B': '♗', 'Q': '♕', 'K': '♔', 'P': '♙',
    '.': '·'
}

class ChessGame:
    def __init__(self):
        self.reset_board()

    def reset_board(self):
        self.board = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]
        self.white_turn = True
        self.move_history = [] # Список для сохранения истории (PGN)

    def print_board(self):
        print("\n  a b c d e f g h")
        print(" +-----------------+")
        for i, row in enumerate(self.board):
            line = f"{8 - i}| " + " ".join(UNICODE_PIECES.get(p, p) for p in row) + f" |{8 - i}"
            print(line)
        print(" +-----------------+")
        print("  a b c d e f g h\n")

    # --- ЛОГИКА АНАЛИЗА ХОДА (КАК В ПРОШЛЫЙ РАЗ) ---

    def parse_san_move(self, move_str):
        """Преобразует строку (e4, Nf3) в координаты."""
        move_str = move_str.replace('+', '').replace('#', '').strip()

        # Рокировки
        if move_str == "O-O":
            row = 7 if self.white_turn else 0
            return (row, 4), (row, 6), 'castling_short'
        if move_str == "O-O-O":
            row = 7 if self.white_turn else 0
            return (row, 4), (row, 2), 'castling_long'

        # Обычные ходы
        match = re.match(r'^([NBRQK])?([a-h1-8])?(x)?([a-h][1-8])(=[NBRQ])?$', move_str)
        if not match:
            # Попытка для пешки (e4)
            match = re.match(r'^()([a-h])?(x)?([a-h][1-8])(=[NBRQ])?$', move_str)
        
        if not match:
            raise ValueError("Некорректный формат хода.")

        piece_char, disambig, is_capture, target_sq, promotion = match.groups()
        
        piece_type = piece_char if piece_char else 'P'
        if not self.white_turn: piece_type = piece_type.lower()

        target_c = ord(target_sq[0]) - ord('a')
        target_r = 8 - int(target_sq[1])
        target_pos = (target_r, target_c)

        start_pos = self.find_piece_source(piece_type, target_pos, disambig, is_capture)
        return start_pos, target_pos, promotion

    def find_piece_source(self, piece, target, disambig, is_capture):
        candidates = []
        for r in range(8):
            for c in range(8):
                if self.board[r][c] == piece:
                    if self.can_move((r, c), target, is_capture):
                        candidates.append((r, c))

        # Уточнение (если есть неоднозначность, например Nbd7)
        if disambig:
            if disambig.isdigit():
                row_idx = 8 - int(disambig)
                candidates = [cand for cand in candidates if cand[0] == row_idx]
            else:
                col_idx = ord(disambig) - ord('a')
                candidates = [cand for cand in candidates if cand[1] == col_idx]

        if len(candidates) == 1:
            return candidates[0]
        elif len(candidates) == 0:
            raise ValueError(f"Нет фигур {piece}, которые могут пойти на это поле.")
        else:
            raise ValueError("Неоднозначный ход. Уточните фигуру (например, Nge2).")

    def can_move(self, start, end, is_capture_intention):
        """Базовая проверка геометрии хода."""
        r1, c1 = start
        r2, c2 = end
        piece = self.board[r1][c1].upper()
        dr, dc = r2 - r1, c2 - c1
        
        dest_piece = self.board[r2][c2]
        is_dest_empty = dest_piece == '.'
        
        # Нельзя есть своих
        if not is_dest_empty:
            if (dest_piece.isupper() == self.board[r1][c1].isupper()):
                return False

        if piece == 'N': return (abs(dr), abs(dc)) in [(1, 2), (2, 1)]
        if piece == 'K': return max(abs(dr), abs(dc)) == 1
        if piece == 'R': 
            if dr != 0 and dc != 0: return False
            return self.is_path_clear(start, end)
        if piece == 'B': 
            if abs(dr) != abs(dc): return False
            return self.is_path_clear(start, end)
        if piece == 'Q': 
            if not (dr == 0 or dc == 0 or abs(dr) == abs(dc)): return False
            return self.is_path_clear(start, end)
        
        if piece == 'P':
            direction = -1 if self.board[r1][c1].isupper() else 1
            # Ход вперед
            if dc == 0 and is_dest_empty:
                if dr == direction: return True
                start_row = 6 if direction == -1 else 1
                if r1 == start_row and dr == 2 * direction and self.board[r1 + direction][c1] == '.':
                    return True
            # Взятие
            if abs(dc) == 1 and dr == direction:
                if not is_dest_empty: return True
                if is_capture_intention: return True # En Passant (упрощенно)
            return False

        return False

    def is_path_clear(self, start, end):
        r1, c1 = start
        r2, c2 = end
        dr, dc = r2 - r1, c2 - c1
        step_r = 0 if dr == 0 else (1 if dr > 0 else -1)
        step_c = 0 if dc == 0 else (1 if dc > 0 else -1)
        cur_r, cur_c = r1 + step_r, c1 + step_c
        while (cur_r, cur_c) != (r2, c2):
            if self.board[cur_r][cur_c] != '.': return False
            cur_r += step_r
            cur_c += step_c
        return True

    def apply_move(self, move_str, record=True):
        """Выполняет ход на доске."""
        try:
            start, end, special = self.parse_san_move(move_str)
            
            # Обработка рокировок
            if special == 'castling_short':
                self.board[start[0]][6] = self.board[start[0]][4]
                self.board[start[0]][4] = '.'
                self.board[start[0]][5] = self.board[start[0]][7]
                self.board[start[0]][7] = '.'
            elif special == 'castling_long':
                self.board[start[0]][2] = self.board[start[0]][4]
                self.board[start[0]][4] = '.'
                self.board[start[0]][3] = self.board[start[0]][0]
                self.board[start[0]][0] = '.'
            else:
                piece = self.board[start[0]][start[1]]
                if special: piece = special[1].upper() if self.white_turn else special[1].lower() # Превращение
                
                # En Passant удаление
                if piece.upper() == 'P' and start[1] != end[1] and self.board[end[0]][end[1]] == '.':
                    self.board[start[0]][end[1]] = '.'

                self.board[end[0]][end[1]] = piece
                self.board[start[0]][start[1]] = '.'

            if record:
                self.move_history.append(move_str)
            
            self.white_turn = not self.white_turn
            return True
        except ValueError as e:
            print(f"Ошибка хода: {e}")
            return False

    # --- ФУНКЦИИ ЗАГРУЗКИ И СОХРАНЕНИЯ ---

    def save_to_pgn(self, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write('[Event "Console Game"]\n\n')
            full_str = ""
            for i, move in enumerate(self.move_history):
                if i % 2 == 0:
                    full_str += f"{i//2 + 1}. {move} "
                else:
                    full_str += f"{move} "
            f.write(full_str.strip())
        print(f"Игра сохранена в файл {filename}")

    def load_from_pgn(self, filename):
        if not os.path.exists(filename):
            print("Файл не найден.")
            return

        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Чистка PGN
        content = re.sub(r'\[.*?\]', '', content)
        content = re.sub(r'\{.*?\}', '', content)
        content = re.sub(r'\d+\.', '', content)
        moves = content.split()
        if moves and moves[-1] in ['1-0', '0-1', '1/2-1/2', '*']: moves.pop()

        self.reset_board()
        print(f"Загрузка {len(moves)} ходов...")
        for move in moves:
            if not self.apply_move(move, record=True):
                print(f"Ошибка при загрузке хода {move}. Загрузка остановлена.")
                break
        print("Загрузка завершена.")

    # --- ИГРОВОЙ ЦИКЛ ---

    def play(self):
        print("--- КОНСОЛЬНЫЕ ШАХМАТЫ ---")
        print("Формат ходов: e4, Nf3, O-O, cxd5")
        print("Команды:")
        print("  save <имя> - сохранить игру (например: save mygame.pgn)")
        print("  load <имя> - загрузить игру (например: load kasparov.pgn)")
        print("  exit       - выход")
        print("-" * 30)

        while True:
            self.print_board()
            turn = "Белые" if self.white_turn else "Черные"
            user_input = input(f"Ход {turn} > ").strip()

            if not user_input: continue

            # Обработка команд
            if user_input.lower() in ['exit', 'quit']:
                print("Игра завершена.")
                break
            
            if user_input.lower().startswith("save "):
                fname = user_input.split(" ", 1)[1]
                self.save_to_pgn(fname)
                continue
            
            if user_input.lower().startswith("load "):
                fname = user_input.split(" ", 1)[1]
                self.load_from_pgn(fname)
                continue

            # Попытка сделать ход
            if self.apply_move(user_input):
                print(f"Сделан ход: {user_input}")
            # Если ошибка, она выведется внутри apply_move, цикл продолжится

if __name__ == "__main__":
    game = ChessGame()
    game.play()