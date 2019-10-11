def push(item):
    global top
    global last_value

    top += 1
    H[top] = item
    c, p = top, top // 2
    flag = True
    while p:
        if H[p] > H[c]:
            H[p], H[c] = H[c], H[p]
            if flag:
                last_value = H[c]
                flag = False
            c = p
            p = c // 2
        else:
            break


tries = int(input())

for t in range(1, tries + 1):
    n = int(input())
    arr = list(map(int, input().split()))

    H = [0] * (n + 1)
    top = 0
    last_value = -1
    for a in arr:
        last_value = a
        push(a)

    result = 0
    last_ix = H.index(last_value)
    while last_ix != 1:
        last_ix = last_ix // 2
        result += H[last_ix]

    print('#{} {}'.format(t, result))
