from collections import deque

convert = {
    1: 3,
    3: 1,
    2: 4,
    4: 2
}

length = int(input())
target = deque(map(int, input().split(' ')))

targets = []
for _ in range(length):
    v = target.popleft()
    target.append(v)
    
    targets.append(list(target))
    
    tmp = []
    for v in target:
        tmp.append(convert[v])
    targets.append(tmp)

    new_list = list(target)[::-1]
    targets.append(new_list)
    
    tmp2 = []
    for v in new_list:
        tmp2.append(convert[v])
    targets.append(tmp2)


N = int(input())
answer = []
for _ in range(N):
    polygon = list(map(int, input().split(' ')))
    if polygon in targets:
        answer.append(polygon)

print(len(answer))

for lst in answer:
    str_list = list(map(str, lst))
    print(' '.join(str_list))
