max_score = 0
max_result = []


def get_score(info, result):
    cur_score = 10
    
    info_score = 0
    result_score = 0
    for a, b in zip(info, result):
        if b > a:
            result_score += cur_score
        elif a > 0:
            info_score += cur_score
            
        cur_score -= 1
        
    return result_score - info_score


def who_is_better(a, b):
    for i in range(10, -1, -1):
        if a[i] < b[i]:
            return b[:]
        elif a[i] > b[i]:
            return a[:]
    return a
        

def go(info, stage, arrow, result):
    global max_score 
    global max_result

    if len(result) == 11:
        if arrow > 0:
            result[10] = result[-1] + arrow
        
        score = get_score(info, result)
        if score == max_score and len(max_result) > 0:            
            max_result = who_is_better(result, max_result)
        
        if score > max_score:
            max_score = score
            max_result = result[:]

        return
    
    need_arrow = info[stage] + 1
    
    if arrow - need_arrow >= 0:
        result.append(need_arrow)
        go(info, stage + 1, arrow - need_arrow, result)
        result.pop()
    
    result.append(0)
    go(info, stage + 1, arrow, result)
    result.pop()

    
    
def solution(n, info):
    global max_result
    global max_score
    
    go(info, 0, n, [])
    
    answer = max_result
    if answer == []:
        answer = [-1]
    
    return answer