class Solution:
    def reverse(self, x: int) -> int:
        answer = ''
        if x < 0:
            answer += '-'
        
        string_num = str(abs(x))
        string_num = string_num[::-1]
        
        answer += string_num
        
        answer = int(answer)
        if not -(2**31) <= answer <= 2**31 - 1:
            return 0
        
        return answer
