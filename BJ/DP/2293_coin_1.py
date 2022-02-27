import sys
input = sys.stdin.readline

N, K = list(map(int, input().split(' ')))

coins = []
for _ in range(N):
    coin = int(input())
    coins.append(coin)

dp = [0] * (K + 1)
dp[0] = 1
for coin in coins:
    for j in range(1, K + 1):
        if j - coin >= 0:
            dp[j] += dp[j - coin]
        
print(dp[K])