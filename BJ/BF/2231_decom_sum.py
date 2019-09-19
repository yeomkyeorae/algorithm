n = int(input())
i = 0
for num in range(1, 10000000000):
    if '666' in str(num):
        i += 1
        if i == n:
            break
print(num)
