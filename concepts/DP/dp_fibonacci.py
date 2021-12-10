memo = [0] * 100

def dp(number):
    if number == 1: return 1
    if number == 2: return 1
    
    if memo[number] != 0: return memo[number]
    
    memo[number] = dp(number - 1) + dp(number - 2)
    return memo[number]

result = dp(10)
print(result)