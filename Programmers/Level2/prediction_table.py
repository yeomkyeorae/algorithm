import math


def solution(n,a,b):
    answer = 1

    if a > b:
        a, b = b, a
    
    if b - a == 1 and a % 2 and not b % 2:
        return answer
    
    while n > 1:
        answer += 1
        
        if a != 1:
            a = math.ceil(a / 2)
        if b != 2:
            b = math.ceil(b / 2)
        
        if b - a == 1 and a % 2 and not b % 2:
            break
        
        n //= 2
    
    return answer