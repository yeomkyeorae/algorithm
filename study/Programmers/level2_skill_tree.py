def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        for ix, current_skill in enumerate(skill_tree):
            is_possible = True
            tmp = []
            is_included_in_skill = False
            for one_skill in skill:
                if one_skill == current_skill:
                    is_included_in_skill = True
                    break
                tmp.append(one_skill)
            if is_included_in_skill:
                for t in tmp:
                    if t not in skill_tree[:ix]:
                        is_possible = False
                        break
            if not is_possible:
                break
        if is_possible:
            answer += 1

    return answer