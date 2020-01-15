def c_expand(total_list, max_size):
    global board

    for one_list in total_list:
        for _ in range(max_size - len(one_list)):
            one_list.append(0)
    board = []
    for col in range(len(total_list[0])):
        tmp_list = []
        for row in range(len(total_list)):
            tmp_list.append(total_list[row][col])
        board.append(tmp_list)


def r_expand(total_list, max_size):
    global board

    for one_list in total_list:
        for _ in range(max_size - len(one_list)):
            one_list.append(0)

    board = []
    for one_list in total_list:
        tmp_list = []
        for value in one_list:
            tmp_list.append(value)
        board.append(tmp_list)


def counter(one_list):
    one_dict = {}
    for v in one_list:
        if v == 0:
            continue
        if v in one_dict.keys():
            one_dict[v] += 1
        else:
            one_dict[v] = 1
    before_list = []
    for key, value in one_dict.items():
        before_list.append((key, value))
    return before_list


def sort_list(one_list):
    one_list.sort(key=lambda x: x[0])
    one_list.sort(key=lambda x: x[1])

    tmp_list = []
    for v in one_list:
        tmp_list.append(v[0])
        tmp_list.append(v[1])

    return tmp_list, len(tmp_list)


def c_operation():
    after_max_size = 0
    total_list = []
    for col in range(len(board[0])):
        tmp_list = []
        for row in range(len(board)):
            tmp_list.append(board[row][col])
        before_list = counter(tmp_list)
        after_list, size = sort_list(before_list)
        if size > after_max_size:
            after_max_size = size
        total_list.append(after_list)
    c_expand(total_list, after_max_size)


def r_operation():
    after_max_size = 0
    total_list = []
    for one_list in board:
        tmp_list = []
        for value in one_list:
            tmp_list.append(value)
        before_list = counter(tmp_list)
        after_list, size = sort_list(before_list)
        if size > after_max_size:
            after_max_size = size
        total_list.append(after_list)

    r_expand(total_list, after_max_size)


def size_check():
    global board
    row_size = len(board)
    col_size = len(board[0])

    if row_size >= col_size:
        return True
    else:
        return False


r, c, k = map(int, input().split())

board = []
for _ in range(3):
    board.append(list(map(int, input().split())))

answer = -1
for i in range(101):
    if len(board) > r - 1 and len(board[0]) > c - 1:
        if board[r - 1][c - 1] == k:
            flag = True
            answer = i
            break

    where_to_go = size_check()
    if where_to_go:
        r_operation()
    else:
        c_operation()

print(answer)
