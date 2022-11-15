def solution(food):
    answer = ''
    for i, f in enumerate(food[1:]):
        food_ix = i + 1
        food_num = f // 2
        for _ in range(food_num):
            answer += str(food_ix)

    lst = list(answer)
    lst.reverse()

    print(lst)

    answer += '0'
    answer += ''.join(lst)

    return answer
