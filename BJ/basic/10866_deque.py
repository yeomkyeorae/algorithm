from collections import deque
import sys
input = sys.stdin.readline

d = deque()

n = int(input())

for _ in range(n):
    inputs = input().split()
    command = inputs[0]
    
    if command == 'push_front':
        d.appendleft(inputs[1])
    elif command == 'push_back':
        d.append(inputs[1])
    elif command == 'pop_front':
        if not len(d):
            print(-1)
        else:
            print(d.popleft())
    elif command == 'pop_back':
        if not len(d):
            print(-1)
        else:
            print(d.pop())
    elif command == 'size':
        print(len(d))
    elif command == 'empty':
        if not len(d):
            print(1)
        else:
            print(0)
    elif command == 'front':
        if not len(d):
            print(-1)
        else:
            print(d[0])
    elif command == 'back':
        if not len(d):
            print(-1)
        else:
            print(d[-1])
    