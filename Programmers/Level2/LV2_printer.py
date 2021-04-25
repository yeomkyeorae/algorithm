from collections import deque


def check(popped, d):
    for one in d:
        if one[1] > popped[1]:
            return False
    return True


def solution(priorities, location):
    d = deque()
    for i, priority in enumerate(priorities):
        d.append([i, priority])

    answer = 0
    while True:
        popped = d.popleft()
        if check(popped, d):
            answer += 1
            if popped[0] == location:
                return answer
        else:
            d.append(popped)