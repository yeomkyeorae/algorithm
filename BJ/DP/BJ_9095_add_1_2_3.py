tries = int(input())

for t in range(1, tries + 1):
    n = int(input())
    d = [0] * 20
    d[0] = 1
    d[1] = 1
    d[2] = 2
    d[3] = 4

    if n > 3:
        for i in range(4, n + 1):
            d[i] = d[i - 1] + d[i - 2] + d[i - 3]

    print(d[n])
