def solution(numbers):
    answer = []
    for num in numbers:
        if num == 0:
            answer.append(1)
            continue
        
        if num % 2 == 0:
            answer.append(num + 1)
            continue
        
        n = 0
        binary = format(num, 'b')
        for b in binary[::-1]:
            if b == '1':
                n += 1   
            else:
                break

        answer.append(num + (2 ** (n - 1)))

    return answer