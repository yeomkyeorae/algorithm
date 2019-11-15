from collections import deque


directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
occupation = {}


def breed(candidate):
    survivals = {}
    for c in candidate:
        if (c[0], c[1]) in survivals.keys():
            if survivals[(c[0], c[1])] < c[2]:
                survivals[(c[0], c[1])] = c[2]
        else:
            survivals[(c[0], c[1])] = c[2]

    for k, v in survivals.items():
        deactivate.append([k[0], k[1], v, 0])


def to_activate():
    candidate = []
    for _ in range(len(deactivate)):
        popped = deactivate.popleft()
        popped[3] += 1
        if popped[2] == popped[3]:
            popped[3] = 0
            for direction in directions:
                if popped[0] + direction[0] in occupation.keys():
                    if not popped[1] + direction[1] in occupation[popped[0] + direction[0]]:
                        candidate.append([popped[0] + direction[0], popped[1] + direction[1], popped[2]])
            activate.append(popped)
        else:
            deactivate.append(popped)
    if candidate:
        breed(candidate)


def to_kill():
    for _ in range(len(activate)):
        popped = activate.popleft()
        popped[3] += 1
        if popped[2] == popped[3] - 1:
            if popped[0] in occupation.keys():
                occupation[popped[0]].append(popped[1])
            else:
                occupation[popped[0]] = [popped[1]]
        else:
            activate.append(popped)


tries = int(input())

for t in range(1, tries + 1):
    N, M, K = map(int, input().split())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))

    deactivate = deque()
    for row in range(N):
        for col in range(M):
            if board[row][col] > 0:
                if row in occupation.keys():
                    occupation[row].append(col)
                else:
                    occupation[row] = [col]
                deactivate.append([row, col, board[row][col], 0])

    time = 0
    activate = deque()
    # print(deactivate)
    while time != K:
        to_activate()
        # print(deactivate)
        to_kill()
        # print(activate)
        time += 1

    print('#{} {}'.format(t, len(deactivate) + len(activate)))
