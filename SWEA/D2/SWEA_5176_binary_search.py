def go(n):

    if n > N:
        return

    go(n * 2)
    visit_order.append(n)
    go(n * 2 + 1)


tries = int(input())

for t in range(1, tries + 1):
    N = int(input())
    V = [0] * (N + 1)

    visit_order = []
    go(1)
    value = 1
    tree = [0] * (N + 1)
    for i in visit_order:
        tree[i] = value
        value += 1
    print('#{} {} {}'.format(t, tree[1], tree[N // 2]))
