# import sys
# sys.stdin = open('test_input.txt', 'r')
#
# print(sys.stdin.read())

tries = 10
for try_num in range(1, tries + 1):
    len_test_case = int(input())
    buildings = list(map(int, input().split()))

    result = 0
    for i in range(2, len_test_case - 2):
        left_max = max(buildings[i-1], buildings[i-2])
        right_max = max(buildings[i+1], buildings[i+2])
        two_max = max(left_max, right_max)

        if buildings[i] - two_max > 0:
            result += buildings[i] - two_max

    print('#{} {}'.format(try_num, result))
