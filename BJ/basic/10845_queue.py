import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

q = deque()
for _ in range(n):
    inputs = list(input().split())
    command = inputs[0]
    
    if command == 'push':
        q.append(inputs[1])
    elif command == 'pop':
        if not len(q):
            print(-1)
        else:
            print(q.popleft())
    elif command == 'size':
        print(len(q))
    elif command == 'empty':
        if not len(q):
            print(1)
        else:
            print(0)
    elif command == 'front':
        if not len(q):
            print(-1)
        else:
            print(q[0])
    elif command == 'back':
        if not len(q):
            print(-1)
        else:
            print(q[-1])
