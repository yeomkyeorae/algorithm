import math
from collections import deque


def left_first(center, num):
    left, right = center - 1, center + 1
    d = deque()
    d.append(center)
    for i in range(num - 1):
        if i % 2:
            d.append(right)
            right += 1
        else:
            if left < 0:
                return []
            d.appendleft(left)
            left -= 1
    return d


def right_first(center, num):
    left, right = center - 1, center + 1
    d = deque()
    d.append(center)
    for i in range(num - 1):
        if i % 2:
            if left < 0:
                return []
            d.appendleft(left)
            left -= 1
        else:
            d.append(right)
            right += 1

    return d


def makeAnswer(arr):
    return ' '.join(list(map(str, arr)))


N, L = map(int, input().split(' '))

answer = -1
for num in range(L, 101):
    center = N / num
    center1 = math.floor(center)
    center2 = math.ceil(center)

    a = left_first(center1, num)
    if sum(a) == N:
        answer = makeAnswer(a)
        break

    b = right_first(center1, num)
    if sum(b) == N:
        answer = makeAnswer(b)
        break

    c = left_first(center2, num)
    if sum(c) == N:
        answer = makeAnswer(c)
        break

    d = right_first(center2, num)
    if sum(b) == N:
        answer = makeAnswer(b)
        break

print(answer)
