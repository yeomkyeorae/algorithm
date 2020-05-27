for t in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))

    answer = 0
    for i in range(2, N - 2):
        max_value = 0
        for c in range(-2, 3):
            if c == 0:
                continue
            if buildings[i + c] > max_value:
                max_value = buildings[i + c]
        if buildings[i] < max_value:
            continue
        answer += buildings[i] - max_value

    print('#{} {}'.format(t, answer))
