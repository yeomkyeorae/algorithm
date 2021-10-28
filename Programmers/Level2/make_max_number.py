def solution(number, k):
    lst = list(map(lambda x: int(x), number))
    
    while k > 0:
        tmp = None
        flag = False
        for i, num in enumerate(lst):
            if k == 0:
                break
            if tmp is not None and tmp < num:
                lst.pop(i - 1)
                k -= 1
                flag = True
                break
            else:
                tmp = num

        if not flag:
            lst.pop()
            k -= 1

    return ''.join(str(n) for n in lst)