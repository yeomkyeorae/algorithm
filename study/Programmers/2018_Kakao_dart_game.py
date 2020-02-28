def solution(dartResult):
    ix = 0
    n_list = [0] * 3
    option_list = [0] * 3
    for i, ch in enumerate(dartResult):
        try:
            if i != 0:
                if ch == '0':
                    if dartResult[i - 1] == '1':
                        num = 10
                        continue
            num = int(ch)
        except:
            if ch == 'S':
                n_list[ix] = num
            elif ch == 'D':
                num = num ** 2
                n_list[ix] = num
            elif ch == 'T':
                num = num ** 3
                n_list[ix] = num
            elif ch == '*':
                option_list[ix - 1] = '*'
                continue
            elif ch == '#':
                option_list[ix - 1] = '#'
                continue
            ix += 1
    for ix, option in enumerate(option_list[::-1]):
        if option == 0:
            continue
        if option == '*':
            n_list[2 - ix] = n_list[2 - ix] * 2
            if 1 - ix >= 0:
                n_list[1 - ix] = n_list[1 - ix] * 2
        if option == '#':
            n_list[2 - ix] = n_list[2 - ix] * (-1)

    answer = sum(n_list)
    return answer