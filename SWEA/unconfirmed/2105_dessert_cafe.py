d = [[1, 1], [1, -1], [-1, -1], [-1, 1]]


def make_rectangle(row, col, one, two):
    global answer
    if answer == (one + two) * 2:
        return
    axis = []
    for _ in range(one):
        row += d[2][0]
        col += d[2][1]
        if visited[board[row][col]] or (0 > row or row >= n) or (0 > col or col >= n):
            for ax in axis:
                visited[board[ax[0]][ax[1]]] = 0
            return
        axis.append([row, col])
        visited[board[row][col]] = 1

    for i in range(two):
        row += d[3][0]
        col += d[3][1]
        if i == two - 1:
            break
        if visited[board[row][col]] or (0 > row or row >= n) or (0 > col or col >= n):
            for ax in axis:
                visited[board[ax[0]][ax[1]]] = 0
            return
        axis.append([row, col])
        visited[board[row][col]] = 1
    if answer < (one + two) * 2:
        answer = (one + two) * 2

    for ax in axis:
        visited[board[ax[0]][ax[1]]] = 0


def second_go(row, col, one, two):
    if 0 <= row < n and 0 <= col < n:
        if visited[board[row][col]]:
            return
        else:
            visited[board[row][col]] = 1
        make_rectangle(row, col, one, two)
        second_go(row + d[1][0], col + d[1][1], one, two + 1)
        visited[board[row][col]] = 0


def first_go(row, col, one):
    if 0 <= row < n and 0 <= col < n:
        if visited[board[row][col]]:
            return
        else:
            visited[board[row][col]] = 1
        second_go(row + d[1][0], col + d[1][1], one, 1)
        first_go(row + d[0][0], col + d[0][1], one + 1)
        visited[board[row][col]] = 0


tries = int(input())
for t in range(1, tries + 1):
    n = int(input())
    board = []
    visited = [0] * 101
    for _ in range(n):
        board.append(list(map(int, input().split())))

    answer = -1
    for row in range(n):
        for col in range(n):
            visited[board[row][col]] = 1
            first_go(row + d[0][0], col + d[0][1], 1)
            visited[board[row][col]] = 0

    print('#{} {}'.format(t, answer))
