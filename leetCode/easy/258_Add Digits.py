class Solution:
    def addDigits(self, num: int) -> int:
        str_num = str(num)
        while len(str_num) != 1:
            tmp_num = 0
            for ch in str_num:
                tmp_num += int(ch)
            str_num = str(tmp_num)

        return int(str_num)
