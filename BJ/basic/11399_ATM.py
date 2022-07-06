_ = int(input())
nums = list(map(int, input().split()))

nums.sort()

answer = 0
current = 0
for num in nums:
    current = current + num
    answer += current

print(answer)
