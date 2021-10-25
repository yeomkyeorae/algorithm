perms = []
length = 0

def get_perm(stage, cur_perms):
    global perms

    if stage == length:
        perms.append(cur_perms[:])
    
    for i in range(length):
        if i in cur_perms:
            continue
        cur_perms.append(i)
        get_perm(stage + 1, cur_perms)
        cur_perms.pop()
        

def solution(k, dungeons):
    global perms
    global length
    
    length = len(dungeons)
    answer = 0
    
    get_perm(0, [])
    
    tmp_k = k
    for p in perms:
        tmp_answer = 0
        
        for i in p:
            minimum_t, consume_t = dungeons[i]
            if minimum_t <= tmp_k:
                tmp_k -= consume_t
                tmp_answer += 1
            else:
                break
        
        if answer < tmp_answer:
            answer = tmp_answer
        
        tmp_k = k
    
    return answer