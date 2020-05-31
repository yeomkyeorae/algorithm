def search(row, col, k):
    global board
    global N

    # 중앙
    home_cnt = 0
    if board[row][col]:
        home_cnt += 1
    for i in range(1, k):
        if 0 <= col - i:
            if board[row][col - i]:
                home_cnt += 1
        if col + i < N:
            if board[row][col + i]:
                home_cnt += 1

    # 위쪽
    for r in range(1, k):
        if 0 <= row - r:
            if board[row - r][col]:
                home_cnt += 1
            for i in range(1, k - r):
                if 0 <= col - i:
                    if board[row - r][col - i]:
                        home_cnt += 1
                if col + i < N:
                    if board[row - r][col + i]:
                        home_cnt += 1

    # 아래 쪽
    for r in range(1, k):
        if row + r < N:
            if board[row + r][col]:
                home_cnt += 1
            for i in range(1, k - r):
                if 0 <= col - i:
                    if board[row + r][col - i]:
                        home_cnt += 1
                if col + i < N:
                    if board[row + r][col + i]:
                        home_cnt += 1

    return home_cnt


def go(k):
    global N
    global answer
    global cost

    total_k = k * k + (k - 1) * (k - 1)
    for row in range(N):
        for col in range(N):
            home_cnt = search(row, col, k)
            if total_k <= cost * home_cnt and answer < home_cnt:
                answer = home_cnt


tries = int(input())

for t in range(1, tries + 1):
    N, cost = map(int, input().split())

    board = []
    answer = 0
    for _ in range(N):
        board.append(list(map(int, input().split())))

    max_k = 21
    for k in range(1, max_k + 1):
        go(k)

    print('#{} {}'.format(t, answer))
