tries = int(input())

for i in range(1, tries + 1):
    print('#{}'.format(i))

    ch_dict = {}
    for _ in range(int(input())):
        ch, num = input().split()
        num = int(num)
        ch_dict[ch] = num

    total_list = []
    for k, v in ch_dict.items():
        for _ in range(v):
            total_list.append(k)

    while len(total_list) > 0:
        if len(total_list) >= 10:
            for ix in range(10):
                print(total_list[ix], end='')
            print()
            total_list = total_list[10:]
        else:
            for ix in range(len(total_list)):
                print(total_list[ix], end='')
            print()
            break

