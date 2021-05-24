from functools import cmp_to_key


def compare_func(a, b):
    value1, value2 = a + b, b + a
    if value1 > value2:
        return 1
    elif value1 < value2:
        return -1
    else:
        return 0


def solution(numbers):
    n = [str(num) for num in numbers]
    n = sorted(n, key=cmp_to_key(compare_func), reverse=True)
    answer = str(int(''.join(n)))

    return answer
