def solution(numbers, hand):
    answer = ''
    left_loc = 10
    right_loc = 12
    num_map = [[], 
               [0, 0], [1, 0], [2, 0], 
               [0, 1], [1, 1], [2, 1], 
               [0, 2], [1, 2], [2, 2],
               [0, 3], [1, 3], [2, 3]]
    
    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            left_loc = num
            continue
        elif num in [3, 6, 9]:
            answer += 'R'
            right_loc = num~
            continue
        
        if(num == 0): num = 11
            
        left_distance = abs(num_map[left_loc][0] - num_map[num][0]) + abs(num_map[left_loc][1] - num_map[num][1])
        
        right_distance = abs(num_map[right_loc][0] - num_map[num][0]) + abs(num_map[right_loc][1] - num_map[num][1])
        
        if left_distance > right_distance:
            answer += 'R'
            right_loc = num
        elif left_distance < right_distance:``
            answer += 'L'
            left_loc = num
        else:
            if hand == 'right':
                answer += 'R'
                right_loc = num
            else:
                answer += 'L'
                left_loc = num
                
    return answer