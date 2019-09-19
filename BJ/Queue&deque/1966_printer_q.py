from collections import deque


tries = int(input())

for t in range(1, tries + 1):
    n, m = map(int, input().split())
    q = deque((i, j) for i, j in enumerate(list(map(int, input().split()))))

    order = []
    while q:
        popped = q.popleft()
        flag = True
        for a in q:
            if popped[1] < a[1]:
                q.append(popped)
                flag = False
                break
        if flag:
            order.append(popped)
    for a in order:
        if a[0] == m:
            print(order.index(a) + 1)
            break
