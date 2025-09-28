OPERATIONS_LIST = ["минус", "плюс", "умножить"]

def calc(s: str):
    s = s.split()
    num1 = 0
    num2 = 0
    flag_num = False
    
    operation_code = -1

    for i in s:
        if i == "на": continue
        if i not in OPERATIONS_LIST:
            match flag_num:
                case False:
                    num1 += number(i)
                case True:
                    num2 += number(i)
        else:
            flag_num = True
            operation_code = operation(i)
    
    num = 0
    match operation_code:
        case 1:
            num = num1 - num2
        case 2:
            num = num1 + num2
        case 3:
            num = num1 * num2

    return to_str(str(num))#, num

def operation(s: str):
    match s:
        case "минус":
            return 1
        case "плюс":
            return 2
        case "умножить":
            return 3

def number(word: str):
    match word:
        case "один": 
            return 1
        case "два":
            return 2
        case "три":
            return 3
        case "четыре":
            return 4
        case "пять":
            return 5
        case "шесть":
            return 6
        case "семь":
            return 7
        case "восемь":
            return 8
        case "девять":
            return 9
        case "десять":
            return 10
        case "одиннадцать":
            return 11            
        case "двенадцать":
            return 12
        case "тринадцать":
            return 13
        case "четырнадцать":
            return 14
        case "пятнадцать":
            return 15
        case "шестнадцать":
            return 16
        case "семнадцать":
            return 17
        case "восемнадцать":
            return 18
        case "девятнадцать":
            return 19
        case "двадцать":
            return 20
        case "тридцать":
            return 30
        case "сорок":
            return 40
        case "пятьдесят":
            return 50
        case "шестьдесят":
            return 60
        case "семьдесят":
            return 70
        case "восемьдесят":
            return 80
        case "девяносто":
            return 90

def to_str(num: str):
    def onenum(s: str):
        match s:
            case "1":
                return "один"
            case "2":
                return "два"
            case "3":
                return "три"
            case "4":
                return 'четыре'
            case "5":
                return "пять"
            case "6":
                return "шесть"
            case "7":
                return "семь"
            case "8":
                return "восемь"
            case "9":
                return "девять"
            case _:
                raise "Ошибка onenum"
    def twonum(s: str):
        match s:
            case "10":
                return "десять"
            case "11":
                return "одиннадцать"
            case "12":
                return "двенадцать"
            case "13":
                return "тринадцать"
            case "14":
                return "четырнадцать"
            case "15":
                return "пятнадцать"
            case "16":
                return "шестнадцать"
            case "17":
                return "семьнадцать"
            case "18":
                return "восемьнадцать"
            case "19":
                return "девятнадцать"
            case "2":
                return "двадцать"
            case "3":
                return "тридцать"
            case "4":
                return "сорок"
            case "5":
                return "пятьдесят"
            case "6":
                return "шестьдесят"
            case "7":
                return "семьдесят"
            case "8":
                return "восемьдесят"
            case "9":
                return "девяносто"
            case _:
                raise "Ошибка twonum"

    if len(num) == 1:
        return onenum(num)
    elif len(num) == 2:
        if int(num) < 20:
            return twonum(num)
        else:
            return twonum(num[0]) + " " + onenum(num[1])
    else:
        raise "Неверная длинна ответа"

if __name__ == "__main__":
    print(calc(input()))