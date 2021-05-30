from collections import deque


def check_bracket(d):
    stack = []
    for value in d:
        if value in ['(', '{', '[']:
            stack.append(value)
        else:
            if len(stack) == 0:
                return False
            last = stack.pop()
            if value == ')' and last == '(':
                pass
            elif value == '}' and last == '{':
                pass
            elif value == ']' and last == '[':
                pass
            else:
                return False

    if len(stack) > 0:
        return False

    return True


def solution(s):
    answer = 0

    d = deque(list(s))
    for _ in range(len(d)):
        if check_bracket(d):
            answer += 1
        d.append(d.popleft())

    return answer
