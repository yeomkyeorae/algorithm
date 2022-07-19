import sys

input = sys.stdin.readline

n = int(input())
num_dict = {}
for _ in range(n):
    num = int(input())
    try:
        num_dict[num] += 1
    except KeyError:
        num_dict[num] = 1

answer = 0
expectation = 1
for rank in range(1, n + 1):
    while True:
        try:
            count = num_dict[expectation]
            if count == 0:
                expectation += 1
                continue

            answer += abs(rank - expectation)
            num_dict[expectation] -= 1

            break
        except KeyError:
            expectation += 1

print(answer)
