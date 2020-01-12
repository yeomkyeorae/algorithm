def can_go(move, horse_num):
    present_loc, board_key = horse_dict[horse_num][0], horse_dict[horse_num][1]
    for ix, v1 in enumerate(board[board_key]):
        if v1 == present_loc:
            if v1 == 0:
                new_loc = 0
                break
            for v2 in board[board_key][ix + 1:ix + 1 + move]:
                if v2 == 0:
                    new_loc = 0
                    break
                new_loc = v2
            break

    for value in horse_dict.values():
        if new_loc == 0:
            continue
        if new_loc == 10 and new_loc == value[0]:
            flag = False
            break
        if new_loc == 20 and new_loc == value[0]:
            flag = False
            break
        if new_loc == 30 and new_loc == value[0]:
            flag = False
            break
        if new_loc == 300 and new_loc == value[0]:
            flag = False
            break
        if new_loc == 35 and new_loc == value[0]:
            flag = False
            break
        if new_loc == 25 and new_loc == value[0]:
            flag = False
            break
        if new_loc == 40 and new_loc == value[0]:
            flag = False
            break
        if [new_loc, board_key] == value:
            flag = False
            break

    else:
        present_loc = new_loc
        if board_key == 0 and present_loc == 10:
            board_key = 10
        elif board_key == 0 and present_loc == 20:
            board_key = 20
        elif board_key == 0 and present_loc == 300:
            board_key = 300
        flag = True

    if flag:
        return flag, [present_loc, board_key]
    else:
        return flag, [-1, -1]


def go(move, stage, score):
    global MAX_VALUE

    if stage == 10:
        if score > MAX_VALUE:
            MAX_VALUE = score
        return

    for horse_num in range(1, 5):
        if horse_dict[horse_num][0] == 0:
            continue
        flag, will_be = can_go(move, horse_num)
        if flag:
            tmp = horse_dict[horse_num]
            horse_dict[horse_num] = will_be
            if will_be[0] == -1:
                add_score = 0
            elif will_be[0] == 300:
                add_score = 30
            else:
                add_score = will_be[0]
            go(move_list[stage + 1], stage + 1, score + add_score)
            horse_dict[horse_num] = tmp


move_list = list(map(int, input().split()))
move_list += [0]
board = {
    0: [-1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 300, 32, 34, 36, 38, 40, 0],
    10: [10, 13, 16, 19, 25, 30, 35, 40, 0],
    20: [20, 22, 24, 25, 30, 35, 40, 0],
    300: [300, 28, 27, 26, 25, 30, 35, 40, 0]
}

horse_dict = {
    1: [-1, 0],
    2: [-1, 0],
    3: [-1, 0],
    4: [-1, 0]
}

MAX_VALUE = 0
go(move_list[0], 0, 0)

print(MAX_VALUE)
