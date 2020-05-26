tries = int(input())

for t in range(1, tries + 1):
    N = int(input())

    board = list(map(int, input().split()))
    answer = 0
    for ix, el in enumerate(board[::-1]):
        if ix == 0:
            tmp_max = el
            continue

        if el < tmp_max:
            answer += tmp_max - el
        else:
            tmp_max = el

    print('#{} {}'.format(t, answer))
