tries = int(input())

for t in range(1, tries + 1):
    tmp_input = int(input())

    # 나사 정보 입력 받기
    nasa_list = list(map(int, input().split()))

    nasa_dict = {}
    # 딕셔너리 입력
    for ix in range(0, len(nasa_list), 2):
        nasa_dict[nasa_list[ix]] = nasa_list[ix + 1]

    start_list = [key for key in nasa_dict.keys()]

    result = ''
    i = 0
    for start in start_list:
        while True:
            try:
                result += str(start) + ' ' + str(nasa_dict[start]) + ' '
                start = nasa_dict[start]
                i += 1
                if i == tmp_input:
                    break
            except KeyError:
                result = ''
                i = 0
                break
        if i == tmp_input:
            break

    print('#{} {}'.format(t, result[:-1]))
