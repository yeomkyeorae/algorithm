def make_area(row, col, k):
    axis = []
    for i in range(k):
        axis.append([row + i, col])
        if i != 0:
            axis.append([row - i, col])

    j = 1
    k -= 1
    while k > 0:
        for i in range(k):
            axis.append([row + i, col + j])
            if i != 0:
                axis.append([row - i, col + j])
        for i in range(k):
            axis.append([row + i, col - j])
            if i != 0:
                axis.append([row - i, col - j])
        k -= 1
        j += 1

    return axis


tries = int(input())

for t in range(1, tries + 1):
    n, m = map(int, input().split())
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))

    answer = -1
    for row in range(n):
        for col in range(n):
            for k in range(1, n + 2):
                axis = make_area(row, col, k)
                home_cnt = 0
                for ax in axis:
                    if 0 <= ax[0] < n and 0 <= ax[1] < n:
                        if board[ax[0]][ax[1]] == 1:
                            home_cnt += 1
                if m * home_cnt >= len(axis):
                    if home_cnt > answer:
                        answer = home_cnt

    print('#{} {}'.format(t, answer))
