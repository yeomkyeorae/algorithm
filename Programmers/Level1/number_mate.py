def solution(X, Y):
    x_dict = {}
    for x in X:
        if x in x_dict.keys():
            x_dict[x] += 1
        else:
            x_dict[x] = 1
            
    y_dict = {}
    for y in Y:
        if y in y_dict.keys():
            y_dict[y] += 1
        else:
            y_dict[y] = 1
            
    answer = ''
    for key in range(9, -1, -1):
        key = str(key)
        if key in x_dict.keys() and key in y_dict.keys():
            x_key, y_key = x_dict[key], y_dict[key]
            
            k = 0
            if x_key < y_key:
                k = x_key
            else:
                k = y_key
                
            for _ in range(k):
                if key == '0' and answer == '0':
                    break
                answer += key
    
    if answer == '':
        return '-1'
    
    return answer