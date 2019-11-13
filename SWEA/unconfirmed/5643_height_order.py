from collections import deque


def bfs(start, paths):
    global visited

    local_visited = [0] * n
    d = deque()
    d.append(start)
    local_visited[start - 1] = 1
    while d:
        popped = d.popleft()
        if popped in paths.keys():
            for p in paths[popped]:
                if not local_visited[p - 1]:
                    d.append(p)
                    local_visited[p - 1] = 1

    for ix, v in enumerate(local_visited):
        if v == 1:
            visited[ix] = 1


tries = int(input())

for t in range(1, tries + 1):
    n = int(input())
    m = int(input())

    forward = {}
    backward = {}
    for _ in range(m):
        start, end = map(int, input().split())
        if start in forward.keys():
            forward[start].append(end)
        else:
            forward[start] = [end]

        if end in backward.keys():
            backward[end].append(start)
        else:
            backward[end] = [start]

    students = list(range(1, n + 1))
    cnt = 0
    for student in students:
        visited = [0] * n
        bfs(student, forward)
        bfs(student, backward)
        if visited.count(1) == len(visited):
            cnt += 1

    print('#{} {}'.format(t, cnt))
