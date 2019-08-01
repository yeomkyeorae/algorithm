tries = int(input())

for t in range(1, tries + 1):
    k, n, m = map(int, input().split())
    stop_list = [0]   # 현재 위치 추가
    stop_list = stop_list + list(map(int, input().split()))
    stop_list = stop_list + [n]   # 종점 위치 추가

    # 종점까지 못 가는 경우 계산
    for ix in range(1, len(stop_list)):
        if stop_list[ix] - stop_list[ix - 1] > k:  # 정류장과 정류장 사이의 거리가 연비 초과이면
            print('#{} {}'.format(t, 0))
            flag = False
            break
        else:
            flag = True

    # 종점까지 갈 수 있으면
    if flag:
        result = 0   # 정류장 몇개 들렀는지
        stop_by = 0  # 현재 머문 정류장
        can_go = k   # 현재 정류장에서 나아갈 수 있는 최대 위치
        while stop_by + k < stop_list[len(stop_list) - 1]:  # 현재 머문 정류장에서 종점까지 갈 수 있으면 종료
            for i in range(len(stop_list)-2, 0, -1):  # 정류장 위치가 먼 것부터 검색
                if stop_list[i] <= can_go:  # 현재 위치에서 해당 정류장을 갈 수 있으면
                    result += 1
                    can_go = stop_list[i] + k  # 앞으로 나아갈 수 있는 최대 거리 갱신
                    stop_by = stop_list[i]     # 머문 정류장 위치 갱신
                    break

        print('#{} {}'.format(t, result))


