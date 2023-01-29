from collections import deque

def solution(x, y, n):
    d = deque([[y, 0]])    
    
    while d:
        v, s = d.popleft()
        if v == x:
            return s
    
        if v % 3 == 0:
            d.append([v // 3, s + 1])
        
        if v % 2 == 0:
            d.append([v // 2, s + 1])
        
        if v - n >= x:
            d.append([v - n, s + 1])
            
    return -1