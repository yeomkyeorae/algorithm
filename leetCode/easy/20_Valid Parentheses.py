class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        paren_dict = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        open_paren = paren_dict.values()
        for ch in s:
            if ch in open_paren:
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                
                current_open_paren = stack.pop()
                if paren_dict[ch] != current_open_paren:
                    return False
                
        if len(stack) == 0:
            return True 
        else:
            return False
                
