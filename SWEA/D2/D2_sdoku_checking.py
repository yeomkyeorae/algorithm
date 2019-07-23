tries = int(input())
for i in range(1, tries+1):
    row_list = []
    col_list = []
    square_list = []

    # row 방향 숫자들 추가 (가로 방향)
    row_part_list = []
    for _ in range(9):
        row_list.append(list(map(int, input().split())))
        # row_list[row][col]

    # col 방향 숫자들 추가 (세로 방향)
    col_list = []
    for col_ix in range(9):
        col_part_list = []
        for row_ix in range(9):
            col_part_list.append(row_list[row_ix][col_ix])
        col_list.append(col_part_list)

    # square 형태의 숫자들 추가
    square_list = []
    start_col_ix, end_col_ix = 0, 3
    start_row_ix, end_row_ix = 0, 3
    for _ in range(9):
        square_part_list = []
        for col_ix in range(start_col_ix, end_col_ix):
            for row_ix in range(start_row_ix, end_row_ix):
                square_part_list.append(row_list[row_ix][col_ix])

        square_list.append(square_part_list)

        start_col_ix += 3
        end_col_ix += 3
        if end_col_ix > 9:
            start_col_ix = 0
            end_col_ix = 3
            start_row_ix += 3
            end_row_ix += 3

    result = 1
    if result:  # row 검증
        for row_ix in range(9):
            if len(set(row_list[row_ix])) != 9:
                result = 0
                break
    if result:  # col 검증
        for col_ix in range(9):
            if len(set(col_list[col_ix])) != 9:
                result = 0
                break
    if result:  # square 검증
        for square_ix in range(9):
            if len(set(square_list[square_ix])) != 9:
                result = 0
                break

    print('#{} {}'.format(i, result))
