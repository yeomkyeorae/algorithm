from collections import deque


directions = {
    1: [[1, 0], [-1, 0], [0, 1], [0, -1]],
    2: [[1, 0], [-1, 0]],
    3: [[0, 1], [0, -1]],
    4: [[-1, 0], [0, 1]],
    5: [[1, 0], [0, 1]],
    6: [[0, -1], [1, 0]],
    7: [[-1, 0], [0, -1]]
}


def can_i_go(row, col, dy, dx, time):
    for direct in directions[board[row + dy][col + dx]]:
        if dy + direct[0] == 0 and dx + direct[1] == 0:
            if not visited[row + dy][col + dx]:
                if time > L:
                    return False
                d.append([row + dy, col + dx, time])
                visited[row + dy][col + dx] = 1
    return True


def go(r, c):
    d.append([r, c, 1])
    visited[r][c] = 1
    while d:
        popped = d.popleft()
        row = popped[0]
        col = popped[1]

        value = board[row][col]
        for i in range(1, 8):
            if value == i:
                for direction in directions[value]:
                    dy = direction[0]
                    dx = direction[1]
                    if 0 <= row + dy < N and 0 <= col + dx < M:
                        if board[row + dy][col + dx] > 0:
                            if not can_i_go(row, col, dy, dx, popped[2] + 1):
                                return
                break


tries = int(input())

for t in range(1, tries + 1):
    N, M, start_r, start_c, L = map(int, input().split())

    board = []
    visited = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
        visited.append([0] * M)

    d = deque()
    go(start_r, start_c)

    cnt = 0
    for row in range(N):
        for col in range(M):
            if visited[row][col] == 1:
                cnt += 1

    print('#{} {}'.format(t, cnt))
