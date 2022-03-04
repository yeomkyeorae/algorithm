from itertools import combinations


N = int(input())

max_value = 0
answer = 0
for i, _ in enumerate(range(N)):
    lst = list(map(int, input().split(' ')))
    
    for comb in combinations(lst, 3):
        summation = sum(comb)
        one = int(str(summation)[-1])
        
        if max_value <= one:
            max_value = one
            answer = i + 1

print(answer)
