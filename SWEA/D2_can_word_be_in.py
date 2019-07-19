tries = int(input())

for i in range(1, tries + 1):
    n, k = map(int, input().split())
    board = []

    for _ in range(n):
        board.append(list(map(int, input().split())))

    # print(board)

    result = 0
    # board[row][col]
    for col in range(n):
        is_possible = 0
        for row in range(n):
            if board[row][col] == 1:
                is_possible += 1
            else:
                if is_possible == k:
                    result += 1
                is_possible = 0
        if is_possible == k:
            result += 1

    for row in range(n):
        is_possible = 0
        for col in range(n):
            if board[row][col] == 1:
                is_possible += 1
            else:
                if is_possible == k:
                    result += 1
                is_possible = 0
        if is_possible == k:
            result += 1

    print('#{} {}'.format(i, result))
