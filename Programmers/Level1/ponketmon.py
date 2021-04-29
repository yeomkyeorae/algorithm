def solution(nums):
    answer = 0
    how_many_i_can_gotcha = len(nums) // 2
    unique_mons = len(set(nums))

    if unique_mons > how_many_i_can_gotcha:
        answer = how_many_i_can_gotcha
    else:
        answer = unique_mons

    return answer
