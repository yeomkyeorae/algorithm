class Solution:
    def isHappy(self, n: int) -> bool:
        cnt = 0
        while n != 1:
            string = str(n)
            num = 0
            for ch in string:
                num += int(ch) ** 2
            n = num
            cnt += 1

            if cnt > 5:
                break

        if n == 1:
            return True
        else:
            return False
