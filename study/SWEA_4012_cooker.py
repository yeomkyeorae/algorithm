def perm(num, stage, ix_list):
    global answer
    global N

    if stage == N // 2:
        a_list, b_list = [], []
        for a in ix_list:
            a_list.append(a)
        for i, v in enumerate(visited):
            if v == 0:
                b_list.append(i)

        a, b = 0, 0
        for i in range((N // 2) - 1):
            for j in range(i + 1, N // 2):
                a += board[a_list[i]][a_list[j]] + board[a_list[j]][a_list[i]]
                b += board[b_list[i]][b_list[j]] + board[b_list[j]][b_list[i]]
        tmp = abs(a - b)
        if answer > tmp:
            answer = tmp
        return

    for i in range(num + 1, N):
        if not visited[i]:
            visited[i] = 1
            perm(i, stage + 1, ix_list + [i])
            visited[i] = 0


tries = int(input())
for t in range(1, tries + 1):
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))

    visited = [0] * N
    answer = 0xFFFFFF
    for num in range(N // 2):
        visited[num] = 1
        perm(num, 1, [num])
        visited[num] = 0
    print('#{} {}'.format(t, answer))

