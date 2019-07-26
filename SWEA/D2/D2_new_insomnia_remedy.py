tries = int(input())

for i in range(1, tries + 1):
    num_set = set()
    num = int(input())

    new_num = num
    for tried in range(1, 1000000 + 1):
        for ch in str(new_num):
            if not int(ch) in num_set:
                num_set.add(int(ch))
        if len(num_set) == 10:
            print('#{} {}'.format(i, new_num))
            break
        new_num = tried * num