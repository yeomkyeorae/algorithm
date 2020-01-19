def where_can_i_go(row, col):
    diffusion_list = []
    cnt = 0
    if row + 1 != R and board[row + 1][col] >= 0:
        diffusion_list.append([row + 1, col])
        cnt += 1
    if row - 1 != -1 and board[row - 1][col] >= 0:
        diffusion_list.append([row - 1, col])
        cnt += 1
    if col + 1 != C and board[row][col + 1] >= 0:
        diffusion_list.append([row, col + 1])
        cnt += 1
    if col - 1 != -1 and board[row][col - 1] >= 0:
        diffusion_list.append([row, col - 1])
        cnt += 1

    return cnt, diffusion_list


def diffuse():
    global board

    tmp_board = []
    for _ in range(R):
        tmp_board.append([0] * C)
    for i in range(2):
        tmp_board[machine_loc[i][0]][machine_loc[i][1]] = -1

    for row in range(R):
        for col in range(C):
            if board[row][col] > 0:
                cnt, diffusion_list = where_can_i_go(row, col)
                for r, c in diffusion_list:
                    tmp_board[r][c] += board[row][col] // 5
                tmp_board[row][col] += board[row][col] - (board[row][col] // 5) * cnt

    board = tmp_board


def operate():
    global board

    # 위 공기청정기 : 반 시계
    row, col = machine_loc[0][0], machine_loc[0][1]
    before = 0
    ix = -1
    for i in range(1, C - col):
        tmp = board[row][col + i]
        board[row][col + i] = before
        before = tmp
        ix = i
    c = col + ix

    for i in range(1, row + 1):
        tmp = board[row - i][c]
        board[row - i][c] = before
        before = tmp
        ix = i
    r = row - ix

    for i in range(1, c + 1):
        tmp = board[r][c - i]
        board[r][c - i] = before
        before = tmp
        ix = i
    c = c - ix

    for i in range(1, row + 1):
        tmp = board[r + i][c]
        board[r + i][c] = before
        before = tmp
        ix = i
    r = ix
    print(board)
    if board[r][c] != -1:
        for i in range(C - 1):
            if board[r][c + 1 + i] == -1:
                break
            tmp = board[r][c + 1 + i]
            board[r][c + 1 + i] = before
            before = tmp

    # 아 공기청정기 : 시계
    # row, col = machine_loc[1][0], machine_loc[1][1]
    # before = 0
    # ix = -1
    # for i in range(1, C - col):
    #     tmp = board[row][col + i]
    #     board[row][col + i] = before
    #     before = tmp
    #     ix = i
    # c = col + ix
    #
    # for i in range(1, R - row):
    #     tmp = board[row + i][c]
    #     board[row + i][c] = before
    #     before = tmp
    #     ix = i
    # r = row + ix
    #
    # for i in range(1, col + 1):
    #     tmp = board[r][c - i]
    #     board[r][c - i] = before
    #     before = tmp
    #     ix = i
    # c = c - ix
    #
    # for i in range(1, R - row):
    #     tmp = board[r - i][c]
    #     if board[r - i][c] == -1:
    #         continue
    #     board[r - i][c] = before
    #     before = tmp


def summation():
    answer = 0
    for r in range(R):
        for c in range(C):
            if board[r][c] > 0:
                answer += board[r][c]

    return answer


R, C, T = map(int, input().split())

board = []
machine_loc = []
for r in range(R):
    input_list = list(map(int, input().split()))
    if -1 in input_list:
        machine_loc.append([r, input_list.index(-1)])
    board.append(input_list)

for _ in range(T):
    # diffuse()
    operate()
for v in board:
    print(v)
answer = summation()
print(answer)


# 5 5 1
# 1 2 3 4 5
# 6 7 8 9 10
# -1 11 12 13 14
# -1 15 16 17 18
# 19 20 21 22 23

# 5 5 1
# 1 2 3 4 5
# 6 7 8 9 10
# 11 12 -1 13 14
# 15 16 -1 17 18
# 19 20 21 22 23