class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        x = 0
        while 4 ** x < n:
            x += 1
        four_num = 4 ** x
        if four_num == n:
            return True
        else:
            return False
