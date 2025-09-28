from random import randint

def game():
    secret_number = str(randint(1000, 9999))
    #print(secret_number)
    while True:
        user_number = input("Введите число: ")
        try:
            int(user_number)
            char1, char2, char3, char4 = user_number[0], user_number[1], user_number[2], user_number[3]
            if (user_number.count(char1) + user_number.count(char2) + user_number.count(char3) + user_number.count(char4)) != 0:

                bulls = (secret_number[0] == char1) + (secret_number[1] == char2) + (secret_number[2] == char3) + (secret_number[3] == char4)
                #cows = (secret_number.count(char1)) + (secret_number.count(char2)) + (secret_number.count(char3)) + (secret_number.count(char4)) - bulls
                #cows = (char1 in secret_number and char1 != secret_number[0]) + (char2 in secret_number and char2 != secret_number[1]) + (char3 in secret_number and char3 != secret_number[2]) + (char4 in secret_number and char4 != secret_number[3])
                num = [i for i in secret_number]
                for i in user_number:
                    if i in num:
                        num.remove(i)
                cows = 4 - len(num) - bulls
                if bulls == 4: break
                printdata(bulls = bulls, cows = cows)
            else:
                printdata(0,0)
        except ValueError:
            print("Введено некоректное число")

    print("Победа")
    

def printdata(bulls: int, cows: int):
    print(f"Коров: {cows}")
    print(f"Быков: {bulls}")

if __name__ == "__main__":
    game()