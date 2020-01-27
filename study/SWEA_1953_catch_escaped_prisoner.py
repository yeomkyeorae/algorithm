tunnel_type = {
    1: [1, 2, 3, 4],
    2: [1, 3],
    3: [2, 4],
    4: [1, 2],
    5: [2, 3],
    6: [3, 4],
    7: [1, 4]
}

tunnel_couple = {
    1: 3,
    2: 4,
    3: 1,
    4: 2
}

dxdy = {
    1: [-1, 0],
    2: [0, 1],
    3: [1, 0],
    4: [0, -1]
}


from collections import deque


def bfs(r, c):

    d = deque()
    d.append([r, c, 1])
    visited[r][c] = 1

    cnt = 0
    while d:
        popped = d.popleft()
        row, col, stage = popped[0], popped[1], popped[2]
        if stage > L:
            return cnt
        cnt += 1

        for direction in tunnel_type[board[row][col]]:
            dx, dy = dxdy[direction][0], dxdy[direction][1]
            if 0 <= row + dx < N and 0 <= col + dy < M:
                if board[row + dx][col + dy]:
                    if not visited[row + dx][col + dy]:
                        if tunnel_couple[direction] in tunnel_type[board[row + dx][col + dy]]:
                            d.append([row + dx, col + dy, stage + 1])
                            visited[row + dx][col + dy] = 1

    return cnt


tries = int(input())

for T in range(1, tries + 1):
    N, M, R, C, L = map(int, input().split())

    board = []
    visited = []
    for _ in range(N):
        visited.append([0] * M)
        board.append(list(map(int, input().split())))

    visited[R][C] = 1
    ANSWER = bfs(R, C)

    print('#{} {}'.format(T, ANSWER))
