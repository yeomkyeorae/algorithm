def dfs(start_col):

    global min_value
    value = 0
    num = 0
    for r in range(n):
        for c in range(n):
            if visited[r][c] == 1:
                num += 1
                value += board[r][c]
    if value > min_value:
        return
    if start_col == n:
        if min_value > value and num == n:
            min_value = value
        return

    for row in range(n):
        flag = True
        for col in range(n):
            if visited[row][col] == 1:
                flag = False
                break
        if flag:
            visited[row][start_col] = 1
            dfs(start_col + 1)
            visited[row][start_col] = 0


tries = int(input())

for t in range(1, tries + 1):
    n = int(input())

    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))

    visited = []
    for _ in range(n):
        visited.append([0] * n)

    min_value = 100
    dfs(0)

    print('#{} {}'.format(t, min_value))
