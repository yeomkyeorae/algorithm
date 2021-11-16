def check_possible_zip(arr, window, answer):
    for start_row in range(0, len(arr), window):
        for start_col in range(0, len(arr), window):
            flag = True
            
            one_cnt = 0
            zero_cnt = 0
            
            for row in range(start_row, start_row + window):
                for col in range(start_col, start_col + window):
                    if arr[row][col] == 2:
                        flag = False
                        break
                    
                    if arr[row][col]:
                        one_cnt += 1
                    else:
                        zero_cnt += 1
                        
                    if one_cnt and zero_cnt:
                        flag = False
                        break
                    
                if not flag:
                    break

            if flag:
                if arr[start_row][start_col]:
                    answer[1] += 1
                else:
                    answer[0] += 1
                for row in range(start_row, start_row + window):
                    for col in range(start_col, start_col + window):
                        arr[row][col] = 2
                        
    return answer
        
            
def solution(arr):
    answer = [0, 0]
    
    window_size = []
    length = len(arr)
    while length:
        window_size.append(length)
        length = int(length // 2)

    for window in window_size:
        answer = check_possible_zip(arr, window, answer)
    
    return answer