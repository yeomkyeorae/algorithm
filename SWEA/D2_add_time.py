tries = int(input())
for i in range(1, tries + 1):
    h1, m1, h2, m2 = map(int, input().split())

    new_m = m1 + m2
    new_h = h1 + h2

    if new_m >= 60:
        new_h += 1
        new_m -= 60
    if new_h > 12:
        new_h -= 12

    print('#{} {} {}'.format(i, new_h, new_m))
