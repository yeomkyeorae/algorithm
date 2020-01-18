from collections import deque


direction_dict = {
    0: [0, 1],  # 오른쪽
    1: [1, 0],  # 아래
    2: [0, -1],  # 왼쪽
    3: [-1, 0]  # 위
}


def index_checker(ix, thresh):
    if ix < 0:
        ix = thresh - 1
    elif ix == thresh:
        ix = 0

    return ix


def bfs(row, col, memory, direction):
    d = deque()
    d.append([row, col, memory, direction])
    visited = [[row, col, memory, direction]]
    i = 0
    while d:
        # print(d)
        popped = d.popleft()
        row, col, memory, direction = popped[0], popped[1], popped[2], popped[3]
        value = board[row][col]
        q_flag = False

        if value == '@':
            return True
        elif value == '>':
            direction = 0
        elif value == 'v':
            direction = 1
        elif value == '<':
            direction = 2
        elif value == '^':
            direction = 3
        elif value == '_':
            if memory == 0:
                direction = 0
            else:
                direction = 2
        elif value == '|':
            if memory == 0:
                direction = 1
            else:
                direction = 3
        elif value == '?':
            q_flag = True
        elif value == '+':
            if memory == 15:
                memory = 0
            else:
                memory += 1
        elif value == '-':
            if memory == 0:
                memory = 15
            else:
                memory -= 1
        elif value == '.':
            pass
        else:
            memory = int(value)

        if q_flag:
            for k in range(4):
                new_row = index_checker(row + direction_dict[k][0], r)
                new_col = index_checker(col + direction_dict[k][1], c)
                if [new_row, new_col, memory, k] not in visited:
                    d.append([new_row, new_col, memory, k])
                    visited.append([new_row, new_col, memory, k])
        else:
            row = index_checker(row + direction_dict[direction][0], r)
            col = index_checker(col + direction_dict[direction][1], c)
            if [row, col, memory, direction] not in visited:
                d.append([row, col, memory, direction])
                visited.append([row, col, memory, direction])
        i += 1
        if i == 1000:
            return False
    return False


tries = int(input())

for t in range(1, tries + 1):
    r, c = map(int, input().split())

    board = []
    flag = False
    for _ in range(r):
        tmp_list = []
        for v in input():
            if v == '@':
                flag = True
            tmp_list.append(v)
        board.append(tmp_list)

    if not flag:
        print('#{} {}'.format(t, 'NO'))
        continue

    end_flag = bfs(0, 0, 0, 0)
    if end_flag:
        print('#{} {}'.format(t, 'YES'))
    else:
        print('#{} {}'.format(t, 'NO'))
