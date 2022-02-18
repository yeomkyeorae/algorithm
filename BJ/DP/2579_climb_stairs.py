import sys

input = sys.stdin.readline

N = int(input())
stairs = []
for _ in range(N):
    stair = int(input())
    stairs.append(stair)
    
if N == 1:
    print(stairs[-1])
elif N == 2:
    print(sum(stairs))
else:
    memo = [0] * N
    memo[0] = stairs[0]
    memo[1] = max(stairs[0] + stairs[1], stairs[1])
    memo[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

    for i in range(3, N):
        memo[i] = max(memo[i - 2] + stairs[i], memo[i - 3] + stairs[i - 1] + stairs[i])

    print(memo[-1])