from itertools import combinations
from collections import deque


def consume(wait_q_1, wait_q_2):
    global answer
    calc = 1
    d1 = deque()
    d2 = deque()
    while wait_q_1 or wait_q_2 or d1 or d2:
        calc += 1

        pop_cnt = 0
        for i in range(len(d1)):
            if d1[i] > 0:
                d1[i] -= 1
            if d1[i] == 0:
                pop_cnt += 1
        for _ in range(pop_cnt):
            d1.popleft()

        pop_cnt = 0
        for i in range(len(d2)):
            if d2[i] > 0:
                d2[i] -= 1
            if d2[i] == 0:
                pop_cnt += 1
        for _ in range(pop_cnt):
            d2.popleft()

        p1 = 0
        len_1 = len(d1)
        for i in range(len(wait_q_1)):
            if wait_q_1[i] > 0:
                wait_q_1[i] -= 1
            if wait_q_1[i] == 0:
                if len_1 < 3:
                    p1 += 1
                    len_1 += 1
        for _ in range(p1):
            wait_q_1.popleft()
            d1.append(stair_1)

        p2 = 0
        len_2 = len(d2)
        for i in range(len(wait_q_2)):
            if wait_q_2[i] > 0:
                wait_q_2[i] -= 1
            if wait_q_2[i] == 0:
                if len_2 < 3:
                    p2 += 1
                    len_2 += 1
        for _ in range(p2):
            wait_q_2.popleft()
            d2.append(stair_2)

    if calc < answer:
        answer = calc


tries = int(input())

for t in range(1, tries + 1):
    n = int(input())
    board = []
    peoples = []
    stairs = []
    stair_1 = 0
    stair_2 = 0
    for _ in range(n):
        board.append(list(map(int, input().split())))

    for row in range(n):
        for col in range(n):
            if board[row][col] == 1:
                peoples.append((row, col))
            elif board[row][col] > 1:
                stairs.append((row, col))
                if stair_1 == 0:
                    stair_1 = board[row][col]
                else:
                    stair_2 = board[row][col]

    # stair별 거리 구해서 dict에 저장
    dist_dict = {}
    for ix, people in enumerate(peoples):
        dist_dict[ix + 1] = [abs(stairs[0][0] - people[0]) + abs(stairs[0][1] - people[1]),
                         abs(stairs[1][0] - people[0]) + abs(stairs[1][1] - people[1])]

    # 조합 구하면서 시간 구하기
    peoples_key = list(range(1, len(peoples) + 1))
    answer = 10000
    for n in range(len(peoples) + 1):
        for combies in combinations(peoples_key, n):    # 조합 반복문
            # 1번 계단으로 가는 놈들
            wait_q_1 = deque()
            tmp_list = []
            for combi in combies:
                tmp_list.append(dist_dict[combi][0])
            tmp_list.sort()
            for el in tmp_list:
                wait_q_1.append(el)

            # 2번 계단으로 가는 놈들
            wait_q_2 = deque()
            tmp_list = []
            for p in peoples_key:
                if p not in combies:
                    tmp_list.append(dist_dict[p][1])
            tmp_list.sort()
            for el in tmp_list:
                wait_q_2.append(el)

            consume(wait_q_1, wait_q_2)

    print('#{} {}'.format(t, answer))
