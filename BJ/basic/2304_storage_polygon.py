# 참고: https://kimmeh1.tistory.com/268
# stack 활용
N = int(input())

max_height = -1
max_ix = -1
bars = [0] * 1001
for _ in enumerate(range(N)):
    loc, height = map(int, input().split(' '))
    bars[loc] = height

    if max_height < height:
        max_height = height
        max_ix = loc

answer = 0
stack = []
# 맨 좌측에서 가장 높은 곳으로
for i in range(max_ix + 1):
    height = bars[i]
    if not stack:
        stack.append(height)
        answer += stack[-1]
    else:
        if stack[-1] < height:
            stack.pop()
            stack.append(height)
        answer += stack[-1]

stack = []
# 맨 우측에서 가장 높은 곳으로
for i in range(len(bars) - 1, max_ix, -1):
    height = bars[i]
    if not stack:
        stack.append(height)
        answer += stack[-1]
    else:
        if stack[-1] < height:
            stack.pop()
            stack.append(height)
        answer += stack[-1]

print(answer)