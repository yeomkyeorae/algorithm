import sys
import heapq

input = sys.stdin.readline
N = int(input())

heap = []
for _ in range(N):
    n = int(input())
    
    if n == 0:
        if not len(heap):
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, n)

