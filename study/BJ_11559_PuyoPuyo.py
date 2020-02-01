from collections import deque


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def bfs(row, col, ch):

    visited = []
    for _ in range(12):
        visited.append([0] * 6)

    d = deque()
    d.append([row, col])
    visited[row][col] = 1
    cnt = 1

    while d:
        p = d.popleft()
        for pr, pc in zip(dr, dc):
            new_r, new_c = p[0] + pr, p[1] + pc
            if 0 <= new_r < 12 and 0 <= new_c < 6:
                if board[new_r][new_c] == ch:
                    if not visited[new_r][new_c]:
                        d.append([new_r, new_c])
                        visited[new_r][new_c] = 1
                        cnt += 1

    return cnt, visited


def bomb(visited):
    global board

    for row in range(12):
        for col in range(6):
            if visited[row][col]:
                board[row][col] = '.'


def move():
    global board

    for col in range(6):
        tmp = []
        for row in range(11, -1, -1):
            if board[row][col] != '.':
                tmp.append(board[row][col])
                board[row][col] = '.'
        for row in range(len(tmp)):
            board[11 - row][col] = tmp[row]


board = []
for _ in range(12):
    tmp = []
    for el in input():
        tmp.append(el)
    board.append(tmp)

flag = True
ANSWER = 0
while flag:
    flag = False
    for row in range(12):
        for col in range(6):
            if board[row][col] != '.':
                cnt, visited = bfs(row, col, board[row][col])
                if cnt >= 4:
                    bomb(visited)
                    flag = True
    if flag:
        move()
        ANSWER += 1

print(ANSWER)
