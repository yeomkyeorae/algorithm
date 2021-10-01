def get_value(n, q = 3):
    rev_base = ''

    while n > 0:
        tmp_n, mod = divmod(n, q)
        if n % q == 0:
            tmp_n -= 1
            mod = 3
        n = tmp_n
        rev_base += str(mod)

    return rev_base[::-1] 

def solution(n):
    answer = get_value(n)
    answer = answer.replace('3', '4')
    return answer