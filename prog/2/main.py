import customtkinter as ctk
from tkinter import messagebox, simpledialog
import random

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

CLUBS = [
    "Реал Мадрид", "Барселона", "Бавария", "Манчестер Юнайтед",
    "Ливерпуль", "Ювентус", "ПСЖ", "Челси", "Арсенал", "Милан", "Интер", "Атлетико"
]
PLAYER_DATABASE = {
    ("Реал Мадрид", "Барселона"): ["Луиш Фигу", "Роналдо", "Микаэль Лаудруп", "Хавьер Савиола", "Рональд Куман"],
    ("Реал Мадрид", "Бавария"): ["Тони Кроос", "Хамес Родригес", "Арьен Роббен"],
    ("Реал Мадрид", "Манчестер Юнайтед"): ["Криштиану Роналду", "Дэвид Бекхэм", "Хуан Мата"],
    ("Реал Мадрид", "Ливерпуль"): ["Хаби Алонсо", "Майкл Оуэн", "Стив Макманаман"],
    ("Реал Мадрид", "Ювентус"): ["Зинедин Зидан", "Гонсало Игуаин", "Альваро Мората", "Фабио Каннаваро"],
    ("Реал Мадрид", "ПСЖ"): ["Килиан Мбаппе", "Анхель Ди Мария", "Николя Анелька"],
    ("Реал Мадрид", "Челси"): ["Тибо Куртуа", "Эден Азар", "Клод Макелеле"],
    ("Реал Мадрид", "Арсенал"): ["Месут Озил", "Дани Себальос", "Николя Анелька"],
    ("Реал Мадрид", "Милан"): ["Кака", "Андрей Шевченко", "Роналдо", "Кларенс Зеедорф"],
    ("Реал Мадрид", "Интер"): ["Уэсли Снейдер", "Роналдо", "Самюэль Это'О"],
    ("Реал Мадрид", "Атлетико"): ["Тибо Куртуа", "Альваро Мората", "Фернандо Торрес"],

    ("Барселона", "Бавария"): ["Роберт Левандовски", "Тьяго Алькантара", "Хавьер Маскерано"],
    ("Барселона", "Манчестер Юнайтед"): ["Златан Ибрагимович", "Хуан Верон", "Жерар Пике"],
    ("Барселона", "Ливерпуль"): ["Луис Суарес", "Фелипе Коутиньо", "Хавьер Маскерано"],
    ("Барселона", "Ювентус"): ["Артур Мело", "Миралем Пьянич", "Тьяго Мотта"],
    ("Барселона", "ПСЖ"): ["Неймар", "Лионель Месси", "Роналдиньо", "Тьяго Мотта"],
    ("Барселона", "Челси"): ["Сеск Фабрегас", "Педро Родригес", "Хуан Верон"],
    ("Барселона", "Арсенал"): ["Алексис Санчес", "Тьерри Анри", "Сеск Фабрегас"],
    ("Барселона", "Милан"): ["Роналдиньо", "Златан Ибрагимович", "Патрик Клюйверт"],
    ("Барселона", "Интер"): ["Роналдо", "Хавьер Дзанетти", "Луиш Фигу"],
    ("Барселона", "Атлетико"): ["Давид Вилья", "Луис Суарес", "Тьяго Алькантара"],

    ("Бавария", "Манчестер Юнайтед"): ["Бастиан Швайнштайгер", "Хуан Мата", "Гордон Стракан"],
    ("Бавария", "Ливерпуль"): ["Тьяго Алькантара", "Дитмар Хаманн", "Штефан Эффенберг"],
    ("Бавария", "Ювентус"): ["Маттейс де Лигт", "Артуро Видаль", "Дуглас Коста"],
    ("Бавария", "ПСЖ"): ["Кингсли Коман", "Эрик Максим Чупо-Мотинг", "Бернд Лено"],
    ("Бавария", "Челси"): ["Михаэль Баллак", "Дидье Дрогба", "Жоржиньо"],
    ("Бавария", "Арсенал"): ["Сердж Гнабри", "Лукас Подольски", "Месут Озил"],
    ("Бавария", "Милан"): ["Андреа Пирло", "Кларенс Зеедорф", "Лука Тони"],
    ("Бавария", "Интер"): ["Луиш Фигу", "Кларенс Зеедорф", "Лотар Маттеус"],
    ("Бавария", "Атлетико"): ["Хуанфран", "Диего Симеоне", "Луис Гарсия"],

    ("Манчестер Юнайтед", "Ливерпуль"): ["Майкл Оуэн", "Стив Макманаман", "Питер Крауч"],
    ("Манчестер Юнайтед", "Ювентус"): ["Криштиану Роналду", "Златан Ибрагимович", "Анхель Ди Мария"],
    ("Манчестер Юнайтед", "ПСЖ"): ["Анхель Ди Мария", "Златан Ибрагимович", "Маркус Рэшфорд"],
    ("Манчестер Юнайтед", "Челси"): ["Хуан Мата", "Неманья Видич", "Дидье Дрогба"],
    ("Манчестер Юнайтед", "Арсенал"): ["Робин ван Перси", "Дэнни Уэлбек", "Сол Кэмпбелл"],
    ("Манчестер Юнайтед", "Милан"): ["Златан Ибрагимович", "Дэвид Бекхэм", "Кларенс Зеедорф"],
    ("Манчестер Юнайтед", "Интер"): ["Златан Ибрагимович", "Ромелу Лукаку", "Алексис Санчес"],
    ("Манчестер Юнайтед", "Атлетико"): ["Хуан Мата", "Диего Форлан", "Радмель Фалькао"],

    ("Ливерпуль", "Ювентус"): ["Фабио Каннаваро", "Джанлука Дзамбротта", "Николя Анелька"],
    ("Ливерпуль", "ПСЖ"): ["Николя Анелька", "Джибриль Сиссе", "Маму Сако"],
    ("Ливерпуль", "Челси"): ["Фернандо Торрес", "Дидье Дрогба", "Стив Макманаман"],
    ("Ливерпуль", "Арсенал"): ["Майкл Оуэн", "Николя Анелька", "Джермейн Пеннант"],
    ("Ливерпуль", "Милан"): ["Андрей Шевченко", "Дидье Дрогба", "Кларенс Зеедорф"],
    ("Ливерпуль", "Интер"): ["Иван Перишич", "Ромелу Лукаку", "Луис Суарес"],
    ("Ливерпуль", "Атлетико"): ["Фернандо Торрес", "Луис Гарсия", "Диего Симеоне"],

    ("Ювентус", "ПСЖ"): ["Анхель Ди Мария", "Гонсало Игуаин", "Мойзе Кин"],
    ("Ювентус", "Челси"): ["Альваро Мората", "Гонсало Игуаин", "Клаудио Маркизио"],
    ("Ювентус", "Арсенал"): ["Аарон Рэмси", "Месут Озил", "Николя Анелька"],
    ("Ювентус", "Милан"): ["Андреа Пирло", "Кларенс Зеедорф", "Джанлуиджи Буффон"],
    ("Ювентус", "Интер"): ["Роналдо", "Андреа Пирло", "Кларенс Зеедорф", "Зинедин Зидан"],
    ("Ювентус", "Атлетико"): ["Альваро Мората", "Фернандо Льоренте", "Диего Симеоне"],

    ("ПСЖ", "Челси"): ["Тьяго Силва", "Давид Луиз", "Николя Анелька"],
    ("ПСЖ", "Арсенал"): ["Николя Анелька", "Тьерри Анри", "Александр Ляказетт"],
    ("ПСЖ", "Милан"): ["Златан Ибрагимович", "Роналдиньо", "Дэвид Бекхэм"],
    ("ПСЖ", "Интер"): ["Златан Ибрагимович", "Роналдо", "Майкон"],
    ("ПСЖ", "Атлетико"): ["Анхель Ди Мария", "Диего Симеоне", "Луис Гарсия"],

    ("Челси", "Арсенал"): ["Сеск Фабрегас", "Оливье Жиру", "Николя Анелька", "Эшли Коул"],
    ("Челси", "Милан"): ["Андрей Шевченко", "Дидье Дрогба", "Кларенс Зеедорф"],
    ("Челси", "Интер"): ["Ромелу Лукаку", "Андреа Пирло", "Кларенс Зеедорф"],
    ("Челси", "Атлетико"): ["Диего Коста", "Фернандо Торрес", "Тибо Куртуа"],

    ("Арсенал", "Милан"): ["Андрей Шевченко", "Тьерри Анри", "Патрик Виейра"],
    ("Арсенал", "Интер"): ["Деннис Бергкамп", "Патрик Виейра", "Кларенс Зеедорф"],
    ("Арсенал", "Атлетико"): ["Тьерри Анри", "Хосе Антонио Рейес", "Месут Озил"],

    ("Милан", "Интер"): ["Роналдо", "Андреа Пирло", "Кларенс Зеедорф", "Златан Ибрагимович", "Лука Модрич"],
    ("Милан", "Атлетико"): ["Фернандо Торрес", "Диего Симеоне", "Луис Гарсия"],

    ("Интер", "Атлетико"): ["Диего Симеоне", "Хавьер Дзанетти", "Луис Гарсия"]
}

class FootballTicTacToe(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Футбольные крестики-нолики")
        self.geometry("800x900")

        self.row_clubs = []
        self.col_clubs = []
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.cell_buttons = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = 1

        self.setup_ui()
        self.setup_new_game()

    def setup_ui(self):
        self.title_label = ctk.CTkLabel(self, text="Футбольные крестики-нолики",
                                        font=ctk.CTkFont(size=28, weight="bold"))
        self.title_label.pack(pady=(20, 10))

        self.turn_label = ctk.CTkLabel(self, text="Ход: Игрок 1",
                                       font=ctk.CTkFont(size=22, weight="bold"),
                                       text_color="red")
        self.turn_label.pack(pady=5)

        self.status_label = ctk.CTkLabel(self, text="Выберите клетку на поле",
                                         font=ctk.CTkFont(size=16), text_color="gray")
        self.status_label.pack(pady=10)

        self.board_frame = ctk.CTkFrame(self, fg_color="gray25", corner_radius=15)
        self.board_frame.pack(pady=20)

        self.restart_btn = ctk.CTkButton(self, text="Новая игра",
                                         command=self.setup_new_game,
                                         font=ctk.CTkFont(size=18, weight="bold"),
                                         width=200, height=40,
                                         fg_color="green", hover_color="darkgreen")
        self.restart_btn.pack(pady=20)

    def setup_new_game(self):
        selected = random.sample(CLUBS, 6)
        self.row_clubs = selected[:3]
        self.col_clubs = selected[3:]

        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = 1
        self.update_turn_indicator()
        self.status_label.configure(text="Выберите клетку на поле")

        for widget in self.board_frame.winfo_children():
            widget.destroy()

        corner = ctk.CTkLabel(self.board_frame, text="", width=120, height=60)
        corner.grid(row=0, column=0, padx=10, pady=10)

        for c in range(3):
            label = ctk.CTkLabel(self.board_frame, text=self.col_clubs[c],
                                 font=ctk.CTkFont(size=14, weight="bold"),
                                 width=120, height=60,
                                 fg_color="gray40", corner_radius=10,
                                 text_color="white")
            label.grid(row=0, column=c + 1, padx=10, pady=10)

        for r in range(3):
            label = ctk.CTkLabel(self.board_frame, text=self.row_clubs[r],
                                 font=ctk.CTkFont(size=14, weight="bold"),
                                 width=120, height=60,
                                 fg_color="gray40", corner_radius=10,
                                 text_color="white")
            label.grid(row=r + 1, column=0, padx=10, pady=10)

            for c in range(3):
                btn = ctk.CTkButton(
                    self.board_frame,
                    text="",
                    width=120,
                    height=120,
                    font=ctk.CTkFont(size=40, weight="bold"),
                    fg_color="gray50", hover_color="gray60",
                    corner_radius=10,
                    border_width=0,
                    command=lambda r=r, c=c: self.on_cell_click(r, c)
                )
                btn.grid(row=r + 1, column=c + 1, padx=10, pady=10)
                self.cell_buttons[r][c] = btn

    def on_cell_click(self, r, c):
        if self.board[r][c] is not None:
            messagebox.showinfo("Ошибка", "Эта клетка уже занята!")
            return

        row_club = self.row_clubs[r]
        col_club = self.col_clubs[c]

        self.status_label.configure(text=f"Клетка: {row_club}  {col_club}")

        player_name = simpledialog.askstring(
            "Назовите футболиста",
            f"Игрок {self.current_player}, назовите футболиста,\n"
            f"который играл за «{row_club}» и «{col_club}»:",
            parent=self
        )

        if not player_name or not player_name.strip():
            messagebox.showwarning("Пропуск хода", "Вы не назвали футболиста. Ход переходит сопернику.")
            self.switch_turn()
            return

        player_name = player_name.strip()

        if self.validate_player(r, c, player_name):
            self.board[r][c] = self.current_player
            self.update_cell(r, c)
            self.status_label.configure(text=f"Верно! {player_name} играл за оба клуба.")

            if self.check_win():
                self.highlight_winning_line()
                messagebox.showinfo("Победа!", f"Игрок {self.current_player} победил!")
                self.disable_board()
            elif self.check_draw():
                messagebox.showinfo("Ничья", "Все клетки заполнены. Ничья!")
                self.disable_board()
            else:
                self.switch_turn()
        else:
            correct_answers = self.get_correct_answers(r, c)
            answers_text = ", ".join(correct_answers[:3]) if correct_answers else "Нет данных"

            messagebox.showerror(
                "Неверный ответ",
                f"Футболист «{player_name}» не играл за оба клуба!\n\n"
                f"Правильные варианты:\n{answers_text}\n\n"
                f"Ход переходит к Игроку {3 - self.current_player}."
            )
            self.switch_turn()

    def normalize(self, text):
        return text.lower().replace('ё', 'е').strip()

    def validate_player(self, r, c, player_name):

        row_club = self.row_clubs[r]
        col_club = self.col_clubs[c]

        key1 = (row_club, col_club)
        key2 = (col_club, row_club)

        players = PLAYER_DATABASE.get(key1) or PLAYER_DATABASE.get(key2)
        if not players:
            return False

        input_words = set(self.normalize(player_name).split())

        for correct_player in players:
            player_words = set(self.normalize(correct_player).split())
            if input_words & player_words:
                return True

        return False

    def get_correct_answers(self, r, c):
        row_club = self.row_clubs[r]
        col_club = self.col_clubs[c]

        key1 = (row_club, col_club)
        key2 = (col_club, row_club)

        if key1 in PLAYER_DATABASE:
            return PLAYER_DATABASE[key1]
        elif key2 in PLAYER_DATABASE:
            return PLAYER_DATABASE[key2]
        return []

    def update_cell(self, r, c):
        for row in self.cell_buttons:
            for btn in row:
                if btn.cget("state") == "normal":
                    btn.configure(border_width=0)

        btn = self.cell_buttons[r][c]
        if self.board[r][c] == 1:
            btn.configure(fg_color="red", hover_color="darkred",
                          text="X", text_color="white",
                          border_width=3, border_color="yellow")
        elif self.board[r][c] == 2:
            btn.configure(fg_color="blue", hover_color="darkblue",
                          text="O", text_color="white",
                          border_width=3, border_color="yellow")
        btn.configure(state="disabled")

    def highlight_winning_line(self):
        b = self.board
        winning_cells = []

        for i in range(3):
            if b[i][0] == b[i][1] == b[i][2] and b[i][0] is not None:
                winning_cells = [(i, 0), (i, 1), (i, 2)]
                break
            if b[0][i] == b[1][i] == b[2][i] and b[0][i] is not None:
                winning_cells = [(0, i), (1, i), (2, i)]
                break

        if not winning_cells:
            if b[0][0] == b[1][1] == b[2][2] and b[0][0] is not None:
                winning_cells = [(0, 0), (1, 1), (2, 2)]
            elif b[0][2] == b[1][1] == b[2][0] and b[0][2] is not None:
                winning_cells = [(0, 2), (1, 1), (2, 0)]

        for r, c in winning_cells:
            btn = self.cell_buttons[r][c]
            btn.configure(fg_color="green", border_width=3, border_color="white")

    def switch_turn(self):
        self.current_player = 3 - self.current_player
        self.update_turn_indicator()
        self.status_label.configure(text="Выберите клетку на поле")

    def update_turn_indicator(self):
        color = "red" if self.current_player == 1 else "blue"
        self.turn_label.configure(text=f"Ход: Игрок {self.current_player}", text_color=color)

    def check_win(self):
        b = self.board
        for i in range(3):
            if b[i][0] == b[i][1] == b[i][2] and b[i][0] is not None: return True
            if b[0][i] == b[1][i] == b[2][i] and b[0][i] is not None: return True
        if b[0][0] == b[1][1] == b[2][2] and b[0][0] is not None: return True
        if b[0][2] == b[1][1] == b[2][0] and b[0][2] is not None: return True
        return False

    def check_draw(self):
        for r in range(3):
            for c in range(3):
                if self.board[r][c] is None: return False
        return True

    def disable_board(self):
        for r in range(3):
            for c in range(3):
                self.cell_buttons[r][c].configure(state="disabled")


if __name__ == "__main__":
    app = FootballTicTacToe()
    app.mainloop()