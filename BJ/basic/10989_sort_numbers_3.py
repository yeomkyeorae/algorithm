import heapq
import sys
input = sys.stdin.readline

n = int(input())

num_set = set()
num_dict = dict()
for _ in range(n):
    num = int(input())
    num_set.add(num)
    
    if num in num_dict.keys():
        num_dict[num] += 1
    else:
        num_dict[num] = 1

heap = []    
for num in list(num_set):
    heapq.heappush(heap, num)
    
while heap:
    num = heapq.heappop(heap)
    for _ in range(num_dict[num]):
        print(num)

