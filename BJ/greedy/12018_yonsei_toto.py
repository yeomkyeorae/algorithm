import sys
import heapq
input = sys.stdin.readline

n, mileage = map(int, input().split())

min_mileages = []
for _ in range(n):
    student_num, num_limit = map(int, input().split())
    
    scores = list(map(int, input().split()))
    scores.sort(reverse=True)
    
    is_full = False
    for i, s in enumerate(scores):
        num_limit -= 1
        
        if num_limit == 0:
            heapq.heappush(min_mileages, s)
            is_full = True
            break
        
    if not is_full:
        heapq.heappush(min_mileages, 1)
    
answer = 0
while min_mileages:
    need_mileage = heapq.heappop(min_mileages)
    
    if mileage - need_mileage >= 0:
        mileage -= need_mileage
        answer += 1
    else:
        break
    
print(answer)