d = [0] * (30 + 1)

def dp(n):
    if n == 0: return 1
    if n == 1: return 0
    if n == 2: return 3
    
    if d[n] != 0: return d[n]
    
    result = 3 * dp(n - 2)
    for i in range(3, n + 1):
        if i % 2 == 0:
           result += 2 * dp(n - i)
        
    d[n] = result
    
    return d[n]


n = int(input())
result = dp(n)

print(result)