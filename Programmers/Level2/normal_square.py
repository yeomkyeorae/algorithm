import math


def solution(w, h):
    if w == 1 or h == 1:
        return 0
    
    answer = w * h
    deleted = 0
    before = 0
    
    routine = 0
    for x in range(w + 1):
        if x == 0:
            continue
        
        y = (h * x) / w
        up = math.ceil(y)
        down = math.floor(before)
        deleted += up - down
        before = y
        
        if y == int(y):
            routine = x
            break
            
    routine_cnt = w // routine
    deleted = deleted * routine_cnt
        
    return answer - deleted