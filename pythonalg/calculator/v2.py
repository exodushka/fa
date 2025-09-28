NOT_NUMS = ["bbb", "ccc", "минус", "плюс"]
def calc(s):
    def pars_num(s):
        if s == "один": return 1
        if s == "два": return 2
        if s == "три": return 3
        if s == "четыре": return 4
        if s == "пять": return 5
        if s == "шесть": return 6
        if s == "семь": return 7
        if s == "восемь": return 8
        if s == "девять": return 9
        if s == "десять": return 10
        if s == 'одиннадцать': return 11
        if s == 'двенадцать': return 12
        if s == 'тринадцать': return 13
        if s == 'четырнадцать': return 14
        if s == 'пятнадцать': return 15
        if s == 'шестнадцать': return 16
        if s == 'семнадцать': return 17
        if s == 'восемнадцать': return 18
        if s == 'девятнадцать': return 19
        if s == 'двадцать': return 20
        if s == 'двадцать один': return 21
        if s == 'двадцать два': return 22
        if s == 'двадцать три': return 23
        if s == 'двадцать четыре': return 24
        if s == 'двадцать пять': return 25
        if s == 'двадцать шесть': return 26
        if s == 'двадцать семь': return 27
        if s == 'двадцать восемь': return 28
        if s == 'двадцать девять': return 29
        if s == 'тридцать': return 30
        if s == 'тридцать один': return 31
        if s == 'тридцать два': return 32
        if s == 'тридцать три': return 33
        if s == 'тридцать четыре': return 34
        if s == 'тридцать пять': return 35
        if s == 'тридцать шесть': return 36
        if s == 'тридцать семь': return 37
        if s == 'тридцать восемь': return 38
        if s == 'тридцать девять': return 39
        if s == 'сорок': return 40
        if s == 'сорок один': return 41
        if s == 'сорок два': return 42
        if s == 'сорок три': return 43
        if s == 'сорок четыре': return 44
        if s == 'сорок пять': return 45
        if s == 'сорок шесть': return 46
        if s == '': return 47
        if s == '': return 48
        if s == '': return 49
        if s == '': return 50
        if s == '': return 51
        if s == '': return 52
        if s == '': return 53
        if s == '': return 54
        if s == '': return 55
        if s == '': return 56
        if s == '': return 57
        if s == '': return 58
        if s == '': return 59
        if s == '': return 60
        if s == '': return 61
        if s == '': return 62
        if s == '': return 63
        if s == '': return 64
        if s == '': return 65
        if s == '': return 66
        if s == '': return 67
        if s == '': return 68
        if s == '': return 69
        if s == '': return 70
        if s == '': return 71
        if s == '': return 72
        if s == '': return 73
        if s == '': return 74
        if s == '': return 75
        if s == '': return 76
        if s == '': return 77
        if s == '': return 78
        if s == '': return 79
        if s == '': return 80
        if s == '': return 81
        if s == '': return 82
        if s == '': return 83
        if s == '': return 84
        if s == '': return 85
        if s == '': return 86
        if s == '': return 87
        if s == '': return 88
        if s == '': return 89
        if s == '': return 90
        if s == '': return 91
        if s == '': return 92
        if s == '': return 93
        if s == '': return 94
        if s == '': return 95
        if s == '': return 96
        if s == '': return 97
        if s == '': return 98
        if s == '': return 99

    def pars(s):
        match s:
            case "минус":
                return "-"
            case "плюс":
                return "+"
            case "умножить":
                return "*"
            case "bbb":
                return "("
            case "ccc":
                return ")"
    def unpars(num):
        ...
    
    if "скобка" in s:
        s = s.replace("скобка открывается", "bbb").replace("скобка закрывается", "ccc")
    s = s.split()
    rawS = ""
    for i in s:
        if i == "на": continue
        if i not in NOT_NUMS:
            rawS += pars(i)
        else:
            ...