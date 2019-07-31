tries = int(input())

for _ in range(tries):
    case_num = int(input())

    input_list = list(map(int, input().split()))

    input_dict = dict()
    for value in input_list:
        if value in input_dict.keys():
            input_dict[value] += 1
        else:
            input_dict[value] = 0

    result = 0
    value_max = -1
    for key, value in input_dict.items():
        if value > value_max:
            value_max = value
            result = key

    print('#{} {}'.format(case_num, result))

