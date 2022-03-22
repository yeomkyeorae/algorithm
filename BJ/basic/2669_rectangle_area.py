board = []
for _ in range(101):
    board.append([0] * 101)

for _ in range(4):
    col1, row1, col2, row2 = map(int, input().split(' '))
    
    for row in range(row1, row2):
        for col in range(col1, col2):
            board[row][col] = 1
    
answer = 0        
for b in board:
    answer += b.count(1)

print(answer) 