from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

board = []
for _ in range(N):
    row = input().split('\n')[0]
    board.append(row)
    
visited = []
for _ in range(N):
    visited.append([0] * N)

answer = []
for row in range(N):
    for col in range(N):
        if not visited[row][col] and int(board[row][col]):
            d = deque()
            d.append([row, col])
            
            part_answer = 0
            while d:
                r, c = d.popleft()
                visited[r][c] = 1
                part_answer += 1
            
                for add_row in [-1, 1]:
                    new_row = r + add_row
                    if 0 <= new_row < N and not visited[new_row][c] and int(board[new_row][c]):
                        visited[new_row][c] = 1
                        d.append([new_row, c])
                
                for add_col in [-1, 1]:
                    new_col = c + add_col
                    if 0 <= new_col < N and not visited[r][new_col] and int(board[r][new_col]):
                        visited[r][new_col] = 1
                        d.append([r, new_col])

            if part_answer:           
                answer.append(part_answer)
            
print(len(answer))
answer.sort()
for a in answer:
    print(a)