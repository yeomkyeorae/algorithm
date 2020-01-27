dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(r, c, p, stage):

    global ANSWER

    if ANSWER < stage:
        ANSWER = stage

    for px, py in zip(dx, dy):
        if 0 <= r + px < n and 0 <= c + py < n:
            if not visited[r + px][c + py]:
                if board[r][c] <= board[r + px][c + py] and p:
                    for cut in range(1, k + 1):
                        if board[r][c] > board[r + px][c + py] - cut:
                            tmp = board[r + px][c + py]

                            board[r + px][c + py] = board[r + px][c + py] - cut
                            visited[r + px][c + py] = 1

                            dfs(r + px, c + py, 0, stage + 1)

                            board[r + px][c + py] = tmp
                            visited[r + px][c + py] = 0

                            break

                elif board[r][c] > board[r + px][c + py]:
                    visited[r + px][c + py] = 1
                    dfs(r + px, c + py, p, stage + 1)
                    visited[r + px][c + py] = 0


tries = int(input())

for t in range(1, tries + 1):
    n, k = map(int, input().split())

    board = []
    max_value = 0
    max_loc = []
    visited = []
    for row in range(n):
        visited.append([0] * n)
        tmp_list = list(map(int, input().split()))
        for col, value in enumerate(tmp_list):
            if value > max_value:
                max_value = value
                max_loc = [(row, col)]
            elif value == max_value:
                max_loc.append((row, col))
        board.append(tmp_list)

    ANSWER = -1
    for r, c in max_loc:
        visited[r][c] = 1
        dfs(r, c, 1, 1)
        visited[r][c] = 0

    print('#{} {}'.format(t, ANSWER))
