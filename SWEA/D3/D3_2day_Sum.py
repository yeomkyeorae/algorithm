for i in range(1, 11):
    tmp_input = input()

    total_list = []
    for _ in range(100):
        total_list.append(list(map(int, input().split())))

    result = []
    # 가로 더하기
    for r in range(len(total_list)):
        result.append(sum(total_list[r]))

    # 세로 더하기
    for c in range(len(total_list)):
        tmp_sum = 0
        for r in range(len(total_list)):
            tmp_sum += total_list[r][c]
        result.append(tmp_sum)

    # 우하향 대각선 더하기
    tmp_sum = 0
    for diag in range(len(total_list)):
        tmp_sum += total_list[diag][diag]
    result.append(tmp_sum)

    # 좌하향 대각선 더하기
    tmp_sum = 0
    for ix in range(len(total_list)):
        tmp_sum += total_list[ix][len(total_list) - ix - 1]
    result.append(tmp_sum)

    result = max(result)
    print('#{} {}'.format(i, result))
