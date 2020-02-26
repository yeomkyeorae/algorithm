def solution(s):
    min_value = len(s)
    for unit in range(1, len(s) - 1):
        compressed = ''
        for ix in range(0, len(s), unit):
            if ix == 0:
                tmp_string = s[ix:ix + unit]
                cnt = 1
                continue

            if s[ix:ix + unit] == tmp_string:
                cnt += 1
            else:
                if cnt > 1:
                    compressed += str(cnt) + tmp_string
                else:
                    compressed += tmp_string
                tmp_string = s[ix:ix + unit]
                cnt = 1
        if cnt > 1:
            compressed += str(cnt) + tmp_string
        else:
            compressed += tmp_string
        if len(compressed) < min_value:
            min_value = len(compressed)

    return min_value