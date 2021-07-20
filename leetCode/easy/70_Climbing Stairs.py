class Solution:
    def climbStairs(self, n: int) -> int:
        sheet = [1, 2, 3]
        while len(sheet) != n and n > 3:
            sheet.append(sheet[-1] + sheet[-2])

        return sheet[n - 1]
