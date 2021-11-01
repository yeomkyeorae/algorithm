def solution(sizes):
    answer = 0
    
    max_w, max_h = 0, 0
    for size in sizes:
        size.sort()
        w, h = size
        if max_w < w:
            max_w = w
        if max_h < h:
            max_h = h
    
    return max_w * max_h