import sys

input = sys.stdin.readline

N = int(input())

colors = []
for _ in range(N):
    color = list(map(int, input().split(' ')))
    colors.append(color)

dp = []
for i, color in enumerate(colors):
    if i == 0:
        dp.append(color)
        continue
    
    before_dp = dp[-1]
    current_dp = [sys.maxsize, sys.maxsize, sys.maxsize]
    for j, c in enumerate(color):
        for k in range(3):
            if j == k:
                continue
            
            if c + before_dp[k] < current_dp[j]:
                current_dp[j] = c + before_dp[k]
                
    dp.append(current_dp)

print(min(dp[-1]))