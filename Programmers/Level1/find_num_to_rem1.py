def solution(n):
    answer = 0
    for num in range(n, 1, -1):
        if n % num == 1:
            answer = num
    
    return answer

