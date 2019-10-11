tries = int(input())

for t in range(1, tries + 1):
    n, m, l = map(int, input().split())
    V = [0] * (n + 1)
    for _ in range(m):
        ix, value = map(int, input().split())
        V[ix] = value

    visited = [0] * (n + 1)
    while V.count(0) != 1:
        for i in range(len(V) - 1, 0, -1):
            if not visited[i]:
                visited[i] = 1
                if i // 2 > 0:
                    if V[i // 2] == 0:
                        V[i // 2] = V[i]
                    else:
                        V[i // 2] = V[i] + V[i // 2]

    print('#{} {}'.format(t, V[l]))
