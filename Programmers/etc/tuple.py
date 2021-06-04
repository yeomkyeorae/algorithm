def solution(s):
    length = len(s.split('},{'))

    s = s[1:len(s) - 1]
    s = s.replace('{', '')
    s = s.replace('}', '')

    cnt_dict = {}
    for ch in s.split(','):
        num = int(ch)
        if num in cnt_dict.keys():
            cnt_dict[num] += 1
        else:
            cnt_dict[num] = 1

    answer = [0] * length
    for k, v in cnt_dict.items():
        answer[length - v] = k

    return answer
