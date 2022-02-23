N = int(input())

arr = []
dp = []
for _ in range(N):
    el = list(map(int, input().split(' ')))
    arr.append(el)
    dp.append([0] * len(el))
    
dp[0] = [arr[0][0]]
for i in range(1, len(arr)):
    el = arr[i]
    for j in range(len(el)):
        if j == 0:
            dp[i][j] = dp[i - 1][j] + arr[i][j]
        elif j == len(el) - 1:
            dp[i][j] = dp[i - 1][j - 1] + arr[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + arr[i][j]
            
print(max(dp[-1]))