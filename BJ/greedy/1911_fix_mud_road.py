import sys
input = sys.stdin.readline

N, L = map(int, input().split())

pools = []
for _ in range(N):
    start, end = map(int, input().split())
    pools.append([start, end])

pools.sort(key=lambda x:x[0])

answer = 0

started = False
location = 0
for pool in pools:
    start, end = pool
    
    if location <= start:
        location = start
        for _ in range(start, end, L):
            location += L
            answer += 1     
    else:
        for _ in range(location, end, L):
            location += L
            answer += 1       
            
print(answer)