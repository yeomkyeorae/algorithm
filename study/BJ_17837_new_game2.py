direction = {
    1: [0, 1],
    2: [0, -1],
    3: [-1, 0],
    4: [1, 0]
}
reverse_direction = {
    1: 2,
    2: 1,
    3: 4,
    4: 3
}

n, k = map(int, input().split())

color_board = []
for _ in range(n):
    tmp_list = list(map(int, input().split()))
    color_board.append(tmp_list)

horse_board = []
for _ in range(n):
    tmp_list = []
    for _ in range(n):
        tmp_list.append([])
    horse_board.append(tmp_list)

horse_dict = {}
for i in range(k):
    r, c, d = map(int, input().split())
    horse_board[r - 1][c - 1].append(i + 1)
    horse_dict[i + 1] = [r, c, d]


def white_or_red(old_r, old_c, new_r, new_c, horse_num, type_num):
    length = len(horse_board[old_r][old_c])
    ix = 0
    for i, h in enumerate(horse_board[old_r][old_c]):
        if h == horse_num:
            ix = i
        break
    t_list = []
    for _ in range(length - ix):
        popped = horse_board[old_r][old_c].pop()
        horse_dict[popped] = [new_r + 1, new_c + 1, horse_dict[popped][2]]
        t_list.append(popped)
    if type_num == 0:
        t_list.reverse()

    horse_board[new_r][new_c] = horse_board[new_r][new_c] + t_list

    return new_r, new_c


def blue(old_r, old_c, new_r, new_c, horse_num):
    length = len(horse_board[old_r][old_c])
    ix = 0
    for i, h in enumerate(horse_board[old_r][old_c]):
        if h == horse_num:
            ix = i
        break

    if 0 > new_r or n <= new_r:
        return old_r, old_c

    if 0 > new_c or n <= new_c:
        return old_r, old_c

    if color_board[new_r][new_c] == 2:
        return old_r, old_c

    t_list = []
    for _ in range(length - ix):
        popped = horse_board[old_r][old_c].pop()
        horse_dict[popped] = [new_r + 1, new_c + 1, horse_dict[popped][2]]
        t_list.append(popped)

    horse_board[new_r][new_c] = horse_board[new_r][new_c] + t_list

    return new_r, new_c


def go(one_list, horse_num):
    row, col, direct = one_list
    add_row, add_col = direction[direct]
    row_ix = row + add_row - 1
    col_ix = col + add_col - 1
    if 0 <= row_ix < n and 0 <= col_ix < n:
        # 하얀색
        if color_board[row_ix][col_ix] == 0:
            white_row, white_col = white_or_red(row - 1, col - 1, row_ix, col_ix, horse_num, 0)
            one_list = [white_row + 1, white_col + 1, direct]
        # 빨간색
        elif color_board[row_ix][col_ix] == 1:
            red_row, red_col = white_or_red(row - 1, col - 1, row_ix, col_ix, horse_num, 1)
            one_list = [red_row + 1, red_col + 1, direct]
        # 파란색
        else:
            add_row, add_col = direction[reverse_direction[direct]]
            blue_row, blue_col = blue(row - 1, col - 1, row + add_row - 1, col + add_col - 1, horse_num)
            one_list = [blue_row + 1, blue_col + 1, reverse_direction[direct]]
    else:
        add_row, add_col = direction[reverse_direction[direct]]
        blue_row, blue_col = blue(row - 1, col - 1, row + add_row - 1, col + add_col - 1, horse_num)
        one_list = [blue_row + 1, blue_col + 1, reverse_direction[direct]]
    return one_list


def check(horse_board):
    for i in range(n):
        for j in range(n):
            if len(horse_board[i][j]) == 4:
                return True
    return False


answer = 0
flag = False
for i in range(1, 1001):
    for j in range(k):
        one_list = horse_dict[j + 1]
        one_list = go(one_list, j + 1)
        horse_dict[j + 1] = one_list
        flag = check(horse_board)
        if flag:
            break
    if flag:
        answer = i
        break

if not flag:
    answer = -1

print(answer)
