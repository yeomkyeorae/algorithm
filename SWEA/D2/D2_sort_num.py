def my_sort(one_list):

    tmp_list = []
    while len(one_list) > 0:
        min_value = min(one_list)
        tmp_list.append(str(min_value))
        one_list.remove(min_value)
    return tmp_list


tries = int(input())


for i in range(1, tries + 1):
    tmp = input()
    num_list = list(map(int, input().split()))
    print('#{} {}'.format(i, ' '.join(my_sort(num_list))))
