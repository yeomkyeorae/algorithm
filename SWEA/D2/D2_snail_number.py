tries = int(input())

for i in range(1, tries + 1):
    n = int(input())

    # 2차원 리스트로 사용할 변수
    total_list = []
    # 0으로 초기화한 리스트 total_list에 추가
    for _ in range(n):
        total_list.append([0] * n)
    # mapping = [[0] * n for _ in range(n)] 한 줄로 2차원 리스트 정의하기

    # total_list에 추가할 값
    num = 0

    # 각각의 방향으로 이동할 때의 출발 값 초기화
    right_start = 0
    down_start = 1
    left_start = n - 2
    up_start = n - 2

    # 각 방향으로 이동할 떄 고정되어야할 row 또는 col 방향의 index 초기화
    fixed_ix = 0
    while True:
        # 오른쪽으로 이동할 때
        for c in range(right_start, n):
            # 리스트 값이 0일 때(순회하지 않았을 때)
            if total_list[fixed_ix][c] == 0:
                num += 1
                total_list[fixed_ix][c] = num
                # 리스트 끝까지 갔을 때
                if c == n - 1:
                    fixed_ix = c
            # 전에 순회한 적이 있으면
            else:
                # 이전 c 값으로 초기화
                fixed_ix = c - 1
                break
        # 다음 오른쪽으로 이동할 때의 변경될 출발 값
        right_start += 1
        # 이후 위와 거의 상동

        # 아래로 이동할 때
        for r in range(down_start, n):
            if total_list[r][fixed_ix] == 0:
                num += 1
                total_list[r][fixed_ix] = num
                if r == n - 1:
                    fixed_ix = r
            else:
                fixed_ix = r - 1
                break
        down_start += 1

        # 왼쪽으로 이동할 때
        for c in range(left_start, -1, -1):
            if total_list[fixed_ix][c] == 0:
                num += 1
                total_list[fixed_ix][c] = num
                if c == 0:
                    fixed_ix = c
            else:
                fixed_ix = c + 1
                break
        left_start -= 1

        # 위로 올라갈 때
        for r in range(up_start, -1, -1):
            if total_list[r][fixed_ix] == 0:
                num += 1
                total_list[r][fixed_ix] = num
            else:
                fixed_ix = r + 1
                break
        up_start -= 1

        # while문이 무한 loop에 빠지는 것을 방지하기 위한 조건문
        if right_start > n - 1 or down_start > n - 1 or left_start < 0 or up_start < 0:
            break

    print('#{}'.format(i))
    for one_row in total_list:
        one_row = map(str, one_row)
        print(' '.join(one_row))
