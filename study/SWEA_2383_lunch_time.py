from collections import deque


def find(input_list, row):
    global stair_list
    global person_list
    global stair_value

    for col, value in enumerate(input_list):
        if value == 1:
            person_list.append([row, col])
        elif value > 1:
            stair_list.append([row, col])
            stair_value.append(value)


def nearest(person_list, stair_list):
    global stair_value

    where_to_stair = deque()
    tmp_list = []
    for p in person_list:
        dist = 1000
        candidate_ix = -10
        for s_ix, s in enumerate(stair_list):
            tmp_dist = abs(p[0] - s[0]) + abs(p[1] - s[1])
            if tmp_dist < dist:
                dist = tmp_dist
                candidate_ix = s_ix
            elif tmp_dist == dist:
                if stair_value[candidate_ix] > stair_value[s_ix]:
                    candidate_ix = s_ix
        tmp_list.append(candidate_ix)
        where_to_stair.append([candidate_ix, dist])

    return where_to_stair


def move(where_to_stair):
    global stair_list
    global stair_value
    global person_list

    ANSWER = 0
    arrived = []
    waitings = deque()
    ing_dict = {}
    for i in range(len(stair_value)):
        ing_dict[i] = deque()
    while len(arrived) < len(person_list):
        for one_d in ing_dict.values():
            for _ in range(len(one_d)):
                popped = one_d.popleft()
                popped -= 1
                if popped == 0:
                    arrived.append(True)
                else:
                    one_d.append(popped)

        for i in range(len(where_to_stair)):
            popped = where_to_stair.popleft()
            if popped[1] == 0:
                waitings.append(popped[0])
            else:
                popped[1] -= 1
                where_to_stair.append(popped)

        for _ in range(len(waitings)):
            popped = waitings.popleft()
            if len(ing_dict[popped]) < 3:
                ing_dict[popped].append(stair_value[popped])
            else:
                waitings.append(popped)

        if len(arrived) != len(person_list):
            ANSWER += 1
    return ANSWER


tries = int(input())

for t in range(1, tries + 1):
    N = int(input())
    person_list = []
    stair_list = []
    stair_value = []

    board = []
    for row in range(N):
        tmp_list = list(map(int, input().split()))
        find(tmp_list, row)
        board.append(tmp_list)
    where_to_stair = nearest(person_list, stair_list)
    ANSWER = move(where_to_stair)
    print('#{} {}'.format(t, ANSWER + 1))