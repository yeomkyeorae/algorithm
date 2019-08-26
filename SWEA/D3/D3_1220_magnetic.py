for t in range(1, 11):
    size = int(input())

    board = []
    for _ in range(size):
        tmp_list = list(map(int, input().split()))
        board.append(tmp_list)

    result = 0
    for col in range(size):
        stack = []
        for row in range(size):
            if board[row][col] != 0:
                stack.append(board[row][col])

        flag = False
        for _ in range(len(stack)):
            tmp = stack.pop()
            if tmp == 2:
                flag = True
            if flag and tmp == 1:
                result += 1
                flag = False

    print('#{} {}'.format(t, result))
