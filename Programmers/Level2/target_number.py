answer = 0


def go(numbers, index, target, length, value):
    global answer

    if index == length:
        if value == target:
            answer += 1
        return

    for mode in range(2):
        if mode == 0:
            go(numbers, index + 1, target, length, value + numbers[index])
        else:
            go(numbers, index + 1, target, length, value - numbers[index])

    return answer


def solution(numbers, target):
    length = len(numbers)
    answer = go(numbers, 0, target, length, 0)

    return answer
