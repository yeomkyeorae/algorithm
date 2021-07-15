class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        string_num = str(x)
        string_reversed = string_num[::-1]
        num_reversed = int(string_reversed)
        
        if x == num_reversed:
            return True
        else:
            return False
