num = int(input())

d = [0] * 10000000
d[1] = 0
for i in range(2, num + 1):
    d[i] = d[i - 1] + 1
    if i % 2 == 0 and d[i] > d[i // 2] + 1:
        d[i] = d[i // 2] + 1
    if i % 3 == 0 and d[i] > d[i // 3] + 1:
        d[i] = d[i // 3] + 1

print(d[num])
