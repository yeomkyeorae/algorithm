# 실패
# 보드 크기 입력
r, c = map(int, input().split())

# whether it goes or not 체크
ch_dict = {}

# 보드 및 체크 초기화
board = []
for ix in range(r):
    tmp_list = []
    input_string = input()
    for ch in input_string:
        ch_dict[ch] = False
        tmp_list.append(ch)
    board.append(tmp_list)

y_axis = 0
x_axis = 0
count = 1


def go(y_axis, x_axis, count, ch_dict):

    count1 = count
    count2 = count
    count3 = count
    count4 = count

    ch_dict[board[y_axis][x_axis]] = True

    # 위
    if y_axis != 0 and ch_dict[board[y_axis - 1][x_axis]] is False:
        count1 = go(y_axis - 1, x_axis, count + 1, ch_dict)
        ch_dict[board[y_axis - 1][x_axis]] = False
    # 왼쪽
    if x_axis != 0 and ch_dict[board[y_axis][x_axis - 1]] is False:
        count2 = go(y_axis, x_axis - 1, count + 1, ch_dict)
        ch_dict[board[y_axis][x_axis - 1]] = False
    # 아래
    if y_axis != r - 1 and ch_dict[board[y_axis + 1][x_axis]] is False:
        count3 = go(y_axis + 1, x_axis, count + 1, ch_dict)
        ch_dict[board[y_axis + 1][x_axis]] = False
    # 오른쪽
    if x_axis != c - 1 and ch_dict[board[y_axis][x_axis + 1]] is False:
        count4 = go(y_axis, x_axis + 1, count + 1, ch_dict)
        ch_dict[board[y_axis][x_axis + 1]] = False

    max_value = max([count1, count2, count3, count4])

    return max_value


result = go(y_axis, x_axis, count, ch_dict)
print(result)