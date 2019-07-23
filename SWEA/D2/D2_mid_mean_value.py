num = int(input())
for i in range(1, num+1):
    # 입력
    tmp_list = list(map(int, input().split()))

    # max 값 제거
    tmp_list.remove(max(tmp_list))

    # min 값 제거
    tmp_list.remove(min(tmp_list))

    # 평균 출력
    print('#{} {}'.format(i, round(sum(tmp_list)/len(tmp_list))))
