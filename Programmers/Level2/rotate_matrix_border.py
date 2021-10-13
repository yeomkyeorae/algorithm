from collections import deque


def solution(rows, columns, queries):
    num = 1
    board = []
    for _ in range(rows):
        tmp_board = []
        for _ in range(columns):
            tmp_board.append(num)
            num += 1
        board.append(tmp_board)
    
    answer = []
    for q in queries:
        axis_value = []
        r1, c1, r2, c2 = q
        r1 -= 1
        c1 -= 1
        r2 -= 1
        c2 -= 1
        
        d = deque()
        
        min_value = rows * columns
        for col in range(c2 - c1 + 1):
            axis_value.append([r1, c1 + col])
            value = board[r1][c1 + col]
            d.append(value)
            if min_value > value:
                min_value = value
        for row in range(r2 - r1):
            axis_value.append([r1 + row + 1, c2])
            value = board[r1 + row + 1][c2]
            d.append(value)
            if min_value > value:
                min_value = value
        for col in range(c2 - c1):
            axis_value.append([r2, c2 - col - 1])
            value = board[r2][c2 - col - 1]
            d.append(value)
            if min_value > value:
                min_value = value
        for row in range(r2 - r1 - 1):
            axis_value.append([r2 - row - 1, c1])
            value = board[r2 - row - 1][c1]
            d.append(value)
            if min_value > value:
                min_value = value
                
        answer.append(min_value)
        
        last = d.pop()
        d.appendleft(last)
        
        for row, col in axis_value:
            board[row][col] = d.popleft()
            
    return answer