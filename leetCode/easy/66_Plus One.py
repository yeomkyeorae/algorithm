class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            value = (digits[i] + 1) % 10
            digits[i] = value
            if value != 0:
                break

        if digits[0] == 0:
            answer = digits[::-1]
            answer.append(1)
            digits = answer[::-1]

        return digits
