N = int(input())

answer = 0
for one in range(1, N):
    for two in range(one, N):
        three = N - one - two
        
        if two > three:
            break
        
        if one + two > three:
            answer += 1
        
print(answer)