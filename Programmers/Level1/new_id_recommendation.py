def solution(new_id):
    # lv1
    answer = ''
    for ch in new_id:
        if 'A' <= ch < 'Z':
            answer += ch.lower()
        else:
            answer += ch

    # lv2
    new_id = answer
    answer = ''
    for ch in new_id:
        if 'a' <= ch <= 'z' or ch in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            answer += ch
        elif ch == '-' or ch == '_' or ch == '.':
            answer += ch

    # lv3
    new_id = answer
    answer = ''
    dot_num = 0
    for ch in new_id:
        if ch == '.':
            dot_num += 1
        else:
            if dot_num >= 1:
                answer += '.'
            answer += ch
            dot_num = 0
    if(dot_num > 0):
        answer += '.'

    # lv4
    new_id = answer
    answer = ''
    if len(new_id) and new_id[0] == '.':
        new_id = new_id[1:]
    if len(new_id) and new_id[-1] == '.':
        new_id = new_id[:-1]
    answer = new_id

    # lv5
    if answer == '':
        answer = 'a'

    # lv6
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:14]

    # lv7
    if len(answer) <= 2:
        add_str = answer[-1]
        for _ in range(2):
            answer += add_str
            if len(answer) == 3:
                break

    return answer
