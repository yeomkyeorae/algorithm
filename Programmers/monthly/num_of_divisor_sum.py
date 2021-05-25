def solution(left, right):
    answer = 0
    for num in range(left, right + 1):
        cnt = 0
        for q in range(1, num + 1):
            if num % q == 0:
                cnt += 1
        if cnt % 2:
            answer -= num
        else:
            answer += num

    return answer
