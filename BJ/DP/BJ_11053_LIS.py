# Longest Increasing Subsooyeol
# 수열 중에서 가장 길게 증가하는 부분 순열 길이 찾기

n = int(input())
nums = list(map(int, input().split()))

d = [0] * n
for ix, num in enumerate(nums):
    d[ix] = 1
    max_index = -1
    max_value = 0
    for j in range(ix - 1, -1, -1):
        if nums[j] < nums[ix]:
            if d[j] > max_value:
                max_value = d[j]
                max_index = j
    d[ix] = d[ix] + max_value

print(max(d))
