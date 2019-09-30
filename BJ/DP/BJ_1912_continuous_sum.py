# d[i] 값에 (현재 값)과 (d[i - 1] + 현재 값) 중 큰 값을 대입(음수가 포함돼 있을 수도 있기 때문에)

n = int(input())
nums = list(map(int, input().split()))

d = [0] * n
for ix, num in enumerate(nums):
    if ix == 0:
        d[0] = num
        continue

    if num > num + d[ix - 1]:
        d[ix] = num
    else:
        d[ix] = num + d[ix - 1]

print(max(d))
