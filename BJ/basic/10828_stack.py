import sys
input = sys.stdin.readline


n = int(input())

stack = []
for _ in range(n):
    com_list = list(input().split())
    
    command = com_list[0]
    
    if command == 'push':
        value = com_list[1]
        stack.append(value)
    elif command == 'top':
        if not len(stack):
            print(-1)
        else:
            print(stack[-1])
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        if not len(stack):
            print(1)
        else:
            print(0)
    elif command == 'pop':
        if not len(stack):
            print(-1)
        else:
            print(stack.pop())
