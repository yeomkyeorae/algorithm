import sys

N = int(input())

nums = list(map(int, input().split(' ')))
nums.sort()

answer = sys.maxsize
for i in range(0, len(nums) // 2):
    summation = nums[i] + nums[len(nums) - 1 - i]
    if summation < answer:
        answer = summation
        
print(answer) 