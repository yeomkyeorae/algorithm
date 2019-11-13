def go(num, ix):

    global max_value
    global min_value

    if ix == len(nums):
        if num > max_value:
            max_value = num
        if num < min_value:
            min_value = num
        return

    if operator_nums[0]:
        operator_nums[0] -= 1
        go(num + nums[ix], ix + 1)
        operator_nums[0] += 1

    if operator_nums[1]:
        operator_nums[1] -= 1
        go(num - nums[ix], ix + 1)
        operator_nums[1] += 1

    if operator_nums[2]:
        operator_nums[2] -= 1
        go(num * nums[ix], ix + 1)
        operator_nums[2] += 1

    if operator_nums[3]:
        operator_nums[3] -= 1
        go(int(num / nums[ix]), ix + 1)
        operator_nums[3] += 1


tries = int(input())

for t in range(1, tries + 1):
    n = int(input())
    operator_nums = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    max_value = -1000000001
    min_value = 1000000001
    go(nums[0], 1)

    print('#{} {}'.format(t, max_value - min_value))
