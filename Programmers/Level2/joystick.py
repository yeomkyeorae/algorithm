def is_done(init_lst, name):
    flag = True
    for ch1, ch2 in zip(init_lst, name):
        if ch1 != ch2:
            flag = False
            break
    return flag


def get_up_down_cnt(ch):
    up_cnt = ord(ch) - ord('A')
    down_cnt = ord('Z') - ord(ch) + 1

    if up_cnt > down_cnt:
        return down_cnt
    else:
        return up_cnt


def left_go(name):
    answer = 0
    init_lst = ["A" for _ in range(len(name))]

    up_down_cnt = get_up_down_cnt(name[0])
    answer += up_down_cnt
    init_lst[0] = name[0]

    if is_done(init_lst, name):
        return answer

    loc = len(name)
    for i in range(len(name) - 1, -1, -1):
        up_down_cnt = get_up_down_cnt(name[i])
        answer += up_down_cnt
        init_lst[i] = name[i]

        if is_done(init_lst, name):
            loc = i
            break

    answer += len(name) - loc

    return answer


def right_go(name):
    answer = 0
    init_lst = ["A" for _ in range(len(name))]

    loc = 0
    for i in range(len(name)):
        up_down_cnt = get_up_down_cnt(name[i])
        answer += up_down_cnt
        init_lst[i] = name[i]

        if is_done(init_lst, name):
            loc = i
            break

    answer += loc

    return answer


def right_and_left_go(name):
    answer = 0
    init_lst = ["A" for _ in range(len(name))]

    loc = 0
    for i in range(len(name) // 2):
        up_down_cnt = get_up_down_cnt(name[i])
        answer += up_down_cnt
        init_lst[i] = name[i]

        if is_done(init_lst[:len(name) // 2], name[:len(name) // 2]):
            loc = i
            break
    answer += loc * 2

    loc = len(name)
    for i in range(len(name) - 1, (len(name) // 2) - 1, -1):
        up_down_cnt = get_up_down_cnt(name[i])
        answer += up_down_cnt
        init_lst[i] = name[i]

        if is_done(init_lst, name):
            loc = i
            break
    answer += len(name) - loc

    return answer


def solution(name):
    left_answer = left_go(name)
    right_answer = right_go(name)
    right_left_answer = right_and_left_go(name)

    answers = [left_answer, right_answer, right_left_answer]
    answers.sort()

    return answers[0]
