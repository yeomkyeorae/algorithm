from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    commands = input()
    num = int(input())
    tmp = input()
    tmp = tmp.replace('[', '')
    tmp = tmp.replace(']', '')
    arr = deque()
    
    done = False
    for el in tmp.split(','):
        if el == '':
            print('error')
            done = True
            break
        elif el != '\n':
            arr.append(int(el))
    
    delete_direction = True
    if not done:
        for ch in commands:
            if ch == 'R':
                delete_direction = not delete_direction
            elif ch == 'D':
                if len(arr):
                    if delete_direction:
                        arr.popleft()
                    else:
                        arr.pop()
                else:
                    print('error')
                    done = True
                    break
    
    if not done:
        answer = '['
        if len(arr):
            if not delete_direction:
                arr.reverse()
            answer += ','.join(list(map(str, arr)))
        answer += ']'
        print(answer)
    
