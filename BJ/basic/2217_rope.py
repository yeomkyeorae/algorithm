import heapq


N = int(input())

ropes = []
for _ in range(N):
    rope = int(input())
    heapq.heappush(ropes, [-rope, rope])

answer = -1
num_rope = 1
while ropes:
    rope = heapq.heappop(ropes)[1]

    weight = rope * num_rope

    if weight > answer:
        answer = weight
    
    num_rope += 1

print(answer)