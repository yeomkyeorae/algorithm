tries = int(input())
change_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for i in range(1, tries + 1):
    price = int(input())

    nums = []
    for change in change_list:
        if price >= change:
            nums.append(str(price // change))
            price = price % change
        else:
            nums.append('0')
    print('#{}'.format(i))
    print(' '.join(nums))
