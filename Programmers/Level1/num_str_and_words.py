def solution(s):
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    words = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 
            'four': '4', 'five': '5', 'six': '6', 'seven': '7',
             'eight': '8', 'nine': '9'
            }
    answer = ''
    tmp = ''
    words_key = list(words.keys())
    for ch in s:
        if ch in nums:
            answer += ch
        else:
            tmp += ch
            if tmp in words_key:
                answer += words[tmp]
                tmp = ''
    
    return int(answer)