def solution(n, arr1, arr2):
    answer = []
    board = []
    for _ in range(n):
        board.append([' '] * n)
    for r, v in enumerate(arr1):
        bin_str = bin(v)[2:]
        if len(bin_str) < n:
            tmp = ''
            for _ in range(n - len(bin_str)):
                tmp += '0'
            bin_str = tmp + bin_str
        for c, b in enumerate(bin_str):
            if b == '1':
                board[r][c] = '#'
    for r, v in enumerate(arr2):
        bin_str = bin(v)[2:]
        if len(bin_str) < n:
            tmp = ''
            for _ in range(n - len(bin_str)):
                tmp += '0'
            bin_str = tmp + bin_str
        for c, b in enumerate(bin_str):
            if b == '1':
                board[r][c] = '#'
    answer = []
    for one_list in board:
        answer.append("".join(one_list))

    return answer