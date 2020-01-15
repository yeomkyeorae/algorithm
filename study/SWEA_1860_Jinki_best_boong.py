N = int(input())
for t in range(1, N + 1):
    n, m, k = map(int, input().split())
    customer_list = list(map(int, input().split()))
    customer_list.sort()

    sec = 1
    ix = 0
    boong_num = 0
    people_num = 0
    while True:
        if customer_list[0] == 0:
            answer = 'Impossible'
            break

        if sec % m == 0:
            boong_num += k
        while True:
            if ix == len(customer_list):
                break
            if customer_list[ix] <= sec:
                people_num += 1
                ix += 1
            else:
                break
        boong_num -= people_num
        people_num = 0
        if boong_num < 0:
            answer = 'Impossible'
            break

        if ix == len(customer_list):
            answer = 'Possible'
            break

        sec += 1

    print('#{} {}'.format(t, answer))
