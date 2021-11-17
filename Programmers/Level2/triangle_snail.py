def solution(n):
    value = 1
    stage = []
    for _ in range(n):
        stage.append([])
        
    stage_ix = -1
    stage_type = 'down'
    while n:
        for current_stage in range(n):
            if stage_type == 'down':
                stage_ix += 1
                stage[stage_ix].append(value)
            elif stage_type == 'horizon':
                stage[stage_ix].append(value)
            elif stage_type == 'up':
                stage_ix -= 1
                stage[stage_ix].append(value)
            value += 1
            
        if stage_type == 'down':
            stage_type = 'horizon'
        elif stage_type == 'horizon':
            stage_type = 'up'
        elif stage_type == 'up':
            stage_type = 'down'
        
        n -= 1
        
    answer = []
    for s in stage:
        visited = [0] * len(s)
        flag = False
        consecutive_start_ix = 0
        for i, v in enumerate(s[::2]):
            answer.append(v)
            visited[i * 2] = 1
            if i * 2 + 1 < len(s) and v + 1 == s[i * 2 + 1]:
                consecutive_start_ix = i * 2
                flag = True
                break
        
        if flag:
            for i, v in enumerate(s[consecutive_start_ix + 1:]):
                answer.append(v)
                visited[consecutive_start_ix + i + 1] = 1
                
        for i, v in enumerate(s[::-1]):
            if not visited[len(s) - i - 1]:
                answer.append(v)
    
    return answer