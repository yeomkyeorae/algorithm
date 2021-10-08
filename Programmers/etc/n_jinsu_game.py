import string


tmp = string.digits + string.ascii_uppercase
def convert(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]


def solution(n, t, m, p):
    answer = ''
    total = ''
    start = 0
    flag = True
    while flag:
        total += convert(start, n)
        start += 1
        if len(total[(p-1)::m]) >= t:
            flag = False
    
    for el in total[(p-1)::m]:
        answer += el
        if len(answer) == t:
            break
                
    return answer