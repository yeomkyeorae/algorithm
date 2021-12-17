import heapq


n = int(input())

left = []
right = []
answer = []
for _ in range(n):
    num = int(input())
    
    if len(left) == len(right):
        heapq.heappush(left, (-num, num))
    else:
        heapq.heappush(right, num)
    
    if right and left[0][1] > right[0]:
        min_value = heapq.heappop(right)
        max_value = heapq.heappop(left)[1]
        heapq.heappush(left, (-min_value, min_value))
        heapq.heappush(right, max_value)
        
    answer.append(left[0][1])
    
for v in answer:
    print(v)
    