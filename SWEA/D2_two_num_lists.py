tries = int(input())

for i in range(1, tries + 1):
    a_num, b_num = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    if a_num > b_num:
        tmp_list = a_list
        a_list = b_list
        b_list = tmp_list

    ix_count = 0
    result_list = []
    for a_value in a_list:
        tmp_list = []
        for b_ix in range(ix_count, len(b_list) - len(a_list) + ix_count + 1):
            tmp_list.append(a_value * b_list[b_ix])
        ix_count += 1
        result_list.append(tmp_list)

    max_value = 1e-19
    for c in range(len(result_list[0])):
        tmp_value = 0
        for r in range(len(result_list)):
            tmp_value += result_list[r][c]
        if tmp_value > max_value:
            max_value = tmp_value

    print('#{} {}'.format(i, max_value))
