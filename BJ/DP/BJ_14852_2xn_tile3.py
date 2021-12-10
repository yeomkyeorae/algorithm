import sys
sys.setrecursionlimit(10000000)

d = []
for _ in range(1000000 + 1):
    d.append([0, 0])

def dp(n):
    d[0][0] = 0
    d[1][0] = 2
    d[2][0] = 7
    d[2][1] = 1
    
    divider = 1000000007
        
    for i in range(3, n + 1):
        d[i][1] = (d[i - 1][1] + d[i - 3][0]) % divider
        d[i][0] = (3 * d[i - 2][0] + 2 * d[i - 1][0] + 2 * d[i][1]) % divider
    
    return d[n][0]


n = int(input())
result = dp(n)

print(result)