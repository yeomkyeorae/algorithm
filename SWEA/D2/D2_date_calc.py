tries = int(input())

days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(1, tries + 1):
    dates = list(map(int, input().split()))

    if dates[0] == dates[2]:
        print('#{} {}'.format(i, dates[3] - dates[1] + 1))
        continue

    result = 0
    result += days[dates[0]] - dates[1]
    result += dates[3]

    for month in range(dates[0] + 1, dates[2]):
        result += days[month]

    print('#{} {}'.format(i, result + 1))
