def can_go(move, horse_num):
    flag, will_be = True, 20
    return flag, will_be


def go(move):
    flag, will_be = can_go(move, horse_num)
    if flag:
        footprint[will_be] = horse_num
        go(move, horse_num)
        footprint[will_be] = 0


move_list = list(map(int, input().split()))
board = {
    0: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],
    10: [13, 16, 19, 25, 30, 35, 40],
    20: [22, 24, 25, 30, 35, 40],
    30: [28, 27, 26, 25, 30, 35, 40]
}

horse_dict = {
    1: 0,
    2: 0,
    3: 0,
    4: 0
}

MAX_VALUE = 0
footprint = [0] * 41
for move in move_list:
    go(move)
