n = int(input())

for _ in range(n):
    a, b = map(int, input().split())

    remainder = []
    i = 1
    while True:
        last_num = int(str(a ** i)[-1])
        if last_num in remainder:
            break

        remainder.append(last_num)
        i += 1

    i = b % len(remainder) - 1

    answer = remainder[i]
    if answer == 0:
        print(10)
    else:
        print(answer)
