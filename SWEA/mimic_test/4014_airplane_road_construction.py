def is_possible(one_list, max_size, size):
    criteria = 0
    passport = 0
    for ix, el in enumerate(one_list):
        if passport > 0:
            passport -= 1
            continue
        elif passport == 0:
            criteria = el
            continue

        if el == criteria:
            continue
        if abs(el - criteria) > 2:
            return False

        if criteria - el == 1:
            if ix + size >= max_size:
                return False
            for j in range(ix + 1, ix + size + 1):
                if el == one_list[j]:
                    continue
                else:
                    return False
            criteria = el
            passport = size
            continue

        if criteria - el == -1:
            if ix - size < 0:
                return False
            for j in range(ix - 1, ix - size - 1):
                if el == one_list[j]:
                    continue
                else:
                    return False
            criteria = el
            passport = size
            continue

    return True


tries = int(input())
for t in range(1, tries + 1):
    answer = 0
    N, X = map(int, input().split())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))

    for one_list in board:
        if is_possible(one_list, N, X):
            answer += 1

    for col in range(N):
        tmp_list = []
        for row in range(N):
            tmp_list.append(board[row][col])
        if is_possible(tmp_list, N, X):
            answer += 1

    print('#{} {}'.format(t, answer))
