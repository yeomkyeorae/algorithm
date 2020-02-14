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


def calc(one_list):
    global person_list
    global stair_list
    global stair_value

    person_dist = deque()
    for ix, stair_ix in enumerate(one_list):
        person_dist.append([abs(person_list[ix][0] - stair_list[stair_ix][0]) + abs(person_list[ix][1] - stair_list[stair_ix][1]), stair_ix])
    stair_dict = {
        0: deque(),
        1: deque()
    }
    waitings = deque()
    answer = 0
    flag = False
    while len(waitings) or len(person_dist) or flag:
        for values in stair_dict.values():
            for _ in range(len(values)):
                p = values.popleft()
                p -= 1
                if p != 0:
                    values.append(p)

        for _ in range(len(waitings)):
            p = waitings.popleft()
            if len(stair_dict[p[1]]) < 3:
                stair_dict[p[1]].append(stair_value[p[1]])
            else:
                waitings.append(p)

        for _ in range(len(person_dist)):
            p = person_dist.popleft()
            if p[0] == 0:
                waitings.append(p)
            else:
                p[0] -= 1
                person_dist.append(p)

        for values in stair_dict.values():
            if len(values):
                flag = True
                break
            else:
                flag = False

        answer += 1

    return answer


def permutation(stage, one_list, length):
    global ANSWER

    if stage == length:
        answer = calc(one_list)
        if ANSWER > answer:
            ANSWER = answer
        return

    for i in range(2):
        one_list.append(i)
        permutation(stage + 1, one_list, length)
        one_list.pop()


tries = int(input())
for t in range(1, tries + 1):
    N = int(input())
    person_list = []    # [(row, col), (row, col), ... ]
    stair_list = []     # [(row, col), (row, col)]
    stair_value = []    # [3, 5]

    for row in range(N):
        tmp_list = list(map(int, input().split()))
        find(tmp_list, row)

    ANSWER = 1000
    permutation(0, [], len(person_list))
    print('#{} {}'.format(t, ANSWER - 1))
