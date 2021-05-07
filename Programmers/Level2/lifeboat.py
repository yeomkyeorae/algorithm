def solution(people, limit):
    answer = 0

    min_value = min(people)
    new_people = []
    for p in people:
        if limit - p < min_value:
            answer += 1
        else:
            new_people.append(p)

    people_dict = {}
    for p in new_people:
        if p in people_dict.keys():
            people_dict[p] += 1
        else:
            people_dict[p] = 1

    unique_weight = list(people_dict.keys())
    unique_weight.sort(reverse=True)

    total_cnt = len(new_people)
    while total_cnt > 0:
        for a in unique_weight[::-1]:
            if people_dict[a] > 0:
                new_limit = limit - a

                hook_b = False
                for b in unique_weight:
                    if a == b:
                        if people_dict[b] >= 2 and new_limit - b >= 0:
                            more = people_dict[a] // 2
                            people_dict[a] -= (more + more)
                            total_cnt -= (more + more)
                            answer += more
                            hook_b = True
                            break
                    elif people_dict[b] > 0 and new_limit - b >= 0:
                        more = 0
                        if people_dict[a] >= people_dict[b]:
                            more = people_dict[b]
                        else:
                            more = people_dict[a]
                        people_dict[a] -= more
                        people_dict[b] -= more
                        total_cnt -= (more + more)
                        answer += more
                        hook_b = True
                        break
                if hook_b == False:
                    people_dict[a] -= 1
                    total_cnt -= 1
                    answer += 1

    return answer
