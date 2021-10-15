import math


def solution(board):
    answer = 0
    
    max_row = len(board)
    max_col = len(board[0])
    
    candi_width = 0
    if max_row > max_col:
        candi_width = max_col
    else:
        candi_width = max_row
    
    is_finished = False
    for window in range(candi_width, 0, -1):
        for row in range(max_row - window + 1):
            not_r = -1
            not_c = -1
            for col in range(max_col - window + 1):
                done = True
                
                if row <= not_r and col <= not_c:
                    continue
                
                for r in range(window):
                    flag = True
                    for c in range(window):
                        if not board[row + r][col + c]:
                            not_r = row + r
                            not_c = col + c
                            flag = False
                            break
                    if not flag:
                        done = False
                        break
            
                if done:
                    is_finished = True
                    break
                    
            if is_finished:
                break
                
        if is_finished:
            answer = window * window
            break
            
    return answer