def can_go(move, horse_num):
    present_loc, board_key = horse_dict[horse_num][0], horse_dict[horse_num][1]
    for ix, v1 in enumerate(board[board_key]):
        if v1 == present_loc:
            for v2 in board[board_key][ix + 1:ix + 1 + move]:
                if v2 == 40:
                    new_loc = 40
                    break
                new_loc = v2
            break

    if new_loc in horse_dict.values():
        flag = False
    else:
        present_loc = new_loc
        if board_key == 0 and present_loc == 10:
            board_key = 10
        elif board_key == 0 and present_loc == 20:
            board_key = 20
        elif board_key == 0 and present_loc == 30:
            board_key = 30
        flag = True

    if flag:
        return flag, [present_loc, board_key]
    else:
        return flag, [-1, -1]


def go(move, stage):
    global MAX_VALUE

    if stage == 10:
        tmp_value = 0
        for value in horse_dict.values():
            tmp_value += value[0]
        print(tmp_value)
        if tmp_value > MAX_VALUE:
            MAX_VALUE = tmp_value
        return

    for horse_num in range(1, 5):
        if horse_dict[horse_num][0] == 40:
            continue
        flag, will_be = can_go(move, horse_num)
        if flag:
            tmp = horse_dict[horse_num]
            horse_dict[horse_num] = will_be
            go(move, stage + 1)
            horse_dict[horse_num] = tmp


move_list = list(map(int, input().split()))
board = {
    0: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],
    10: [10, 13, 16, 19, 25, 30, 35, 40],
    20: [20, 22, 24, 25, 30, 35, 40],
    30: [30, 28, 27, 26, 25, 30, 35, 40]
}

horse_dict = {
    1: [0, 0],
    2: [0, 0],
    3: [0, 0],
    4: [0, 0]
}

MAX_VALUE = 0
footprint = [0] * 41
for move in move_list:
    go(move, 0)
