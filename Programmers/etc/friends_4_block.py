def solution(m, n, board):
    answer = 0

    # board 구분
    tmp_board = []
    for string in board:
        tmp = []
        for ch in string:
            tmp.append(ch)
        tmp_board.append(tmp)
    board = tmp_board

    # 색출
    flag = True

    while flag:
        flag = False
        to_be_removed = []
        # 4블록 찾기
        for r, row_board in enumerate(board):
            for c, _ in enumerate(row_board):
                me = board[r][c]

                if me == 0:
                    continue

                if r < m - 1 and c < n - 1:
                    if me == board[r][c + 1] and me == board[r + 1][c] and me == board[r + 1][c + 1]:
                        flag = True
                        to_be_removed.append([r, c])
                        to_be_removed.append([r + 1, c])
                        to_be_removed.append([r, c + 1])
                        to_be_removed.append([r + 1, c + 1])

        if not flag:
            break

        # 4블록 위치 0으로 만들기
        for r, c in to_be_removed:
            board[r][c] = 0

        # 터진 자리 메꾸기
        for c in range(n):
            for r in range(m - 1, -1, -1):
                if board[r][c] == 0:
                    for next_r in range(r - 1, -1, -1):
                        if board[next_r][c] != 0:
                            board[r][c], board[next_r][c] = board[next_r][c], board[r][c]
                            break

    answer = 0
    for row_board in board:
        for value in row_board:
            if value == 0:
                answer += 1

    return answer
