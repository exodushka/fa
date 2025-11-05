def clicker_solver(up : int, goal : int) -> int:
    if up == 0 or goal == 0:
        if up == 0 and goal == 0:
            return 0
        if up == 0 and goal != 0:
            return -1
        if up != 0 and goal == 0:
            return 0
    upgrade_cost = up ** 3
    count = 0
    clicks = 0
    while count < goal:
        while (count < upgrade_cost and count < goal) and (not(count == goal)):
            count += up
            clicks += 1
            print(count, clicks, up)
        if count >= goal:
            return clicks
        if ((goal - count) / up) > ((goal - (count - upgrade_cost)) / (up*2)):
            count -= upgrade_cost
            up *= 2
            upgrade_cost = up **3
            clicks += 1
    return clicks
    raise NotImplementedError

print(clicker_solver(5,3030)) # 11