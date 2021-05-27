def get_binary(value):
    binary = ""
    q = value

    if value == 1:
        return "1"

    while q >= 2:
        r = q % 2
        binary += str(r)
        q = q // 2
        if q < 2:
            if q != 0:
                binary += str(q)

    return binary[::-1]


def solution(s):
    binary_convert_cnt = 0
    delete_zero_cnt = 0

    while True:
        new_s = []
        binary_convert_cnt += 1
        for one_ch in s:
            if one_ch == "0":
                delete_zero_cnt += 1
            else:
                new_s.append(s)
        length = len(new_s)
        converted = get_binary(length)

        if converted == "1":
            break
        s = converted

    answer = [binary_convert_cnt, delete_zero_cnt]

    return answer
