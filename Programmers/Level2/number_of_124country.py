def solution(n):
    answer = ''
    n = 10
    for i in range(19, -1, -1):
        if n <= 3:
            if n == 3:
                answer += '4'
            elif n == 2:
                answer += '2'
            elif n == 1:
                answer += '1'
            n = ''
            break

        p = 3 ** i

        if n > p:
            tmp = ''
            if n > p:
                tmp = '1'
            if n > p * 2:
                tmp = '2'
            if n > p * 3:
                tmp = '3'
            if tmp != '':
                answer += tmp
                n -= p * int(tmp)

            # if n > p * 3:
            #     answer += '4'
            #     n -= p * 3
            # elif n > p * 2 and n < p:
            #     answer += '2'
            #     n -= p * 2
            # elif n > p * 1 and n < (p / 2):
            #     answer += '1'
            #     n -= p * 1

    answer += str(n)

    return answer
