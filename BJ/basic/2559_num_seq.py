from collections import deque
import sys

N, K = list(map(int, input().split(' ')))
nums = list(map(int, input().split(' ')))

d = deque()
max_value = -sys.maxsize
tmp = 0
for i, n in enumerate(nums):
    d.append(n)
    
    tmp += n
    
    if len(d) > K:
        delete_value = d.popleft()
        tmp -= delete_value
    
    if i >= K - 1:
        if tmp > max_value:
            max_value = tmp
        
print(max_value)