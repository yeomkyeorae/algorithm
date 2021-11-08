def split(string):
    open_cnt, close_cnt = 0, 0
    barometer = 0
    for ix, ch in enumerate(string):
        if ch == '(':
            open_cnt += 1
        elif ch == ')':
            close_cnt += 1
            
        if open_cnt and close_cnt and open_cnt == close_cnt:
            barometer = ix
            break

    u, v = string[:barometer + 1], string[barometer + 1:]
    
    return u, v


def test_correct_string(u):
    stack = []
    fail = False
    for ch in u:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if stack:
                stack.pop()
            else:
                fail = True
                break
    
    if not fail and not stack:
        return True
    else:
        return False


def go(string):    
    if string == '':
        return string
    
    u, v = split(string)
    
    answer = ''
    if test_correct_string(u):
        answer = u + go(v)
        return answer
    else:
        tmp = '(' + go(v) + ')'
        deleted = u[1:len(u) - 1]
        transformed = ''
        for d in deleted:
            ch = ''
            if d == '(':
                ch = ')'
            elif d == ')':
                ch = '('
            transformed += ch
        
        return tmp + transformed
    

def solution(p):
    if test_correct_string(p):
        return p
    
    answer = go(p)
    
    return answer