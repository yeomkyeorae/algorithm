from itertools import combinations


def solution(relation):    
    answer = 0
    row_num = len(relation)
    col_num = len(relation[0])
    
    col_indexes = []
    for i in range(col_num):
        col_indexes.append(i)
    
    # 가능한 키의 인덱스 조합
    combs = []
    for r in range(1, col_num + 1):
        for comb in list(combinations(col_indexes, r)): 
            combs.append(list(comb))
    
    candidates = []
    SPLITER = 'A'
    for comb in combs:
        # 최소성 체크
        flag = False
        for candi in candidates:
            check_cnt = 0
            for row in candi:
                if row in comb:
                    check_cnt += 1
            if check_cnt == len(candi):
                flag = True
            if flag:
                break
        if flag:
            continue
        
        # 튜플 concat
        tmp_set = set()
        for row in relation:
            tuple_sum = ''
            for c in comb:
                if len(tuple_sum) > 0:
                    tuple_sum += SPLITER   
                tuple_sum += str(row[c])
            tmp_set.add(tuple_sum)
    
        # 유일성 체크
        if len(tmp_set) == row_num:
            candidates.append(comb)
            answer += 1

    return answer