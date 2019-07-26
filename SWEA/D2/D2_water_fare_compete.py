tries = int(input())

for i in range(1, tries + 1):
    p, q, r, s, w = map(int, input().split())

    a_fare = p * w
    b_fare = q if w <= r else q + s * (w - r)

    best_fare = b_fare if a_fare >= b_fare else a_fare

    print('#{} {}'.format(i, best_fare))
