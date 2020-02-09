def go_max(num, stage):
    global flag

    if flag:
        return

    if stage > 1:
        boo = boo_list[stage - 2]
        before_num = ANSWER[stage - 2]
        if boo == '<':
            if before_num > num:
                return
        elif boo == '>':
            if before_num < num:
                return

    if N + 1 == stage:
        for v in ANSWER:
            print(v, end="")
        flag = True
        return

    for i in range(9, -1, -1):
        if not visited[i]:
            visited[i] = 1
            ANSWER[stage] = i
            go_max(i, stage + 1)
            visited[i] = 0
            ANSWER[stage] = -1


def go_min(num, stage):
    global flag

    if flag:
        return

    if stage > 1:
        boo = boo_list[stage - 2]
        before_num = ANSWER[stage - 2]
        if boo == '<':
            if before_num > num:
                return
        elif boo == '>':
            if before_num < num:
                return

    if N + 1 == stage:
        for v in ANSWER:
            print(v, end="")
        flag = True
        return

    for i in range(10):
        if not visited[i]:
            visited[i] = 1
            ANSWER[stage] = i
            go_min(i, stage + 1)
            visited[i] = 0
            ANSWER[stage] = -1


N = int(input())

boo_list = list(input().split())

ANSWER = [-1] * (N + 1)
visited = [0] * 10
flag = False
go_max(0, 0)
print()
ANSWER = [-1] * (N + 1)
visited = [0] * 10
flag = False
go_min(0, 0)
