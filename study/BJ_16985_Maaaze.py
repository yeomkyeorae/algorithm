from itertools import product, permutations
from collections import deque


rows = [0, 1, -1, 0]
cols = [1, 0, 0, -1]
zs = [-1, 1]


def rotate_list(one_board):
    tmp_board = []
    for _ in range(5):
        tmp_board.append([0] * 5)
    for row in range(5):
        for col in range(5):
            tmp_board[col][4 - row] = one_board[row][col]

    return tmp_board


def add_rotated(one_board):
    tmp_list = [one_board]
    for _ in range(3):
        one_board = rotate_list(one_board)
        tmp_list.append(one_board)

    return tmp_list


def input_board():
    tmp_board = []
    for _ in range(5):
        tmp_board.append(list(map(int, input().split())))
    return tmp_board


def bfs(one_board):
    global result

    visited = []
    for _ in range(5):
        tmp_list = []
        for _ in range(5):
            tmp_list.append([0] * 5)
        visited.append(tmp_list)

    d = deque()
    d.append([0, 0, 0, 0])
    visited[0][0][0] = 1
    while d:
        popped = d.popleft()
        distance = popped[3]
        if distance >= result:
            return 0
        channel, row, col = popped[0], popped[1], popped[2]
        if channel == 4 and row == 4 and col == 4:
            if distance < result:
                result = distance
            return 1
        for r, c in zip(rows, cols):
            if 0 <= row + r < 5 and 0 <= col + c < 5 and visited[channel][row + r][col + c] == 0 and one_board[channel][row + r][col + c] == 1:
                d.append([channel, row + r, col + c, distance + 1])
                visited[channel][row + r][col + c] = 1
        for z in zs:
            if 0 <= channel + z < 5 and visited[channel + z][row][col] == 0 and one_board[channel + z][row][col] == 1:
                d.append([channel + z, row, col, distance + 1])
                visited[channel + z][row][col] = 1

    return 0


board_0, board_1, board_2, board_3, board_4 = input_board(), input_board(), input_board(), input_board(), input_board()
list_0, list_1, list_2, list_3, list_4 = add_rotated(board_0), add_rotated(board_1), add_rotated(board_2), add_rotated(board_3), add_rotated(board_4)
total_dict = {
    0: list_0,
    1: list_1,
    2: list_2,
    3: list_3,
    4: list_4
}

flag = False
can_go_flag = False
result = 60
j = 0
for stack_perm in permutations([0, 1, 2, 3, 4]):
    if flag:
        break
    for dir_perm in product([0, 1, 2, 3], repeat=5):
        if result == 12:
            flag = True
            break
        board = []
        for total_dict_key, ix in zip(stack_perm, dir_perm):
            board.append(total_dict[total_dict_key][ix])
        if board[0][0][0] == 0 or board[4][4][4] == 0:
            continue
        if bfs(board) == 1:
            can_go_flag = True

if can_go_flag:
    print(result)
else:
    print(-1)
