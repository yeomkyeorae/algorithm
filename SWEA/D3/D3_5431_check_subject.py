tries = int(input())

for t in range(1, tries + 1):
    N, K = map(int, input().split())
    done = list(map(int, input().split()))

    check_dict = {}
    for k in range(1, N + 1):
        check_dict[k] = 0

    for d in done:
        check_dict[d] = 1

    answer_list = []
    for k in range(1, N + 1):
        if not check_dict[k]:
            answer_list.append(str(k))

    print('#{} {}'.format(t, ' '.join(answer_list)))
