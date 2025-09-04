OPERATIONS_LIST = ["минус", "плюс", "умножить"]

def calc(s):
    s = s.split()
    num1 = 0
    num2 = 0
    flag_num = False
    
    operation_code = -1

    for i in s:
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
    print(num)

    return s

def operation(s):
    match s:
        case "минус":
            return 1
        case "плюс":
            return 2
        case "умножить":
            return 3

def number(word):
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

if __name__ == "__main__":
    calc(input())