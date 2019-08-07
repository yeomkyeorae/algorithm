def bingo_check(matrix):
    bingo_num = 0

    # 가로 파악
    for row in range(5):
        flag = True
        for col in range(5):
            if not matrix[row][col] == 0:
                flag = False
                break
        if flag:
            bingo_num += 1
        if bingo_num == 3:
            return True

    # 세로 파악
    for col in range(5):
        flag = True
        for row in range(5):
            if not matrix[row][col] == 0:
                flag = False
                break
        if flag:
            bingo_num += 1
        if bingo_num == 3:
            return True

    # 우하향 파악
    flag = True
    for i in range(5):
        if not matrix[i][i] == 0:
            flag = False
            break

    if flag:
        bingo_num += 1
    if bingo_num == 3:
        return True

    # 좌하향 파악
    flag = True
    for i in range(5):
        if not matrix[i][5 - 1 - i] == 0:
            flag = False
            break
    if flag:
        bingo_num += 1

    if bingo_num == 3:
        return True
    else:
        return False


def do_bingo(matrix):

    # 게임 숫자를 저장하는 2차원 리스트
    num_list = []
    for _ in range(5):
        input_list = list(map(int, input().split()))
        num_list.append(input_list)

    # 숫자 부른 횟수 count
    cnt = 0

    # 게임 숫자 한 줄
    for nums in num_list:
        # 게임 숫자 하나
        for num in nums:
            cnt += 1
            for row, one_list in enumerate(matrix):
                if num in one_list:
                    # 불린 숫자 matrix column 위치
                    col = one_list.index(num)
                    # 불린 숫자 0으로 처리
                    matrix[row][col] = 0

                    # 빙고 3개이면
                    if bingo_check(matrix):
                        return cnt


if __name__ == "__main__":
    # 빙고판 입력 받기
    bingo_list = []
    for _ in range(5):
        one_row = list(map(int, input().split()))
        bingo_list.append(one_row)

    # 최소 횟수 출력
    print(do_bingo(bingo_list))
