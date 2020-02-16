from collections import deque


tries = int(input())

for t in range(1, tries + 1):
    N, K = map(int, input().split())

    tmp = input()
    d = deque()
    for v in tmp:
        d.append(v)

    delimeter = N // 4
    num_set = set()
    for _ in range(N):
        for i in range(0, N, delimeter):
            a = ''.join(list(d)[i:i+delimeter])
            b = int(a, 16)
            num_set.add(b)
        d.append(d.popleft())

    final_list = list(num_set)
    final_list.sort(reverse=True)

    print('#{} {}'.format(t, final_list[K - 1]))
