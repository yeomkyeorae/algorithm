tries = int(input())

for i in range(1, tries + 1):
    people_num = int(input())
    throw_list = list(map(int, input().split()))

    abs_throw_list = [abs(throw) for throw in throw_list]

    min_value = min(abs_throw_list)
    nice_num = abs_throw_list.count(min_value)

    print('#{} {} {}'.format(i, min_value, nice_num))
