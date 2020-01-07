from collections import deque


def rotate(deq, d, k):
    # d: 0 -> 시계 방향
    # d: 1 -> 반시계 방향
    for _ in range(k):
        if d == 0:
            deq.appendleft(deq.pop())
        elif d == 1:
            deq.append(deq.popleft())


def delete(deq_list):
    global n, m

    board = []
    for _ in range(n):
        board.append([0] * m)

    # 같은 덱에서의 같은 값 표시
    for i, deq in enumerate(deq_list):
        for j in range(len(deq)):
            if deq[j] == 0:
                continue
            if j == len(deq) - 1:
                if deq[0] == deq[j]:
                    board[i][0] = 1
                    board[i][j] = 1
                break

            if deq[j] == deq[j + 1]:
                board[i][j] = 1
                board[i][j + 1] = 1

    # 다른 덱에서의 같은 값 표시
    for i in range(m):
        for j in range(n - 1):
            if deq_list[j][i] == 0:
                continue
            if deq_list[j][i] == deq_list[j + 1][i]:
                board[j][i] = 1
                board[j + 1][i] = 1

    # 값 없애 주기
    flag = True
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                flag = False
                deq_list[i][j] = 0

    return flag


def control(deq_list):
    not_zero_cnt = 0
    sum_value = 0
    for deq in deq_list:
        for v in deq:
            if v != 0:
                not_zero_cnt += 1
                sum_value += v

    if not_zero_cnt != 0:
        mean = sum_value / not_zero_cnt
    else:
        mean = 0
    for deq in deq_list:
        for j, v in enumerate(deq):
            if v != 0:
                if v > mean:
                    deq[j] -= 1
                elif v < mean:
                    deq[j] += 1


def sum_deq(deq_list):
    sum_value = 0
    for deq in deq_list:
        sum_value += sum(deq)

    return sum_value


n, m, t = map(int, input().split())

rotate_list = []
for _ in range(n):
    rotate_list.append(deque(map(int, input().split())))


for _ in range(t):
    # x: 배수
    # d: 방향
    # k: 이동 칸수
    x, d, k = map(int, input().split())
    for ix in range(x, len(rotate_list) + 1, x):
        rotate(rotate_list[ix - 1], d, k)

    flag = delete(rotate_list)
    if flag:
        control(rotate_list)

print(sum_deq(rotate_list))
