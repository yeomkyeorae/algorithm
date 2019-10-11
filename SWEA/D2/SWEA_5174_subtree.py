def inorder(v):

    global cnt

    if v == 0:
        return

    cnt += 1

    inorder(L[v])
    inorder(R[v])


tries = int(input())

for t in range(1, tries + 1):
    E, N = map(int, input().split())
    V = E + 1
    L = [0] * (V + 1)
    R = [0] * (V + 1)
    P = [0] * (V + 1)

    arr = list(map(int, input().split()))

    for i in range(0, E * 2, 2):
        p, c = arr[i], arr[i + 1]
        if L[arr[i]] == 0:
            L[p] = c
        else:
            R[p] = c
        P[p] = c

    cnt = 0
    inorder(N)

    print('#{} {}'.format(t, cnt))
