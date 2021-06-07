from itertools import combinations


def solution(orders, course):
    comb_dict = {}
    course_max_dict = {}
    for c in course:
        course_max_dict[c] = 0
        for order in orders:
            combs = list(combinations(order, c))
            for comb in combs:
                key = ''.join(sorted(comb))
                if key in comb_dict:
                    comb_dict[key] += 1
                    if comb_dict[key] > course_max_dict[c]:
                        course_max_dict[c] = comb_dict[key]
                else:
                    comb_dict[key] = 1

    answer = []
    for k1, v1 in course_max_dict.items():
        if v1 <= 1:
            continue
        for k2, v2 in comb_dict.items():
            if k1 == len(k2) and v1 == v2:
                answer.append(k2)
    answer = sorted(answer)
    return answer
