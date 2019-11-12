def find_max(one_list):
    max_value = -1
    max_dict = dict()
    for row in range(len(one_list)):
        for col in range(len(one_list)):
            if one_list[row][col] >= max_value:
                max_value = one_list[row][col]
                if max_value in max_dict.keys():
                    max_dict[max_value].append((row, col))
                else:
                    max_dict[max_value] = [(row, col)]

    return max_dict[max_value]


def go(row, col, cur, dist):
    global longest_path
    global n

    if board[row][col] >= cur:
        return

    if dist > longest_path:
        if visited[global_row][global_col]:
            longest_path = dist

    # 아래
    if row + 1 <= n - 1:
        if not visited[row + 1][col]:
            visited[row + 1][col] = 1
            go(row + 1, col, board[row][col], dist + 1)
            visited[row + 1][col] = 0
    # 위
    if 0 <= row - 1:
        if not visited[row - 1][col]:
            visited[row - 1][col] = 1
            go(row - 1, col, board[row][col], dist + 1)
            visited[row - 1][col] = 0
    # 좌
    if 0 <= col - 1:
        if not visited[row][col - 1]:
            visited[row][col - 1] = 1
            go(row, col - 1, board[row][col], dist + 1)
            visited[row][col - 1] = 0
    # 우
    if col + 1 <= n - 1:
        if not visited[row][col + 1]:
            visited[row][col + 1] = 1
            go(row, col + 1, board[row][col], dist + 1)
            visited[row][col + 1] = 0


tries = int(input())
for t in range(1, tries + 1):
    n, k = map(int, input().split())
    board = []
    visited = []
    for _ in range(n):
        board.append(list(map(int, input().split())))
        visited.append([0] * n)
    longest_path = -1
    for row in range(n):
        for col in range(n):
            tmp = board[row][col]
            for new_k in range(k + 1):
                global_row = row
                global_col = col
                board[row][col] = tmp - new_k
                max_list = find_max(board)
                for value in max_list:
                    visited[value[0]][value[1]] = 1
                    go(value[0], value[1], 10000, 1)
                    visited[value[0]][value[1]] = 0
                board[row][col] = tmp

    print('#{} {}'.format(t, longest_path))
