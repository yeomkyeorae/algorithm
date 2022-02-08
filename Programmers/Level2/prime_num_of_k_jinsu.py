import string

tmp = string.digits + string.ascii_uppercase
def convert(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]

    
def is_prime(n):
    if n == 1:
        return False
    
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
    

def solution(n, k):
    converted = str(convert(n, k))
    
    answer = 0
    for string in converted.split("0"):
        if len(string):
            num = int(string)
            if is_prime(num):
                answer += 1
            
    return answer