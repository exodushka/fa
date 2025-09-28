import main


def first():
    q = [
        main.calc("два плюс один") == "три",
        main.calc("два плюс десять") == "двенадцать",
        
        main.calc("два минус один") == "один",
        main.calc("двадцать минус пять") == "пятнадцать",
        main.calc('пятнадцать минус семь') == "восемь",
        
        main.calc("один умножить на три") == "три",
        main.calc("пять умножить на пять") == "двадцать пять"
    ]
    print(q)
    return all(q)

if __name__ == "__main__":
    a = input()
    match a:
        case "1":
            print(first())
        
        case all:
            ...
