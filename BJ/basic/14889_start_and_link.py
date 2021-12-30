from itertools import combinations
import sys


N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

answer = sys.maxsize
for comb in combinations(range(N), N // 2):
    others = []
    for el in range(N):
        if el not in comb:
            others.append(el)
    
    comb_score = 0
    for i in range(len(comb) - 1):
        for j in range(i + 1, len(comb)):
            comb_score += board[comb[i]][comb[j]] + board[comb[j]][comb[i]]
        
    other_score = 0
    for i in range(len(comb) - 1):
        for j in range(i + 1, len(comb)):
            other_score += board[others[i]][others[j]] + board[others[j]][others[i]]
            
    if abs(comb_score - other_score) < answer:
        answer = abs(comb_score - other_score)
    
print(answer)