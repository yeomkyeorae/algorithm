# unresolved version

# def solution(number, k):
#     lst = list(map(lambda x: int(x), number))
    
#     while k > 0:
#         tmp = None
#         flag = False
#         for i, num in enumerate(lst):
#             if k == 0:
#                 break
#             if tmp is not None and tmp < num:
#                 lst.pop(i - 1)
#                 k -= 1
#                 flag = True
#                 break
#             else:
#                 tmp = num

#         if not flag:
#             lst.pop()
#             k -= 1

#     return ''.join(str(n) for n in lst)

def solution(number, k):
    new_lst = []
    lst = list(map(lambda x: int(x), number))

    for num in lst:         
        if not new_lst:
            new_lst.append(num)
            continue

        while new_lst:
            if k == 0:
                break
            tmp = new_lst.pop()
            if tmp < num:            
                k -= 1          
            else:
                new_lst.append(tmp)
                break
        new_lst.append(num)
    
    if k:
        for _ in range(k):
            new_lst.pop()

    return ''.join(str(n) for n in new_lst)