tries = int(input())
for i in range(1, tries + 1):
    num = int(input())
    result_list = [i if i % 2 else -i for i in range(1, num+1)]
    print('#{} {}'.format(i, sum(result_list)))
