map = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]

def main():
    global map
    player = True
    #True - крестик
    #False - нолик
    while True:
        if game_end()[0]:
            print_map()
            break
        else:
            while True:
                print_map()
                print(f"Сейчас ходит: {"крестик" if player else "нолик"}")
                user_motion = input("Введите ход: ")
                if (user_motion in ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]):
                    if player:
                        if motion(user_motion=user_motion, player=player):
                            player = False
                            break
                        else: 
                            print("Неверный ход")
                    else:
                        if motion(user_motion=user_motion, player=player): 
                            player = True
                            break
                        else:
                            print("Неверный ход")
                    break
                else:
                    print("Неверный ход")

    print("Игра окончена")
    if game_end()[1] == "x": 
        print("Победа крестиков")
    elif game_end()[1] == "o":
        print("Победа ноликов")
    else:
        print("Ничья")

def game_end():
    """
    false - игра не окончена
    true - игра окончена
    """
    global map

    if ((map[0].count(" ")) + (map[1].count(" ")) + (map[2].count(" "))) == 0: return True, " "

    #горизантальные ряды
    if (map[0][0] == map[0][1] == map[0][2] != " "): return True, map[0][0]# верхний ряд
    if (map[1][0] == map[1][1] == map[1][2] != " "): return True, map[1][0]# средний ряд
    if (map[2][0] == map[2][1] == map[2][2] != " "): return True, map[2][0]# нижний ряд

    #вертикальные ряды
    if (map[0][0] == map[1][0] == map[2][0] != " "): return True, map[0][0] #левый ряд
    if (map[0][1] == map[1][1] == map[2][1] != " "): return True, map[0][1] #центральный ряд
    if (map[0][2] == map[1][2] == map[2][2] != " "): return True, map[0][2] #левый ряд

    #кресты
    if (map[0][0] == map[1][1] == map[2][2] != " "): return True, map[0][0] #с левого края
    if (map[0][2] == map[1][1] == map[2][0] != " "): return True, map[0][2] #с правого края
    return False, "bug"

def motion(user_motion, player):
    global map
    player = ["o", "x"][int(player)]
    match user_motion[0]:
        case "a":
            match user_motion[1]:
                case "1":
                    if (map[0][0] == " "):
                        map[0][0] = player
                    else: return False
                case "2":
                    if (map[0][1] == " "):
                        map[0][1] = player
                    else: return False
                case "3":
                    if (map[0][2] == " "):
                        map[0][2] = player
                    else: return False
        case "b":
            match user_motion[1]:
                case "1":
                    if (map[1][0] == " "):
                        map[1][0] = player
                    else: return False
                case "2":
                    if (map[1][1] == " "):
                        map[1][1] = player
                    else: return False
                case "3":
                    if (map[1][2] == " "):
                        map[1][2] = player
                    else: return False
        case "c":
            match user_motion[1]:
                case "1":
                    if (map[2][0] == " "):
                        map[2][0] = player
                    else: return False
                case "2":
                    if (map[2][1] == " "):
                        map[2][1] = player
                    else: return False
                case "3":
                    if (map[2][2] == " "):
                        map[2][2] = player
                    else: return False
    return True

def print_map():
    global map
    print("  1 2 3")
    print(f"a {map[0][0]} {map[0][1]} {map[0][2]}")
    print(f"b {map[1][0]} {map[1][1]} {map[1][2]}")
    print(f"c {map[2][0]} {map[2][1]} {map[2][2]}")


if __name__ == "__main__":
    main()
