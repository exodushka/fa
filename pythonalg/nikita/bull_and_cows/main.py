import random
def bull_and_cows():
    number = str(random.randint(0,9999))
    print(f"{number:04}")
    c = input('Привет! Не хочешь сыграть в игру быки и коровы?(да/нет) ')
    if c.lower() == 'да':
        a = 0
        rams = 0
        cows = 0
        print('Тебе нужно отгадать число, которое я загадал. Оно состоит из 4 цифр (0 также может быть на 1 месте)')
        print('Если ты угадал одну цифру, но она не стоит на своём месте, то счетчик коров увеличивается на 1')
        print('Если ты угадал одну цифру и она стоит на своём месте, то счетчик быков увеличивается на 1')
        print('Давай начинать!')
        while a != number:
            a = input('Введи 4-значное число: ')
            if a[0] == number[0]: rams += 1
            if a[1] == number[1]: rams += 1
            if a[2] == number[2]: rams += 1
            if a[3] == number[3]: rams += 1

            if a[0] == number[0] or a[0] == number[1] or a[0] == number[2] or a[0] == number[3] : cows += 1
            if a[1] == number[0] or a[1] == number[1] or a[1] == number[2] or a[1] == number[3] : cows += 1
            if a[2] == number[0] or a[2] == number[1] or a[2] == number[2] or a[2] == number[3]: cows += 1
            if a[3] == number[0] or a[3] == number[1] or a[3] == number[2] or a[3] == number[3] : cows += 1

            print('быки', rams, 'коровы', cows)
            rams, cows = 0, 0
        if a == number:
            print('Молодец, ты правильно отгадал число! ')
    else:
        print('Хорошо,тогда до встречи!')
    return None

if __name__ == "__main__":
    bull_and_cows()