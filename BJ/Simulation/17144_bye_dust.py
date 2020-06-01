def diffuse():
    global R, C, board, puri

    tmp_board = []
    for _ in range(R):
        tmp_board.append([0] * C)

    pass_list = []
    for r in range(R):
        for c in range(C):
            if board[r][c] > 0:
                pass_list.append([r, c])
                cnt = 0
                tmp_list = []
                if 0 <= r - 1 and board[r - 1][c] != -1:
                    cnt += 1
                    tmp_list.append([r - 1, c])
                if r + 1 < R and board[r + 1][c] != -1:
                    cnt += 1
                    tmp_list.append([r + 1, c])
                if 0 <= c - 1 and board[r][c - 1] != -1:
                    cnt += 1
                    tmp_list.append([r, c - 1])
                if c + 1 < C and board[r][c + 1] != -1:
                    cnt += 1
                    tmp_list.append([r, c + 1])
                diffuse_value = int(board[r][c] / 5)
                board[r][c] = board[r][c] - diffuse_value * cnt
                for tmp_r, tmp_c in tmp_list:
                    tmp_board[tmp_r][tmp_c] += diffuse_value

    for r in range(R):
        for c in range(C):
            if [r, c] in puri:
                continue
            if [r, c] in pass_list:
                board[r][c] += tmp_board[r][c]
                continue
            board[r][c] = tmp_board[r][c]


def upper_wind(row, col):
    global R, C, board

    tmp_value = [0]
    tmp_axis = []
    for c in range(col, C - 1):
        tmp_value.append(board[row][c + 1])
        tmp_axis.append([row, c + 1])

    for r in range(row, 0, -1):
        tmp_value.append(board[r - 1][C - 1])
        tmp_axis.append([r - 1, C - 1])

    for c in range(C - 1, 0, -1):
        tmp_value.append(board[0][c - 1])
        tmp_axis.append([0, c - 1])

    for r in range(R - 1, row):
        tmp_value.append(board[r + 1][0])
        tmp_axis.append([r + 1, 0])

    if col != 0:
        for c in range(col - 1):
            tmp_value.append(board[row][c + 1])
            tmp_axis.append([row, c + 1])

    for a, b in zip(tmp_value[:-1], tmp_axis):
        board[b[0]][b[1]] = a


def bottom_wind(row, col):
    global R, C, board

    tmp_value = [0]
    tmp_axis = []
    for c in range(col, C - 1):
        tmp_value.append(board[row][c + 1])
        tmp_axis.append([row, c + 1])

    for r in range(row, R - 1):
        tmp_value.append(board[r + 1][C - 1])
        tmp_axis.append([r + 1, C - 1])

    for c in range(C - 1, 0, -1):
        tmp_value.append(board[R - 1][c - 1])
        tmp_axis.append([R - 1, c - 1])

    for r in range(R - 1, row + 1, -1):
        tmp_value.append(board[r - 1][0])
        tmp_axis.append([r - 1, 0])

    if col != 0:
        for c in range(col - 1):
            tmp_value.append(board[row][c + 1])
            tmp_axis.append([row, c + 1])

    for a, b in zip(tmp_value[:-1], tmp_axis):
        board[b[0]][b[1]] = a


def wind():
    global puri

    upper_wind(puri[0][0], puri[0][1])
    bottom_wind(puri[1][0], puri[1][1])


def go():
    diffuse()
    wind()


R, C, T = map(int, input().split())

board = []
puri = []
for r in range(R):
    tmp_list = list(map(int, input().split()))
    if -1 in tmp_list:
        puri.append([r, tmp_list.index(-1)])
    board.append(tmp_list)

for _ in range(T):
    go()

answer = 2
for row in range(R):
    for col in range(C):
        answer += board[row][col]

print(answer)
