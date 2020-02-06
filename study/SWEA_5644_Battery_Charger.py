from copy import copy


d = {
    0: [0, 0],
    1: [-1, 0],
    2: [0, 1],
    3: [1, 0],
    4: [0, -1]
}


def assign_list(row, col, key):
    global board

    tmp = copy(board[row][col])
    tmp.append(key)
    if key not in board[row][col]:
        board[row][col] = tmp
    del tmp


def draw(one_battery):

    start_r, start_c = one_battery[1] - 1, one_battery[0] - 1
    range_num = one_battery[2]
    key = one_battery[4]

    for i in range(range_num + 1):
        row = start_r + i - range_num
        if 0 <= row:
            for j in range(i + 1):
                if 0 <= start_c - j:
                    assign_list(row, start_c - j, key)
                if start_c + j < 10:
                    assign_list(row, start_c + j, key)

    for i in range(range_num + 1):
        row = start_r - i + range_num
        if row < 10:
            for j in range(i + 1):
                if 0 <= start_c - j:
                    assign_list(row, start_c - j, key)
                if start_c + j < 10:
                    assign_list(row, start_c + j, key)


def check(r1, c1, r2, c2):
    global ANSWER
    global battery_dict

    tmp_answer = -1
    for v1 in board[r1][c1]:
        for v2 in board[r2][c2]:
            if v1 == v2:
                p1 = battery_dict[v1] // 2
                p2 = battery_dict[v2] // 2
            else:
                p1 = battery_dict[v1]
                p2 = battery_dict[v2]
            if tmp_answer < p1 + p2:
                tmp_answer = p1 + p2

    ANSWER += tmp_answer


tries = int(input())

for t in range(1, tries + 1):
    M, A = map(int, input().split())    # M: 이동 시간, A: 배터리 개수
    person1 = list(map(int, input().split()))
    person2 = list(map(int, input().split()))

    board = []
    for _ in range(10):
        board.append([[0]] * 10)

    battery = []    # [[col + 1, row + 1, range, power, key], ... ]
    battery_dict = {0: 0}
    for i in range(1, A + 1):
        tmp = list(map(int, input().split()))
        battery_dict[i] = tmp[3]    # power 넣기
        tmp.append(i)               # key 넣기
        battery.append(tmp)

    # 배터리를 board에 그리자
    for one_battery in battery:
        draw(one_battery)

    row_1, col_1 = 0, 0
    row_2, col_2 = 9, 9
    ANSWER = 0
    check(row_1, col_1, row_2, col_2)
    for p1, p2 in zip(person1, person2):
        row_1 = row_1 + d[p1][0]
        col_1 = col_1 + d[p1][1]
        row_2 = row_2 + d[p2][0]
        col_2 = col_2 + d[p2][1]
        check(row_1, col_1, row_2, col_2)

    print('#{} {}'.format(t, ANSWER))
