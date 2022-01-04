from collections import deque


row, col, k = list(map(int, input().split()))

board = []
for _ in range(row):
    board.append([0] * col)

for _ in range(k):
    c1, rr1, c2, rr2 = list(map(int, input().split()))
    
    for r in range(row - rr2, row - rr1):
        for c in range(c1, c2):
            board[r][c] = 1
            
answer = []   
for r in range(row):
    for c in range(col):
        if not board[r][c]:
            d = deque()
            d.append([r, c])
            board[r][c] = 1
            
            area = 1
            while d:
                cur_row, cur_col = d.popleft()
                
                if 0 <= cur_row + 1 < row and not board[cur_row + 1][cur_col]:
                    d.append([cur_row + 1, cur_col])
                    board[cur_row + 1][cur_col] = 1
                    area += 1
                if 0 <= cur_row - 1 < row and not board[cur_row - 1][cur_col]:
                    d.append([cur_row - 1, cur_col])
                    board[cur_row - 1][cur_col] = 1
                    area += 1
                if 0 <= cur_col + 1 < col and not board[cur_row][cur_col + 1]:
                    d.append([cur_row, cur_col + 1])
                    board[cur_row][cur_col + 1] = 1
                    area += 1
                if 0 <= cur_col - 1 <= col and not board[cur_row][cur_col - 1]:
                    d.append([cur_row, cur_col - 1])
                    board[cur_row][cur_col - 1] = 1
                    area += 1
            
            answer.append(area)
            
print(len(answer))
answer.sort()

print(' '.join(list(map(str, answer))))