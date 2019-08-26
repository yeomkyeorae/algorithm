tries = int(input())

for t in range(1, tries + 1):
    num = int(input())

    room_list = [0] * 200
    for i in range(num):
        n, m = map(int, input().split())
        if n < m:
            n, m = m, n

        for j in range((m - 1) // 2, (n - 1) // 2 + 1):
            room_list[j] += 1

    print('#{} {}'.format(t, max(room_list)))