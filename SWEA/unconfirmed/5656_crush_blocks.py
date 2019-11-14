from copy import deepcopy
from collections import deque


def destroy(where, board):
    d = deque()
    for row in range(H):
        if board[row][where]:
            d.append([row, where])
            break

    while d:
        popped = d.popleft()
        row, col = popped[0], popped[1]
        for jump in range(board[row][col]):
            if row + jump < H:
                d.append([row + jump, col])
            if 0 <= row - jump:
                d.append([row - jump, col])
            if col + jump < W:
                d.append([row, col + jump])
            if 0 <= col - jump:
                d.append([row, col - jump])
        board[row][col] = 0

    for col in range(W):
        flag = True
        while flag:
            i_met_zero = -1
            flag_2 = True
            for row in range(H - 1, -1, -1):
                if board[row][col] == 0 and i_met_zero < 0:
                    i_met_zero = row
                    zero = [row, col]
                if i_met_zero > row and board[row][col] > 0:
                    non_zero = [row, col]
                    board[zero[0]][zero[1]], board[non_zero[0]][non_zero[1]] = board[non_zero[0]][non_zero[1]], board[zero[0]][zero[1]]
                    flag_2 = False
                    break
            if flag_2:
                flag = False

    return board


def counter(board):
    cnt = 0
    for row in range(H):
        for col in range(W):
            if board[row][col] > 0:
                cnt += 1
    return cnt


def go(n, board):
    global w
    global answer

    if n == 0:
        num = counter(board)
        if answer > num:
            answer = num
        return

    for w in range(W):
        destroyed = destroy(w, deepcopy(board))
        go(n - 1, destroyed)


tries = int(input())

for t in range(1, tries + 1):
    N, W, H = map(int, input().split())
    board = []
    for _ in range(H):
        board.append(list(map(int, input().split())))

    answer = 180
    go(N, board)

    print('#{} {}'.format(t, answer))
