def rotate(input_list):
    rotated_list = []
    for c in range(len(input_list)):
        tmp_list = []
        for r in range(len(input_list) - 1, -1, -1):
            tmp_list.append(input_list[r][c])
        rotated_list.append(tmp_list)

    return rotated_list


tries = int(input())

for i in range(1, tries + 1):
    n = int(input())
    board = []
    for row in range(n):
        board.append(list(map(int, input().split())))

    board_one = rotate(board)
    board_two = rotate(board_one)
    board_three = rotate(board_two)

    print('#{}'.format(i))
    for j in range(n):
        print('{} {} {}'.format(''.join([str(x) for x in board_one[j]]), ''.join([str(x) for x in board_two[j]]), ''.join([str(x) for x in board_three[j]])))

