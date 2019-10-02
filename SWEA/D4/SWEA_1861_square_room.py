def go(row, col, n):

    visited[board[row][col]] = 1

    global MAX
    global ROOM_FLAG
    flag = True

    if row - 1 >= 0 and board[row - 1][col] == board[row][col] + 1 and not visited[board[row - 1][col]]:
        flag = False
        go(row - 1, col, n + 1)
    if row + 1 < N and board[row + 1][col] == board[row][col] + 1 and not visited[board[row + 1][col]]:
        flag = False
        go(row + 1, col, n + 1)
    if col - 1 >= 0 and board[row][col - 1] == board[row][col] + 1 and not visited[board[row][col - 1]]:
        flag = False
        go(row, col - 1, n + 1)
    if col + 1 < N and board[row][col + 1] == board[row][col] + 1 and not visited[board[row][col + 1]]:
        flag = False
        go(row, col + 1, n + 1)

    if flag:
        if MAX < n:
            MAX = n
        elif MAX == n:
            ROOM_FLAG = True


tries = int(input())

for t in range(1, tries + 1):
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))

    path = [0] * 1000001
    for row in range(N):
        for col in range(N):
            path[board[row][col]] = (row, col)

    MAX = 0
    ROOM_NUM = -1
    visited = [0] * (N * N + 1)
    for one in path[1:]:
        if type(one) == tuple:
            tmp = MAX
            ROOM_FLAG = False
            go(one[0], one[1], 1)
            if tmp < MAX:
                ROOM_NUM = board[one[0]][one[1]]
            if ROOM_FLAG:
                if ROOM_NUM > board[one[0]][one[1]]:
                    ROOM_NUM = board[one[0]][one[1]]
        else:
            break

    print('#{} {} {}'.format(t, ROOM_NUM, MAX))
