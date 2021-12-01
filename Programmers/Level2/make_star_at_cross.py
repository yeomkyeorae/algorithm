import sys


def solution(line):
    dict_x_y = dict()
    
    min_x = sys.maxsize
    max_x = -sys.maxsize
    min_y = sys.maxsize
    max_y = -sys.maxsize
    
    for i in range(len(line) - 1):
        source = line[i]
        for target in line[i + 1:]:
            A, B, E = source
            C, D, F = target
            
            criteria = A * D - B * C
            if criteria == 0:
                continue
            x = (B * F - E * D) / criteria
            y = (E * C - A * F) / criteria
            
            int_x = int(x)
            int_y = int(y)
            if int_x == x and int_y == y:
                if int_y in dict_x_y.keys():
                    dict_x_y[int_y].add(int_x)
                else:
                    dict_x_y[int_y] = set([int_x])

                if min_x > int_x:
                    min_x = int_x
                if max_x < int_x:
                    max_x = int_x
                if min_y > int_y:
                    min_y = int_y
                if max_y < int_y:
                    max_y = int_y
    answer = []            
    for i in range(abs(min_y - max_y) + 1):
        key = max_y - i
        part_answer = ""
        if key in dict_x_y.keys():
            x_list = sorted(list(dict_x_y[key]), reverse=True)
            popped = x_list.pop()
            for j in range(abs(min_x - max_x) + 1):
                if min_x + j == popped:
                    part_answer += "*"
                    if x_list:
                        popped = x_list.pop()
                else:
                    part_answer += "."
        else:
            part_answer = "." * (abs(min_x - max_x) + 1)
        answer.append(part_answer)

    return answer