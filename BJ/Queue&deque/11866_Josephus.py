from collections import deque


n, k = map(int, input().split())
q = deque(range(1, n + 1))

order = []
while q:
    for _ in range(k - 1):
        q.append(q.popleft())
    order.append(str(q.popleft()))

answer = '<'
answer += ', '.join(order)
answer += '>'
print(answer)
