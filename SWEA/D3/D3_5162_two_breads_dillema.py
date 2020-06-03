tries = int(input())

for t in range(1, tries + 1):
    A, B, C = map(int, input().split())

    if A >= B:
        price = B
        print('#{} {}'.format(t, int(C / B)))
    else:
        price = A
        print('#{} {}'.format(t, int(C / A)))
