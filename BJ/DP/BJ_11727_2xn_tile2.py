import sys
sys.setrecursionlimit(2000)


d = [0] * (1000 + 1)

def dp(n):
    if n == 1: return 1
    if n == 2: return 3
    
    if d[n] != 0: return d[n]
    
    d[n] = (dp(n - 1) + 2 * dp(n - 2)) % 10007
    return d[n]


n = int(input())
result = dp(n)
print(result)