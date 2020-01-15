direction_map = [(1, 1), (1, -1), (-1, -1), (-1, 1)]


def check(row, col):
    if 0 <= row < N and 0 <= col < N:
        return True
    return False


def calc(vertex):
    global MIN_VALUE

    # 게리맨더링 보드 초기화
    gerry = []
    for _ in range(N):
        gerry.append([5] * N)

    # 1: 오른쪽 아래로
    r, c = vertex[0][0], vertex[0][1]
    while True:
        r += direction_map[0][0]
        c += direction_map[0][1]

        # 구역 표시
        for new_r in range(r - 1, -1, -1):
            gerry[new_r][c] = 2

        if [r, c] in vertex:  # 시작점 중의 하나이면 최후의 구획!
            while True:
                c = c + 1
                if c == N:
                    break
                for new_r in range(r, -1, -1):
                    gerry[new_r][c] = 2
            break

    # 2 왼쪽 아래로
    r, c = vertex[1][0], vertex[1][1]
    while True:
        r += direction_map[1][0]
        c += direction_map[1][1]

        for new_c in range(c + 1, N):
            gerry[r][new_c] = 4

        if [r, c] in vertex:
            while True:
                r = r + 1
                if r == N:
                    break
                for new_c in range(c, N):
                    gerry[r][new_c] = 4
            break

    # 3 왼쪽 위로
    r, c = vertex[2][0], vertex[2][1]
    while True:
        r += direction_map[2][0]
        c += direction_map[2][1]

        for new_r in range(r + 1, N):
            gerry[new_r][c] = 3

        if [r, c] in vertex:
            while True:
                c = c - 1
                if c == -1:
                    break
                for new_r in range(r, N):
                    gerry[new_r][c] = 3
            break

    # 4 오른쪽 위로
    r, c = vertex[3][0], vertex[3][1]
    while True:
        r += direction_map[3][0]
        c += direction_map[3][1]

        for new_c in range(c - 1, -1, -1):
            gerry[r][new_c] = 1

        if [r, c] in vertex:
            while True:
                r = r - 1
                if r == -1:
                    break
                for new_c in range(c, -1, -1):
                    gerry[r][new_c] = 1
            break

    # 각 구역별 점수 초기화
    num_dict = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0
    }
    # 점수 계산
    for r in range(N):
        for c in range(N):
            num_dict[gerry[r][c]] += board[r][c]
    tmp_list = []
    for v in num_dict.values():
        tmp_list.append(v)
    tmp_list.sort()
    tmp_value = tmp_list[-1] - tmp_list[0]
    if tmp_value < MIN_VALUE:
        MIN_VALUE = tmp_value


def go(row, col):
    for a in range(1, N):
        for b in range(1, N):
            for c in range(1, N):
                flag = True
                vertex = []
                for d in range(1, N):
                    if a != c or b != d:
                        continue
                    start_r, start_c = row, col

                    for i, v in enumerate([a, b, c, d]):
                        if flag:
                            vertex.append([start_r, start_c])
                            for _ in range(v):
                                start_r += direction_map[i][0]
                                start_c += direction_map[i][1]
                            flag = check(start_r, start_c)
                        else:
                            break

                    if flag:
                        calc(vertex)


N = int(input())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

MIN_VALUE = 100000000
for row in range(N):
    for col in range(N):
        go(row, col)

print(MIN_VALUE)
