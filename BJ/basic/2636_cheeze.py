import sys
from collections import deque
input = sys.stdin.readline

ROW, COL = list(map(int, input().split()))
AIR_CANDIDATE = 0
CHEEZE = 1
AIR = 3

board = []
for _ in range(ROW):
    board.append(list(map(int, input().split())))
    
time = 0
last_count = 0
while True:
    d = deque()
    d.append([0, 0])
    
    visited = []
    for _ in range(ROW):
        visited.append([0] * COL)
    
    while d:
        row, col = d.popleft()
        board[row][col] = AIR
        if 0 <= row - 1 and board[row - 1][col] in [AIR_CANDIDATE, AIR] and not visited[row - 1][col]:
            visited[row - 1][col] = 1
            d.append([row - 1, col])
        if row + 1 < ROW and board[row + 1][col] in [AIR_CANDIDATE, AIR] and not visited[row + 1][col]:
            visited[row + 1][col] = 1
            d.append([row + 1, col])
        if 0 <= col - 1 and board[row][col - 1] in [AIR_CANDIDATE, AIR] and not visited[row][col - 1]:
            visited[row][col - 1] = 1
            d.append([row, col - 1])
        if col + 1 < COL and board[row][col + 1] in [AIR_CANDIDATE, AIR] and not visited[row][col + 1]:
            visited[row][col + 1] = 1
            d.append([row, col + 1])
    
    count = 0
    melting_cheeze = []
    has_cheeze = False

    for row in range(ROW):
        for col in range(COL):
            if board[row][col] == CHEEZE:
                has_cheeze = True
                count += 1
                
                if 0 <= row - 1 and board[row - 1][col] == AIR:
                    melting_cheeze.append([row, col])
                elif row + 1 < ROW and board[row + 1][col] == AIR:
                    melting_cheeze.append([row, col])
                elif 0 <= col - 1 and board[row][col - 1] == AIR:
                    melting_cheeze.append([row, col])
                elif col + 1 < COL and board[row][col + 1] == AIR:
                    melting_cheeze.append([row, col])

    for row, col in melting_cheeze:
        board[row][col] = AIR_CANDIDATE

    if not has_cheeze:
        break

    time += 1
    last_count = count
    
print(time)
print(last_count)
