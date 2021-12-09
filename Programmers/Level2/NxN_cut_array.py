def solution(n, left, right):
    answer = []
    
    left_row = 0
    left_col = 0
    while True:
        if left < (left_row + 1) * n:
            col = 0
            while (left_row * n) + col != left:
                col += 1
            left_col = col
            break
        left_row += 1
    
    right_row = 0
    right_col = 0
    while True:
        if right < (right_row + 1) * n:
            col = 0
            while (right_row * n) + col != right:
                col += 1
            right_col = col
            break
        right_row += 1

    for add_row in range(right_row - left_row + 1):
        row = left_row + add_row
        value = row + 1
        for col in range(n):
            if col > row:
                value += 1
            if row == left_row and col < left_col:
                continue
            if row == right_row and col > right_col:
                break
            answer.append(value)
    
    return answer