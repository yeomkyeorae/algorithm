def check(place, row, col, stage, orig_row, orig_col):
    if row < 0 or row > 4 or col < 0 or col > 4:
        return True
    
    if stage > 0 and row == orig_row and col == orig_col:
        return True
    
    if stage == 1 and place[row][col] == 'P':
        return False
    
    if stage == 1 and place[row][col] == 'X':
        return True
    
    if stage == 2:
        if place[row][col] == 'P':
            return False
        else:
            return True
    
    flag = check(place, row + 1, col, stage + 1, orig_row, orig_col)
    if flag:
        flag = check(place, row - 1, col, stage + 1, orig_row, orig_col)
    if flag:
        flag = check(place, row, col + 1, stage + 1, orig_row, orig_col)
    if flag:
        flag = check(place, row, col - 1, stage + 1, orig_row, orig_col)
    
    return flag


def solution(places):
    answer = []
    for place in places:
        place_flag = 1
        for row in range(5):
            for col in range(5):
                if place[row][col] == 'P':
                    flag = check(place, row, col, 0, row, col)
                    if not flag:
                        place_flag = 0
            if not place_flag:
                break
        answer.append(place_flag)
                    
    return answer